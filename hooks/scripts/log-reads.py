#!/usr/bin/env python3
"""
PostToolUse hook: Logs file reads and web fetches to session cache.
Triggered after Read/WebFetch tools complete.
"""
import sys
import json
import os
from datetime import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    # PyYAML not installed - fail silently
    sys.exit(0)

def main():
    try:
        INPUT = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)
    
    TOOL = INPUT.get('tool_name')
    cwd = Path(INPUT.get('cwd', '.'))
    
    if TOOL == 'Read':
        log_file_read(INPUT, cwd)
    elif TOOL == 'WebFetch':
        log_web_fetch(INPUT)

def log_file_read(input_data: dict, cwd: Path):
    """Log file read to project cache with mtime and line range."""
    cache_path = cwd / '.claude/cache/session-cache.yaml'
    file_path = input_data['tool_input']['file_path']
    offset = input_data['tool_input'].get('offset', 0)
    limit = input_data['tool_input'].get('limit', 'all')
    
    # Load or create cache
    cache = {'files_read': {}, 'decisions': [], 'lookups': {}, 'key_locations': {}}
    if cache_path.exists():
        cache = yaml.safe_load(cache_path.read_text()) or cache
    
    # Get file modification time
    try:
        file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
    except OSError:
        file_mtime = datetime.now().isoformat()
    
    # Create or update entry
    entry = cache['files_read'].setdefault(file_path, {
        'summary': '',
        'file_mtime': file_mtime,
        'sections': {},
        'last_read': ''
    })
    
    # Update mtime and last_read
    entry['file_mtime'] = file_mtime
    entry['last_read'] = datetime.now().isoformat()
    
    # Add section for this read
    if limit != 'all' and isinstance(limit, int):
        section_id = f"L{offset}-{offset + limit}"
    else:
        section_id = "full"
    
    entry['sections'][section_id] = {
        'lines': section_id,
        'summary': ''  # Claude fills this manually or via CLAUDE.md rules
    }
    
    # Write cache
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(yaml.dump(cache, default_flow_style=False, sort_keys=False))

def log_web_fetch(input_data: dict):
    """Log web fetch to global cache and save content to fetched folder."""
    url = input_data['tool_input'].get('url', '')
    content = input_data.get('tool_response', {}).get('content', '')
    
    if not url:
        return
    
    # Save content to fetched folder
    fetched_dir = Path.home() / '.claude/cache/fetched'
    fetched_dir.mkdir(parents=True, exist_ok=True)
    
    # Create safe filename from URL
    safe_name = url.replace('https://', '').replace('http://', '')
    safe_name = ''.join(c if c.isalnum() or c in '._-' else '_' for c in safe_name)
    safe_name = safe_name[:80] + '.md'
    
    (fetched_dir / safe_name).write_text(content or f"# Fetched from {url}\n\nContent not captured.")
    
    # Update global cache
    global_cache_path = Path.home() / '.claude/cache/global-cache.yaml'
    gc = {'research': {}}
    if global_cache_path.exists():
        gc = yaml.safe_load(global_cache_path.read_text()) or gc
    
    # Use URL domain + path as key
    key = safe_name.replace('.md', '').replace('_', ' ')[:40]
    gc['research'][key] = {
        'description': '',  # User fills this
        'sections': {},
        'source': f"fetched/{safe_name}",
        'original_url': url,
        'fetch_date': datetime.now().isoformat(),
        'ttl_days': 7
    }
    
    global_cache_path.parent.mkdir(parents=True, exist_ok=True)
    global_cache_path.write_text(yaml.dump(gc, default_flow_style=False, sort_keys=False))

if __name__ == '__main__':
    main()
