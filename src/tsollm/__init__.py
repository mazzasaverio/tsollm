"""TSO-LLM - Template Structured Output for Large Language Models."""

__version__ = "0.1.0"
__author__ = "Saverio Mazza"
__email__ = "saverio3107@gmail.com"

from .core import (
    TSO,
    extract_note_info,
    extract_bookmark_info,
)
from .schemas import (
    NoteClassification,
    BookmarkClassification,
)
from .exceptions import (
    TSOError,
    ConfigurationError,
    ExtractionError,
    SchemaValidationError,
)

__all__ = [
    "TSO",
    "extract_note_info",
    "extract_bookmark_info",
    "NoteClassification",
    "BookmarkClassification",
    "TSOError",
    "ConfigurationError",
    "ExtractionError",
    "SchemaValidationError",
]
