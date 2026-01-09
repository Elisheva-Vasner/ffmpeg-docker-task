# JSON Record CLI

This project is a simple command-line interface (CLI) built in Python using the Typer library.  
It allows users to **add JSON-formatted records** to a file and **view the latest entries**.

---

## Features

- Add records in JSON format to a `.jsonl` file
- View the last 10 records saved
- Run with or without Docker

---

## 📂 Files in the Project

- `main.py` — Main CLI logic using Typer  
- `requirements.txt` — Python dependencies  
- `Dockerfile` — Docker support for the app  
- `data.jsonl` — Where the JSON records are stored (auto-created)  

---

## How to Use

To run this project locally:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Add a new JSON record
python main.py add '{"name": "Alice", "age": 25}'

# 3. Show the last 10 records
python main.py show
