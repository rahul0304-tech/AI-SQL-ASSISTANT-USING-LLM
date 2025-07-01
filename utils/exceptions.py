class SQLAssistantError(Exception):
    """Base exception class for SQL Assistant application."""
    pass

class ConfigurationError(SQLAssistantError):
    """Raised when there's an error in configuration settings."""
    pass

class ConnectionError(SQLAssistantError):
    """Raised when there's an error connecting to a data source."""
    pass

class QueryExecutionError(SQLAssistantError):
    """Raised when there's an error executing a query."""
    pass

class LLMError(SQLAssistantError):
    """Raised when there's an error with LLM operations."""
    pass

class FileOperationError(SQLAssistantError):
    """Raised when there's an error with file operations."""
    pass

class ValidationError(SQLAssistantError):
    """Raised when there's an error validating input data."""
    pass

class PromptTemplateError(SQLAssistantError):
    """Raised when there's an error with prompt templates."""
    pass