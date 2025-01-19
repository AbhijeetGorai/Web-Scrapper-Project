# Use Python 3.10 as base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY src/web_scrapper /app/web_scrapper

# Set Python path
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Expose port 8000
EXPOSE 8000

# Command to run the FastAPI server
CMD ["uvicorn", "web_scrapper.api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] 