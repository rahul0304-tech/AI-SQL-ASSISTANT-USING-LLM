import os
from pathlib import Path
from typing import Dict, Any
from pydantic import BaseModel

class Config(BaseModel):
    # Project paths
    ROOT_DIR: Path = Path(__file__).parent.parent
    UPLOADS_DIR: Path = ROOT_DIR / "uploads"
    TRAININGS_DIR: Path = ROOT_DIR / "trainings"
    PROMPTS_DIR: Path = ROOT_DIR / "prompts"
    IMAGES_DIR: Path = ROOT_DIR / "images"

    # LLM Configuration
    DEFAULT_MODEL: str = "openai/gpt-3.5-turbo"
    DEFAULT_TEMPERATURE: float = 0.3
    DEFAULT_MAX_TOKENS: int = 500

    # Data Source Defaults
    DEFAULT_MYSQL_PORT: int = 3306
    DEFAULT_MONGODB_URI: str = "mongodb://localhost:27017"

    # UI Configuration
    PAGE_TITLE: str = "Query Assistant"
    PAGE_ICON: str = "🌄"
    SUPPORTED_FILE_TYPES: list[str] = ["csv", "xlsx", "xls"]

    @classmethod
    def load_env_vars(cls) -> Dict[str, Any]:
        """Load environment variables into a dictionary"""
        return {
            "OPENROUTER_API_KEY": os.getenv("OPENROUTER_API_KEY"),
            "SNOWFLAKE_USER": os.getenv("SNOWFLAKE_USER"),
            "SNOWFLAKE_PASSWORD": os.getenv("SNOWFLAKE_PASSWORD"),
            "SNOWFLAKE_ACCOUNT": os.getenv("SNOWFLAKE_ACCOUNT"),
            "SNOWFLAKE_DATABASE": os.getenv("SNOWFLAKE_DATABASE"),
            "SNOWFLAKE_SCHEMA": os.getenv("SNOWFLAKE_SCHEMA"),
        }

config = Config()