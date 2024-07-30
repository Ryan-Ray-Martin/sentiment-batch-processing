# Use a Python 3.11 base image
FROM python:3.11.6-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set the entry point
CMD ["uvicorn", "batch_server:app", "--host", "0.0.0.0", "--port", "5000"]
