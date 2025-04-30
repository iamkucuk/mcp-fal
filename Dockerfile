FROM python:3.10-slim

WORKDIR /app

# Copy requirements first to utilize Docker's caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Port for the MCP server (fastmcp default is 8000)
EXPOSE 8000

# Environment variable for the API key (will be overridden at runtime)
ENV FAL_KEY=""

# Command to run the server
CMD ["fastmcp", "serve", "main.py"]