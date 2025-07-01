import pandas as pd
import mysql.connector
from data_connectors.base_connector import DataConnector

class MySQLConnector(DataConnector):
    def __init__(self, host, user, password, database, port=3306):
        self.connection_params = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port
        }
        self.conn = None
        self.cursor = None
    
    def connect(self):
        try:
            self.conn = mysql.connector.connect(**self.connection_params)
            self.cursor = self.conn.cursor(dictionary=True)
            return True
        except Exception as e:
            print(f"Error connecting to MySQL: {e}")
            return False
    
    def execute_query(self, query):
        try:
            if not self.conn or not self.cursor:
                self.connect()
                
            self.cursor.execute(query)
            
            # Check if the query is a SELECT query
            if self.cursor.description:
                results = self.cursor.fetchall()
                return pd.DataFrame(results)
            else:
                self.conn.commit()
                return pd.DataFrame({"message": [f"Query executed successfully. Rows affected: {self.cursor.rowcount}"]})
                
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame({"error": [f"Error: {e}"]})
    
    def get_schema(self):
        schema_query = """
        SELECT 
            TABLE_NAME as table_name, 
            COLUMN_NAME as column_name, 
            DATA_TYPE as data_type
        FROM 
            INFORMATION_SCHEMA.COLUMNS 
        WHERE 
            TABLE_SCHEMA = %s
        ORDER BY 
            TABLE_NAME, ORDINAL_POSITION
        """
        self.cursor.execute(schema_query, (self.connection_params['database'],))
        results = self.cursor.fetchall()
        return pd.DataFrame(results)
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()