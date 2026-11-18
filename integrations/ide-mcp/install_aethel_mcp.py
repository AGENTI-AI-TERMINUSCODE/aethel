#!/usr/bin/env python3
"""
Aethel Sovereign MCP 1-Click Installer (VS Code / Cursor / Claude Desktop)
Configura automaticamente l'endpoint MCP SSE sovrano: https://aethel.terminuscode.com/mcp/sse
"""
import os
import json
import platform

MCP_ENTRY = {
    "url": "https://aethel.terminuscode.com/mcp/sse",
    "transport": "sse"
}


def patch_config(path: str, label: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = {}
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = {}
    data.setdefault("mcpServers", {})["aethel-sovereign"] = MCP_ENTRY
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✓ Configured Aethel MCP in {label}: {path}")


def main():
    home = os.path.expanduser("~")
    sys_name = platform.system()
    targets = [
        (os.path.join(home, ".cursor", "mcp.json"), "Cursor IDE"),
        (os.path.join(home, ".vscode", "mcp.json"), "VS Code"),
    ]
    if sys_name == "Windows":
        appdata = os.environ.get("APPDATA", home)
        targets.append((os.path.join(appdata, "Claude", "claude_desktop_config.json"), "Claude Desktop"))
    elif sys_name == "Darwin":
        targets.append((os.path.join(home, "Library", "Application Support", "Claude", "claude_desktop_config.json"), "Claude Desktop"))
    else:
        targets.append((os.path.join(home, ".config", "Claude", "claude_desktop_config.json"), "Claude Desktop"))

    for path, label in targets:
        patch_config(path, label)
    print("\n✅ Aethel MCP installed. Restart your IDE to activate `aethel-sovereign`.")


if __name__ == "__main__":
    main()
