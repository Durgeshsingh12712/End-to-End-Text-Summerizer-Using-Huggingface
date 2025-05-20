import os, sys
from typing import Dict, Any
from textSummerizer.logging import logger

class InvalidTextError(Exception):
    """Raised when the input text is invalid or empty."""
    def __init__(self, message: str = "Invalid text input."):
        self.message = message
        super().__init__(self.message)
        logger.error(self.message)

class InvalidRatioError(Exception):
    """Raised when the summarization ratio is invalid."""
    def __init__(self, message: str = "Summarization ratio must be between 0 and 1."):
        self.message = message
        super().__init__(self.message)
        logger.error(self.message)

class TextTooShortError(Exception):
    """Raised when the input text is too short to summarize."""
    def __init__(self, message: str = "Input text is too short to summarize."):
        self.message = message
        super().__init__(self.message)
        logger.error(self.message)

class ConfigurationError(Exception):
    """Raised when there is a configuration issue."""
    def __init__(self, message: str = "Configuration error occurred."):
        self.message = message
        super().__init__(self.message)
        logger.error(self.message)

    def exception_handler(exception: Exception) -> Dict[str, Any]:
        """Generic exception handler for the application."""
        logger.error(f"An error occurred: {str(exception)}")
        return {
            "error": str(exception),
            "status": "failed"
        }
