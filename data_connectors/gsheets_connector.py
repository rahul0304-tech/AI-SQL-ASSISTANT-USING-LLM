import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from data_connectors.base_connector import DataConnector

class GoogleSheetsConnector(DataConnector):
    def __init__(self, credentials_file, spreadsheet_id):
        self.credentials_file = credentials_file
        self.spreadsheet_id = spreadsheet_id
        self.client = None
        self.spreadsheet = None
        self.worksheets = {}
    
    def connect(self):
        try:
            scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
            creds = ServiceAccountCredentials.from_json_keyfile_name(self.credentials_file, scope)
            self.client = gspread.authorize(creds)
            self.spreadsheet = self.client.open_by_key(self.spreadsheet_id)
            
            # Cache all worksheets
            for worksheet in self.spreadsheet.worksheets():
                self.worksheets[worksheet.title] = worksheet
                
            return True
        except Exception as e:
            print(f"Error connecting to Google Sheets: {e}")
            return False
    
    def execute_query(self, query):
        """Execute a query on Google Sheets
        
        The query should be a dictionary with:
        - worksheet: the worksheet name
        - operation: 'read' | 'filter'
        - filter_column: column to filter on (optional)
        - filter_value: value to filter by (optional)
        """
        try:
            if not self.client or not self.spreadsheet:
                self.connect()
            
            worksheet_name = query.get('worksheet')
            if not worksheet_name or worksheet_name not in self.worksheets:
                return pd.DataFrame({"error": [f"Worksheet not found: {worksheet_name}"]})
            
            worksheet = self.worksheets[worksheet_name]
            data = worksheet.get_all_records()
            df = pd.DataFrame(data)
            
            # Apply filter if specified
            if 'filter_column' in query and 'filter_value' in query:
                df = df[df[query['filter_column']] == query['filter_value']]
            
            return df
            
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame({"error": [f"Error: {e}"]})
    
    def get_schema(self):
        if not self.client or not self.spreadsheet:
            self.connect()
        
        schema_data = []
        for worksheet_name, worksheet in self.worksheets.items():
            # Get the header row
            headers = worksheet.row_values(1)
            
            # Get a sample row to infer types
            if worksheet.row_count > 1:
                sample_row = worksheet.row_values(2)
                for i, header in enumerate(headers):
                    data_type = "string"  # Default type
                    if i < len(sample_row):
                        value = sample_row[i]
                        try:
                            float(value)
                            if '.' in value:
                                data_type = "float"
                            else:
                                data_type = "integer"
                        except:
                            data_type = "string"
                    
                    schema_data.append({
                        "worksheet": worksheet_name,
                        "column": header,
                        "type": data_type
                    })
        
        return pd.DataFrame(schema_data)
    
    def close(self):
        # Nothing to explicitly close with gspread
        pass