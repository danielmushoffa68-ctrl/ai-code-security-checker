# AI Code Security Checker

AI Code Security Checker is a simple Python project designed to help developers identify common security issues in source code during the development process.

## Purpose

The project provides a lightweight way to detect potentially unsafe coding patterns and encourages developers to consider security earlier in the software development lifecycle.

## Features

The current version can detect:

* Use of `eval()`
* Use of `exec()`
* Hardcoded passwords
* Potential hardcoded API keys
* Insecure HTTP URLs

## Technology

* Python 3
* Regular expressions
* Pytest

## Project Structure

```text
ai-code-security-checker/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── security_checker.py
└── tests/
    └── test_security_checker.py
```

## Usage

Run the security checker against a Python source file:

```bash
python src/security_checker.py example.py
```

Run the tests:

```bash
pytest
```

## Roadmap

Future improvements may include:

* AI-assisted code analysis
* Support for additional programming languages
* Dependency vulnerability detection
* GitHub Actions integration
* Automated security reports

## Importance

Security issues can be easier and less costly to address when they are identified early in the development process. This project provides a simple foundation for experimenting with automated code security analysis.

## License

MIT License

