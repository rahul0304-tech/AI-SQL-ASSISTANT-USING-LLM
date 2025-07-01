import snowflake.connector
import pandas as pd
from data_connectors.base_connector import DataConnector

class SnowflakeConnector(DataConnector):
    def __init__(self, user, password, account, warehouse, database, schema, role):
        self.connection_params = {
            'user': user,
            'password': password,
            'account': account,
            'warehouse': warehouse,
            'database': database,
            'schema': schema,
            'role': role
        }
        self.conn = None
        self.cur = None
    
    def connect(self):
        try:
            self.conn = snowflake.connector.connect(**self.connection_params)
            self.cur = self.conn.cursor()
            return True
        except Exception as e:
            print(f"Error connecting to Snowflake: {e}")
            return False
    
    def execute_query(self, query):
        try:
            if not self.conn or not self.cur:
                self.connect()
                
            self.cur.execute(query)
            query_results = self.cur.fetchall()
            column_names = [col[0] for col in self.cur.description]
            return pd.DataFrame(query_results, columns=column_names)
        except snowflake.connector.errors.ProgrammingError as pe:
            print(f"Query Compilation Error: {pe}")
            return pd.DataFrame({"error": [f"Query compilation error: {pe}"]})
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame({"error": [f"Error: {e}"]})
    
    def get_schema(self):
        schema_query = """SELECT table_name, column_name, data_type 
                        FROM information_schema.columns 
                        WHERE table_schema = '{}';""".format(self.connection_params['schema'])
        return self.execute_query(schema_query)
    
    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()