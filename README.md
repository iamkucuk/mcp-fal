# fal.ai MCP Server

A Model Context Protocol (MCP) server for interacting with fal.ai models and services.

## Features

- List all available fal.ai models
- Search for specific models by keywords
- Get model schemas
- Generate content using any fal.ai model
- Support for both direct and queued model execution
- Queue management (status checking, getting results, cancelling requests)
- File upload to fal.ai CDN

## Requirements

- Python 3.10+ (for local installation)
- fastmcp
- httpx
- aiofiles
- A fal.ai API key
- Docker (optional, for containerized deployment)

## Installation

### Local Installation

1. Clone this repository:
```bash
git clone https://github.com/am0y/mcp-fal.git
cd mcp-fal
```

2. Install the required packages:
```bash
pip install fastmcp httpx aiofiles
```

3. Set your fal.ai API key as an environment variable:
```bash
export FAL_KEY="YOUR_FAL_API_KEY_HERE"
```

### Docker Installation

1. Clone this repository:
```bash
git clone https://github.com/am0y/mcp-fal.git
cd mcp-fal
```

2. Build and run using Docker Compose:
```bash
# Set your API key as an environment variable
export FAL_KEY="YOUR_FAL_API_KEY_HERE"

# Start the server
docker-compose up -d
```

3. Alternatively, build and run the Docker container directly:
```bash
# Build the Docker image
docker build -t mcp-fal .

# Run the container
docker run -p 8000:8000 -e FAL_KEY="YOUR_FAL_API_KEY_HERE" mcp-fal
```

## Usage

### Running the Server Locally

You can run the server in development mode with:

```bash
fastmcp dev main.py
```

This will launch the MCP Inspector web interface where you can test the tools interactively.

### Running with Docker

The server will be available at http://localhost:8000 when running with Docker.

To stop the server when using Docker Compose:
```bash
docker-compose down
```

### Installing in Claude Desktop

To use the server with Claude Desktop:

```bash
fastmcp install main.py -e FAL_KEY="YOUR_FAL_API_KEY_HERE"
```

This will make the server available to Claude in the Desktop app.

### Running Directly

You can also run the server directly:

```bash
python main.py
```

## MCP Configuration

```json
"mcp": {
    "servers": {
        "fal-ai": {
            "command": "docker",
            "args": [
                "run",
                "-i",
                "--rm",
                "-e",
                "FAL_KEY=YOUR_FAL_API_KEY_HERE",
                "-p",
                "8000:8000",
                "mcp-fal"
            ]
        }
    }
}
```

## API Reference

### Tools

- `models(page=None, total=None)` - List available models with optional pagination
- `search(keywords)` - Search for models by keywords
- `schema(model_id)` - Get OpenAPI schema for a specific model
- `generate(model, parameters, queue=False)` - Generate content using a model
- `result(url)` - Get result from a queued request
- `status(url)` - Check status of a queued request
- `cancel(url)` - Cancel a queued request
- `upload(path)` - Upload a file to fal.ai CDN

## License

[MIT](LICENSE)