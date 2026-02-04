#!/usr/bin/env python3
"""
PreToolUse hook: Checks cache before reading files/URLs.
Provides additionalContext with cached sections and line ranges.
Validates cache freshness via file mtime and web TTL.
"""
import sys
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

try:
    import yaml
except ImportError:
    print(json.dumps({}))
    sys.exit(0)

def check_file_freshness(file_path: str, cached_mtime: str) -> bool:
    """Returns True if cache is fresh (file unchanged since cache)."""
    try:
        actual_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
        cached_dt = datetime.fromisoformat(cached_mtime)
        return actual_mtime <= cached_dt
    except (OSError, ValueError):
        return False

def check_web_freshness(fetch_date: str, ttl_days: int = 7) -> bool:
    """Returns True if web cache is fresh (within TTL)."""
    try:
        fetched = datetime.fromisoformat(fetch_date)
        return datetime.now() - fetched < timedelta(days=ttl_days)
    except ValueError:
        return False

def output_context(context: str):
    """Output additionalContext to Claude."""
    print(json.dumps({
        'hookSpecificOutput': {
            'hookEventName': 'PreToolUse',
            'additionalContext': context
        }
    }))

def main():
    try:
        INPUT = json.load(sys.stdin)
    except json.JSONDecodeError:
        print(json.dumps({}))
        sys.exit(0)
    
    TOOL = INPUT.get('tool_name')
    cwd = Path(INPUT.get('cwd', '.'))
    
    if TOOL == 'Read':
        check_file_cache(INPUT, cwd)
    elif TOOL == 'WebFetch':
        check_web_cache(INPUT)
    else:
        print(json.dumps({}))

def check_file_cache(input_data: dict, cwd: Path):
    """Check if file is in cache and still fresh."""
    file_path = input_data['tool_input']['file_path']
    cache_path = cwd / '.claude/cache/session-cache.yaml'
    
    if not cache_path.exists():
        print(json.dumps({}))
        return
    
    data = yaml.safe_load(cache_path.read_text()) or {}
    entry = data.get('files_read', {}).get(file_path)
    
    if not entry:
        print(json.dumps({}))
        return
    
    cached_mtime = entry.get('file_mtime', '')
    
    if check_file_freshness(file_path, cached_mtime):
        # Cache is valid
        sections = entry.get('sections', {})
        section_info = '; '.join([
            f"{k}: L{v.get('lines', '?')} ({v.get('summary', 'no summary')[:30]})"
            for k, v in sections.items()
        ])
        context = f"""CACHE VALID: {file_path}
Sections: {section_info}
Use line ranges for targeted reads (e.g., offset=45, limit=35 for L45-80)."""
        output_context(context)
    else:
        # Cache stale - file was modified
        output_context(f"CACHE STALE: {file_path} was modified since last read. Re-reading and updating cache.")
        # Invalidate entry
        del data['files_read'][file_path]
        cache_path.write_text(yaml.dump(data, default_flow_style=False, sort_keys=False))

def check_web_cache(input_data: dict):
    """Check if URL is in global cache and still fresh."""
    url = input_data['tool_input'].get('url', '')
    global_cache_path = Path.home() / '.claude/cache/global-cache.yaml'
    
    if not global_cache_path.exists():
        print(json.dumps({}))
        return
    
    gc = yaml.safe_load(global_cache_path.read_text()) or {}
    
    for key, entry in gc.get('research', {}).items():
        if entry.get('original_url') == url:
            ttl = entry.get('ttl_days', 7)
            fetch_date = entry.get('fetch_date', '')
            
            if check_web_freshness(fetch_date, ttl):
                source = entry.get('source', '')
                sections = entry.get('sections', {})
                section_info = '; '.join([
                    f"{k}: L{v.get('lines', '?')}"
                    for k, v in sections.items()
                ]) or "No sections labeled yet"
                
                context = f"""CACHED: Read from ~/.claude/cache/{source} instead.
Sections: {section_info}
Avoid re-fetching - use local file."""
                output_context(context)
                return
            else:
                output_context(f"CACHE EXPIRED: {url} (>{ttl} days old). Re-fetching.")
                return
    
    print(json.dumps({}))

if __name__ == '__main__':
    main()
