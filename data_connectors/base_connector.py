from abc import ABC, abstractmethod
import pandas as pd

class DataConnector(ABC):
    """Base class for all data connectors"""
    
    @abstractmethod
    def connect(self):
        """Establish connection to the data source"""
        pass
    
    @abstractmethod
    def execute_query(self, query):
        """Execute a query and return results as a pandas DataFrame"""
        pass
    
    @abstractmethod
    def get_schema(self):
        """Return the schema information for this data source"""
        pass
    
    @abstractmethod
    def close(self):
        """Close the connection"""
        pass