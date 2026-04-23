#!/usr/bin/env python3
"""
Offensive Tool Documentation Generator (Zero-Dependency Version)
Maintains a markdown knowledge base of Kali/Parrot tools.
"""

import urllib.request
import re
from pathlib import Path

# Target directory for the markdown files
OUTPUT_DIR = Path("kb/tools")

def get_tool_list():
    """Fetches the tool index from Kali's official documentation."""
    print("[*] Connecting to Kali Tool Directory...")
    url = "https://www.kali.org/tools/"
    try:
        # Standard library request (no 'requests' module needed)
        with urllib.request.urlopen(url, timeout=10) as response:
            html = response.read().decode('utf-8')
            # Extract tool paths and names using regex
            matches = re.findall(r'href="(/tools/[^"]+/)">([^<]+)</a>', html)
            return {name.strip(): "https://www.kali.org" + path for path, name in matches}
    except Exception as e:
        print(f"[!] Network error: {e}")
        return {}

def get_tool_details(url):
    """Parses tool pages for descriptions and code examples."""
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            html = response.read().decode('utf-8')
            
            # Find first paragraph for description, strip HTML tags
            desc_match = re.search(r'<p>(.*?)</p>', html, re.DOTALL)
            desc = re.sub(r'<[^>]+>', '', desc_match.group(1)).strip() if desc_match else "No description."

            # Find text within code blocks for examples
            example_matches = re.findall(r'<code>(.*?)</code>', html, re.DOTALL)
            # Filter for blocks that look like commands (usually 5+ chars)
            examples = [ex.strip() for ex in example_matches if len(ex) > 5]
            
            return {
                "description": desc,
                "examples": "\n".join(examples[:3]) if examples else "Manual examples needed."
            }
    except:
        return {"description": "Metadata fetch failed.", "examples": "N/A"}

def update_markdown(tool_name, details):
    """
    Intelligently updates only the '# auto summary' section.
    Preserves all other content in the file.
    """
    file_path = OUTPUT_DIR / f"{tool_name}.md"
    
    # The 'Auto Summary' Block
    new_summary = [
        "# auto summary",
        f"**Tool:** `{tool_name}`",
        "",
        "### Description",
        details['description'],
        "",
        "### Usage Examples",
        "```bash",
        details['examples'],
        "```",
        "" # Trailing newline
    ]
    
    if file_path.exists():
        existing_lines = file_path.read_text().splitlines()
        final_lines = []
        is_skipping = False
        replaced = False

        for line in existing_lines:
            # Detect start of our block
            if line.strip().lower() == "# auto summary":
                is_skipping = True
                final_lines.extend(new_summary)
                replaced = True
                continue
            
            # Detect end of our block (the next H1)
            if is_skipping and line.startswith("# "):
                is_skipping = False
            
            # Keep lines that aren't part of the old auto-summary
            if not is_skipping:
                final_lines.append(line)
        
        # If the file exists but has no auto-summary, prepend it
        if not replaced:
            final_lines = new_summary + ["---", ""] + final_lines
            
        content = "\n".join(final_lines)
    else:
        content = "\n".join(new_summary)

    file_path.write_text(content)

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    tools = get_tool_list()
    
    if not tools:
        print("[-] No tools found. Check internet connection.")
        return

    # To process every single tool (hundreds), remove '[:15]'
    # We limit to 15 for a fast, successful demonstration
    target_tools = list(tools.items())[:15]
    print(f"[*] Generating/Updating {len(target_tools)} tool files...")

    for name, url in target_tools:
        print(f" [+] Processing: {name}")
        details = get_tool_details(url)
        update_markdown(name, details)

    print(f"\n[*] Success! Documentation stored in '{OUTPUT_DIR}/'")

if __name__ == "__main__":
    main()