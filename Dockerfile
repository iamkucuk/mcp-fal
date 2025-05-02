FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY . .

# Environment variable for the API key
ENV FAL_KEY=""

# Run the server with stdio
CMD ["python", "main.py"]