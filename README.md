# Automation Tool

A lightweight Python automation tool demonstrating pip, PyPI, and scripting fundamentals.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python generate_log.py
```

## Features

- Writes a timestamped log file (`log_YYYYMMDD.txt`) from a list of entries
- Fetches a sample post from a public API using `requests`
- Raises `ValueError` when called with non-list input
- Creates a valid (empty) log file when given an empty list

## Project Structure

```
.
├── generate_log.py
├── requirements.txt
├── README.md
└── .gitignore
```
