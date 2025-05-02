"""
fal.ai MCP Server : Main entry point
"""

import os
from fastmcp import FastMCP
from api.models import register_model_tools
from api.generate import register_generation_tools
from api.storage import register_storage_tools
from api.config import get_api_key, SERVER_NAME, SERVER_DESCRIPTION, SERVER_VERSION, SERVER_DEPENDENCIES

# Create the FastMCP server instance
app = FastMCP(
    SERVER_NAME,
    description=SERVER_DESCRIPTION,
    dependencies=SERVER_DEPENDENCIES,
    version=SERVER_VERSION
)

# Register all tools
register_model_tools(app)
register_generation_tools(app)
register_storage_tools(app)

if __name__ == "__main__":
    # Ensure API key is set
    get_api_key()
    
    # Run with stdio transport (default)
    app.run()