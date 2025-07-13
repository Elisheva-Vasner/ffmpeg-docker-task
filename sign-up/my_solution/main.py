import typer
import json
from typing import List

app = typer.Typer()

FILE_NAME = 'data.jsonl'

@app.command()
def add(txt: str):
    """
    Adds a JSON-formatted record to the file.
    """
    try:
        data_json = json.loads(txt)
        with open(FILE_NAME, 'a', encoding='utf-8') as f:
            f.write(json.dumps(data_json, ensure_ascii=False) + '\n')
        print("Data saved successfully.")
    except json.JSONDecodeError as e:
        print("Invalid JSON input.")
        print("Details:", e)

@app.command()
def show():
    # Displays the last 10 records from the file
    try:
        with open(FILE_NAME, 'r') as f:
            lines = f.readlines()[-10:]
            for line in lines:
                print(json.loads(line))
    except:
        print("No data found.")

if __name__ == "__main__":
    app()
