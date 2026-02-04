# Sub-Par-Powers

A plugin for token-efficient development: skills for requirement gathering, implementation planning, and session caching with automatic cache invalidation.

## Install

### Claude Code Plugin

```bash
# Step 1: Add the marketplace
/plugin marketplace add EdwinMurari/sub-par-powers

# Step 2: Install the plugin
/plugin install session-cache@sub-par-powers
```

### Universal (via skills.sh) - Skills only, no hooks

```bash
npx skills add EdwinMurari/sub-par-powers --agent claude-code
npx skills add EdwinMurari/sub-par-powers --agent opencode
npx skills add EdwinMurari/sub-par-powers --agent '*'  # all agents
```

> **Limitation:** skills.sh only installs the skill files (markdown instructions). Session cache hooks are not installed — cache behavior relies on LLM following the rules in skills, which is less reliable than hooks.

### Local Development

```bash
git clone https://github.com/EdwinMurari/sub-par-powers.git
claude --plugin-dir ./sub-par-powers
```

**Requires:** `pip install pyyaml` (for hooks)

## Features

### Skills

| Skill | Description |
|-------|-------------|
| `requirement-gathering` | Socratic interview to clarify requirements |
| `writing-haiku-plans` | Create exact implementation plans for Haiku |
| `executing-haiku-plans` | Execute plans verbatim with no additions |
| `reviewing-implementation` | Verify implementation matches plan exactly |
| `optimizing-prompts` | Audit prompts for token efficiency |

### Session Cache (Hooks)

Automatic hooks prevent redundant file reads and save web fetches:

| Hook | Trigger | Action |
|------|---------|--------|
| `context-check.py` | Before Read/WebFetch | Checks cache freshness, provides line ranges |
| `log-reads.py` | After Read/WebFetch | Logs file mtime + sections to cache |

**Cache invalidation:**
- Files: Invalidates when file modified (mtime check)
- Web: Expires after TTL (default 7 days)

## Workflow

```
requirement-gathering → writing-haiku-plans → executing-haiku-plans → reviewing-implementation
```

## Structure

```
sub-par-powers/
├── .claude-plugin/plugin.json   # Plugin manifest
├── hooks/
│   ├── hooks.json               # Hook definitions
│   └── scripts/                 # Python hook scripts
├── skills/                      # Skill definitions
└── docs/                        # Memory rules, plans
```

## Memory Rules (Optional)

Copy [`docs/recommended-memory-rules.md`](docs/recommended-memory-rules.md) to:
- `~/.claude/CLAUDE.md` (Claude Code)
- `GEMINI.md` (Antigravity)