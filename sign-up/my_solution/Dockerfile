# Base Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /myapp

# Copy project files into the container
COPY . /myapp

# Install required dependencies
RUN pip install -r requirements.txt

# Run the app
ENTRYPOINT ["python", "main.py"]
