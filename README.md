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
- A fal.ai API key
- Docker (optional, for containerized deployment)

## Quick Start with Docker

1. Clone this repository:
```bash
git clone https://github.com/am0y/mcp-fal.git
cd mcp-fal
```

2. Set your fal.ai API key:
```bash
export FAL_KEY="YOUR_FAL_API_KEY_HERE"
```

3. Build and run with Docker:
```bash
docker compose up -d
```

To stop the server:
```bash
docker compose down
```

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your API key:
```bash
export FAL_KEY="YOUR_FAL_API_KEY_HERE"
```

3. Run the server:
```bash
python main.py
```

## Dockerized MCP Server

The MCP server has been configured to run as a Docker container with stdio transport, making it compatible with MCP clients like VS Code and Claude. This approach simplifies deployment and ensures consistent environment across different systems.

### Building the Docker Image

```bash
# Build the image
docker build -t mcp-fal .
```

### Running the Dockerized Server

```bash
# Run with your fal.ai API key
docker run -i --rm -e FAL_KEY="YOUR_FAL_API_KEY_HERE" mcp-fal
```

The `-i` flag is essential as it keeps stdin open, allowing the MCP server to communicate via stdio.

### Testing the MCP Server

You can test the individual tools by integrating the server with an MCP-compatible client like Claude or VS Code. Some example operations:

- Listing models: `models(page=1, total=5)`
- Getting a model schema: `schema(model_id="fal-ai/llava")`
- Searching for models: `search(keywords="image generation")`

## MCP Configuration

### VS Code Integration

To use this server with VS Code, add this configuration to your VS Code settings.json:

```jsonc
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
                "mcp-fal"
            ]
        }
    }
}
```

### Claude Desktop Integration

For Claude Desktop, you can configure the server like this:

```json
{
    "context7": {
        "command": "docker",
        "args": [
            "run",
            "-i",
            "--rm",
            "-e",
            "FAL_KEY=YOUR_FAL_API_KEY_HERE",
            "mcp-fal"
        ]
    }
}
```

This configuration allows Claude to directly communicate with your fal.ai MCP server through the Docker container.

## API Reference

### Tools

- `models(page=None, total=None)` - List available models with optional pagination
- `search(keywords)` - Search for models by keywords
- `schema(model_id)` - Get OpenAPI schema for a specific model
- `generate(model, parameters, queue=False)` - Generate content using a model
- `result(url)` - Get result from a queued request
- `status(url)` - Check status of a queued request
- `cancel(url)` - Cancel a queued request
- `upload(path)` - Upload a file to fal.ai storage

## License

[MIT](LICENSE)