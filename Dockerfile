# Use Python 3.9 as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY src/ ./src/

# Set Python path
ENV PYTHONPATH=/app

# Expose port 8000
EXPOSE 8000

# Command to run the FastAPI server
CMD ["python", "src/web_scrapper/run_server.py"] 