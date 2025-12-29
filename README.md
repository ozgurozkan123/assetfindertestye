# Assetfinder MCP (Render)

This is a FastMCP server that wraps **assetfinder** (tomnomnom) and exposes it over MCP via SSE on `/mcp`.

## Tool
- `do_assetfinder(target: str, subs_only: bool = True)`
  - Finds related domains/subdomains for the given root domain using `assetfinder`.

## Running locally
```bash
docker build -t assetfinder-mcp .
docker run -p 8000:8000 assetfinder-mcp
```
The MCP endpoint will be at `http://localhost:8000/mcp` (SSE transport).

## Deployment notes
- Binds to `0.0.0.0` and uses `PORT` environment variable (Render/Railway set this automatically).
- Dockerfile installs `assetfinder` via `go install github.com/tomnomnom/assetfinder@latest`.
