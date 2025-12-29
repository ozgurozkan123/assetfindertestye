import os
import subprocess
from fastmcp import FastMCP

mcp = FastMCP("assetfinder-mcp")

@mcp.tool()
def do_assetfinder(target: str, subs_only: bool = True) -> str:
    """Find related domains and subdomains using assetfinder for a given target.

    Args:
        target: The root domain (e.g., example.com) to discover associated subdomains and related domains.
        subs_only: If True, only return subdomains (default: True)
    Returns:
        Collected domains/subdomains as newline-separated text.
    """
    args = ["assetfinder"]
    if subs_only:
        args.append("--subs-only")
    args.append(target)

    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "assetfinder failed")
    output = result.stdout.strip()
    return output or "No domains found."

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    mcp.run(
        transport="sse",
        host=host,
        port=port,
        path="/mcp",
    )
