import pandas as pd
from pymongo import MongoClient
from data_connectors.base_connector import DataConnector

class MongoDBConnector(DataConnector):
    def __init__(self, connection_string, database):
        self.connection_string = connection_string
        self.database_name = database
        self.client = None
        self.db = None
    
    def connect(self):
        try:
            self.client = MongoClient(self.connection_string)
            self.db = self.client[self.database_name]
            return True
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            return False
    
    def execute_query(self, query):
        """Execute MongoDB query
        
        The query should be a dictionary with:
        - collection: the collection name
        - operation: find, aggregate, etc.
        - filter: the filter criteria
        - projection: fields to return
        """
        try:
            if not self.client or not self.db:
                self.connect()
                
            collection = self.db[query['collection']]
            
            if query['operation'] == 'find':
                cursor = collection.find(
                    filter=query.get('filter', {}),
                    projection=query.get('projection', None)
                )
                return pd.DataFrame(list(cursor))
            
            elif query['operation'] == 'aggregate':
                cursor = collection.aggregate(query['pipeline'])
                return pd.DataFrame(list(cursor))
            
            else:
                return pd.DataFrame({"error": [f"Unsupported operation: {query['operation']}"]})
                
        except Exception as e:
            print(f"An error occurred: {e}")
            return pd.DataFrame({"error": [f"Error: {e}"]})
    
    def get_schema(self):
        collections = self.db.list_collection_names()
        schema_data = []
        
        for collection in collections:
            # Get a sample document to infer schema
            sample = self.db[collection].find_one()
            if sample:
                for field, value in sample.items():
                    schema_data.append({
                        "collection": collection,
                        "field": field,
                        "type": type(value).__name__
                    })
        
        return pd.DataFrame(schema_data)
    
    def close(self):
        if self.client:
            self.client.close()