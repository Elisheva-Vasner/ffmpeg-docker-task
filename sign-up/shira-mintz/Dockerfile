FROM python:3.11-slim

WORKDIR /app

# install python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy code and image
COPY . .

# command
CMD ["python", "main.py"]
