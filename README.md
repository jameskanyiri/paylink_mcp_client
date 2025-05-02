# PayLink python client

## Overview
PayLink is an open-source framework designed to simplify payment integrations for AI agents by leveraging the Model Context Protocol (MCP). It provides a standardized interface for various payment providers, including M-Pesa and Airtel enabling seamless and rapid integration of payment functionalities into your AI agents.


## Features

- **List Available Tools**: Retrieve a list of available tools for payment operations, such as initiating STK Push.

## Installation

Install the PayLink python Client using uv:

```bash
uv add paylink-mcp-client
```

## Requirements

- Python 3.12 or higher

## Usage

The PayLink python Client provides an asynchronous interface to list available tools and supports both direct client instantiation and convenience functions. Below are examples demonstrating how to use the client to list tools.

### Basic Usage

Create a client instance to list available tools from the PayLink MCP API.

```python
import asyncio
from paylink_mcp_client import PayLinkMCPClient

async def main():
    # Initialize the client
    client = PayLinkMCPClient()
    
    # List available tools
    tools = await client.list_tools()
    print(tools)

if __name__ == "__main__":
    asyncio.run(main())
```


### Using Convenience Functions

Use the convenience function to list tools without manually instantiating the client.

```python
import asyncio
from paylink_mcp_client import list_tools

async def main():
    # List tools using the convenience function
    tools = await list_tools()
    print(tools)

if __name__ == "__main__":
    asyncio.run(main())
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Inspired by the need for seamless M-Pesa payment integrations for AI agents and businesses in Kenya.