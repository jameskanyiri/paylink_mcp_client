"""
Tests for the PayLink MCP Client.
"""
import pytest
from unittest.mock import AsyncMock, patch

from paylink_mcp_client import PayLinkMCPClient, list_tools


class AsyncContextManagerMock:
    """Mock for async context managers."""
    def __init__(self, return_value):
        self.return_value = return_value
        
    async def __aenter__(self):
        return self.return_value
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


@pytest.mark.asyncio
async def test_client_init():
    """Test client initialization."""
    # Test with default URL
    client = PayLinkMCPClient()
    assert client.url == "http://paylink-app.eastus.azurecontainer.io:8050/sse"


@pytest.mark.asyncio
async def test_list_tools():
    """Test listing tools."""
    # Create mock return values
    mock_read_stream = AsyncMock()
    mock_write_stream = AsyncMock()
    mock_session = AsyncMock()
    mock_session.initialize = AsyncMock()
    mock_session.list_tools = AsyncMock(return_value=["tool1", "tool2"])
    
    # Set up context manager mocks
    mock_sse_client = AsyncContextManagerMock((mock_read_stream, mock_write_stream))
    mock_client_session = AsyncContextManagerMock(mock_session)
    
    # Patch both context managers
    with patch("paylink_mcp_client.client.sse_client", return_value=mock_sse_client), \
         patch("paylink_mcp_client.client.ClientSession", return_value=mock_client_session):
        
        client = PayLinkMCPClient()
        tools = await client.list_tools()
        
        # Check that initialize and list_tools were called
        mock_session.initialize.assert_called_once()
        mock_session.list_tools.assert_called_once()
        
        # Check the returned tools
        assert tools == ["tool1", "tool2"]



@pytest.mark.asyncio
async def test_convenience_functions():
    """Test the convenience functions."""
    # Create a mock client
    mock_client = AsyncMock()
    mock_client.list_tools = AsyncMock(return_value=["tool1", "tool2"])
    mock_client.execute_tool = AsyncMock(return_value={"result": "success"})
    
    # Patch the client class
    with patch("paylink_mcp_client.client.PayLinkMCPClient", return_value=mock_client):
        # Test list_tools convenience function
        tools = await list_tools()
        assert tools == ["tool1", "tool2"]
        