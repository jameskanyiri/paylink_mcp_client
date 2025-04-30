from mcp import ClientSession
import asyncio
import nest_asyncio
from mcp.client.sse import sse_client
from dotenv import load_dotenv
import os

load_dotenv(override=True)

url = os.getenv('SERVER_URL')

nest_asyncio.apply()

     
async def main():
     # Connect to the server using SSE
    async with sse_client(url=url) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            
            print(tools)
            
            return tools
            

if __name__ == "__main__":
    asyncio.run(main())