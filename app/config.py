"""
Configuration module for loading environment variables.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """Application settings loaded from environment variables."""
    google_api_key: str = os.getenv("GOOGLE_API_KEY", "")
    
    def __init__(self):
        if not self.google_api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")

# Create settings instance
settings = Settings()
