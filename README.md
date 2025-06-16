# TSO-LLM

**Template Structured Output for Large Language Models**

[![PyPI version](https://badge.fury.io/py/tsollm.svg)](https://badge.fury.io/py/tsollm)
[![Tests](https://github.com/yourusername/tsollm/workflows/Tests/badge.svg)](https://github.com/yourusername/tsollm/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A powerful Python package providing predefined schemas for OpenAI's Structured Outputs. Get structured data from text using battle-tested templates - no schema design needed!

## ✨ Features

- 🎯 **Predefined Templates**: Ready-to-use schemas for common use cases
- ⚡ **Structured Outputs**: Guaranteed JSON schema compliance via OpenAI
- 📝 **Note Classification**: Categorize and prioritize notes automatically
- 🔖 **Bookmark Organization**: Intelligently catalog URLs and web content
- 🛡️ **Type Safety**: Full Pydantic validation and type hints
- 🧪 **Well Tested**: Comprehensive test suite with 95%+ coverage
- 📚 **Easy to Use**: Simple API with convenience functions

## 🚀 Installation

```bash
pip install tsollm
```

## 🔧 Quick Start

```python
import os
from tsollm import TSO

# Set your OpenAI API key
os.environ['OPENAI_API_KEY'] = 'your-api-key-here'

# Initialize TSO
tso = TSO()

# Extract structured information from a note
note_text = "Remember to buy groceries tomorrow - milk, bread, eggs. This is urgent!"
result = tso.extract(note_text, "note")
print(result)
# Output: {
#     "title": "Grocery Shopping",
#     "category": "personal",
#     "priority": "urgent",
#     "tags": ["shopping", "groceries"],
#     "summary": "Buy milk, bread, and eggs tomorrow",
#     "actionable": True,
#     "due_date": "2024-01-15"
# }

# Extract bookmark information
url_text = "https://github.com/openai/openai-python - Official OpenAI Python library"
bookmark = tso.extract(url_text, "bookmark") 
print(bookmark)
# Output: {
#     "title": "OpenAI Python Library",
#     "description": "Official Python library for OpenAI API",
#     "category": "tool",
#     "tags": ["python", "openai", "api", "library"],
#     "domain": "github.com",
#     "language": "en",
#     "content_type": "tool",
#     "estimated_read_time": 15,
#     "usefulness_score": 9,
#     "is_free": True
# }
```

## 📖 Usage Examples

### Note Classification

```python
from tsollm import extract_note_info

# Simple note extraction
note = "Team meeting at 2 PM tomorrow to discuss Q4 goals"
result = extract_note_info(note)
print(f"Category: {result['category']}")  # work
print(f"Priority: {result['priority']}")  # medium
print(f"Actionable: {result['actionable']}")  # True
```

### Bookmark Classification

```python
from tsollm import extract_bookmark_info

# Bookmark extraction
bookmark_text = """
https://docs.python.org/3/tutorial/
The Python Tutorial - comprehensive guide covering Python basics
"""
result = extract_bookmark_info(bookmark_text)
print(f"Category: {result['category']}")  # documentation
print(f"Usefulness: {result['usefulness_score']}")  # 9
print(f"Read time: {result['estimated_read_time']} minutes")  # 45
```

### Advanced Usage with Context

```python
from tsollm import TSO

tso = TSO()

# Provide additional context for better extraction
context = "This is from a project management meeting"
note_text = "Finalize the API documentation by Friday"

result = tso.extract(
    note_text, 
    "note", 
    additional_context=context
)
print(result)
```

### Schema Exploration

```python
from tsollm import TSO

tso = TSO()

# Get all available schemas
schemas = tso.get_supported_schemas()
print(f"Available schemas: {list(schemas.keys())}")

# Get detailed schema information
note_info = tso.get_schema_info("note")
print(f"Schema: {note_info['name']}")
print(f"Fields: {list(note_info['fields'].keys())}")
```

## 📋 Available Templates

### Note Classification Schema

Automatically categorizes and structures notes with:

- **Categories**: personal, work, study, idea, todo, meeting, other
- **Priorities**: low, medium, high, urgent
- **Tags**: Relevant keywords (max 5)
- **Summary**: Brief description (max 200 chars)
- **Actionable**: Boolean flag for actionable items
- **Due Date**: Optional ISO date format

### Bookmark Classification Schema

Intelligently organizes web content with:

- **Categories**: news, blog, documentation, tutorial, tool, resource, social, entertainment, shopping, reference, other
- **Content Types**: article, video, podcast, image, document, tool, homepage, other
- **Usefulness Score**: 1-10 rating for content quality
- **Language**: ISO 639-1 language code
- **Read Time**: Estimated minutes (optional)
- **Access**: Free vs paid content flag

## 🛠️ Configuration

### API Key Setup

```python
import os
from tsollm import TSO

# Method 1: Environment variable (recommended)
os.environ['OPENAI_API_KEY'] = 'your-key-here'
tso = TSO()

# Method 2: Direct parameter
tso = TSO(api_key='your-key-here')
```

### Model Configuration

```python
from tsollm import TSO

# Configure model and temperature
tso = TSO(
    model="gpt-4o-2024-08-06",  # Default model
    temperature=0.1,            # Lower = more deterministic
    api_key="your-key-here"
)
```

## 📊 Error Handling

```python
from tsollm import TSO, ExtractionError, ConfigurationError

try:
    tso = TSO(api_key="invalid-key")
    result = tso.extract("test note", "note")
except ConfigurationError as e:
    print(f"Setup error: {e}")
except ExtractionError as e:
    print(f"Extraction failed: {e}")
except ValueError as e:
    print(f"Invalid schema type: {e}")
```

## 🧪 Testing

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=src/tsollm --cov-report=html
```

## 🤝 Contributing

Contributions are welcome! Please check out our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/tsollm.git
cd tsollm

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Run code quality checks
black src/ tests/
isort src/ tests/
flake8 src/ tests/
mypy src/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [PyPI Package](https://pypi.org/project/tsollm/)
- [Documentation](https://tsollm.readthedocs.io/)
- [GitHub Repository](https://github.com/yourusername/tsollm)
- [Issue Tracker](https://github.com/yourusername/tsollm/issues)

## 🙏 Acknowledgments

- Built with [OpenAI's Structured Outputs](https://openai.com/blog/introducing-structured-outputs-in-the-api)
- Powered by [Pydantic](https://pydantic.dev/) for data validation
- Inspired by the need for reliable LLM-based data extraction

---

**Made with ❤️ for the Python community**