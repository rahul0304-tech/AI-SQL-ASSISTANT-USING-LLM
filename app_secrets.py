import streamlit as st
import os

# ... existing code ...

class AppSecrets:
    def __init__(self):
        self._openrouter_api_key = self._get_secret("OPENROUTER_API_KEY")

    def _get_secret(self, key):
        # Try to get the secret from Streamlit's secrets management first
        if key in st.secrets:
            return st.secrets[key]
        # Fallback to environment variables for local development
        elif os.getenv(key):
            return os.getenv(key)
        else:
            raise ValueError(f"Secret '{key}' not found in Streamlit secrets or environment variables.")
    @property
    def openrouter_api_key(self):
        return self._openrouter_api_key

# ... existing code ...