# Python String Calculator

A Python implementation of a string calculator that parses and evaluates mathematical expressions provided as strings.

## Overview

The Python String Calculator is a utility library that takes string-based mathematical expressions and computes their results. It handles basic arithmetic operations and provides a clean, simple API for expression evaluation.

## Features

- Parse and evaluate mathematical expressions from strings
- Support for basic arithmetic operations
- Comprehensive test coverage with pytest
- Type hints for better code clarity
- Development-ready with code quality tools

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/arpit1003/Python-string-calculaor.git
cd Python-string-calculaor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from string_calculator import calculate

result = calculate("2 + 2")
print(result)  # Output: 4
```

## Development

### Project Structure

```
.
├── src/                 # Source code
├── tests/              # Test suite
├── requirements.txt    # Project dependencies
├── pytest.ini         # Pytest configuration
├── LICENSE            # Apache 2.0 License
└── README.md          # This file
```

### Running Tests

Run the test suite using pytest:

```bash
pytest
```

For coverage report:

```bash
pytest --cov=src
```

### Code Quality

Format your code with Black:

```bash
black src/ tests/
```

Sort imports with isort:

```bash
isort src/ tests/
```

Type checking with mypy:

```bash
mypy src/
```

## Dependencies

- **pytest** >= 7.0.0 - Testing framework
- **pytest-cov** >= 3.0.0 - Code coverage
- **black** >= 22.0.0 - Code formatter
- **isort** >= 5.0.0 - Import sorter
- **mypy** >= 0.900 - Static type checker

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

- [arpit1003](https://github.com/arpit1003)