from typing import Any, Dict, List, Optional
from pydantic import BaseModel, validator
from pathlib import Path
from .exceptions import ValidationError

class DataSourceConfig(BaseModel):
    """Validation model for data source configuration."""
    source_type: str
    connection_params: Dict[str, Any]

    @validator('source_type')
    def validate_source_type(cls, v):
        valid_sources = ["Snowflake", "MongoDB", "MySQL", "CSV/Excel", "Google Sheets"]
        if v not in valid_sources:
            raise ValidationError(f"Invalid source type. Must be one of: {valid_sources}")
        return v

    @validator('connection_params')
    def validate_connection_params(cls, v, values):
        source_type = values.get('source_type')
        if source_type == "MySQL":
            required = {"host", "port", "user", "password", "database"}
            if not all(k in v for k in required):
                raise ValidationError(f"Missing required MySQL parameters: {required}")
            if not isinstance(v['port'], int) or not (0 < v['port'] < 65536):
                raise ValidationError("Invalid MySQL port number")

        elif source_type == "MongoDB":
            if 'connection_string' not in v:
                raise ValidationError("MongoDB connection string is required")

        elif source_type in ["CSV/Excel", "Google Sheets"]:
            if source_type == "CSV/Excel" and 'file_path' not in v:
                raise ValidationError("File path is required for CSV/Excel")
            elif source_type == "Google Sheets":
                required = {"credentials_file", "spreadsheet_id"}
                if not all(k in v for k in required):
                    raise ValidationError(f"Missing required Google Sheets parameters: {required}")

        return v

def validate_file_upload(file_path: Path, allowed_extensions: List[str]) -> bool:
    """Validate uploaded file."""
    if not file_path.exists():
        raise ValidationError(f"File does not exist: {file_path}")
    
    if file_path.suffix.lower().lstrip('.') not in allowed_extensions:
        raise ValidationError(f"Invalid file type. Allowed types: {allowed_extensions}")
    
    return True

def validate_prompt(prompt: str) -> str:
    """Validate and sanitize user prompt."""
    if not prompt or not prompt.strip():
        raise ValidationError("Prompt cannot be empty")
    
    # Basic sanitization
    prompt = prompt.strip()
    
    # Add more validation rules as needed
    
    return prompt