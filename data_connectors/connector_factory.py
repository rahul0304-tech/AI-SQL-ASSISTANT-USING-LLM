from data_connectors.snowflake_connector import SnowflakeConnector
from data_connectors.mongodb_connector import MongoDBConnector
from data_connectors.mysql_connector import MySQLConnector
from data_connectors.file_connector import FileConnector
from data_connectors.gsheets_connector import GoogleSheetsConnector

class ConnectorFactory:
    @staticmethod
    def create_connector(connector_type, **kwargs):
        """Create a connector based on the specified type"""
        if connector_type.lower() == 'snowflake':
            return SnowflakeConnector(
                user=kwargs.get('user'),
                password=kwargs.get('password'),
                account=kwargs.get('account'),
                warehouse=kwargs.get('warehouse'),
                database=kwargs.get('database'),
                schema=kwargs.get('schema'),
                role=kwargs.get('role')
            )
        
        elif connector_type.lower() == 'mongodb':
            return MongoDBConnector(
                connection_string=kwargs.get('connection_string'),
                database=kwargs.get('database')
            )
        
        elif connector_type.lower() == 'mysql':
            return MySQLConnector(
                host=kwargs.get('host'),
                user=kwargs.get('user'),
                password=kwargs.get('password'),
                database=kwargs.get('database'),
                port=kwargs.get('port', 3306)
            )
        
        elif connector_type.lower() in ['csv', 'excel']:
            return FileConnector(
                file_path=kwargs.get('file_path')
            )
        
        elif connector_type.lower() == 'gsheets':
            return GoogleSheetsConnector(
                credentials_file=kwargs.get('credentials_file'),
                spreadsheet_id=kwargs.get('spreadsheet_id')
            )
        
        else:
            raise ValueError(f"Unsupported connector type: {connector_type}")