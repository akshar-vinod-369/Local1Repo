# FROM python:3.10-alpine

# WORKDIR /app

# #RUN apk update && apk get-install vim

# COPY requirements.txt .

# RUN pip install -r requirements.txt

# COPY app.py .

# #EXPOSE 5002

# CMD ["python", "app.py"]

FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]