# Sub-Par-Powers

A plugin with skills for token-efficient requirement gathering, implementation planning, and exact plan execution for Haiku models.

## Installation

### Universal (via skills.sh) - Works with 35+ agents

```bash
# Install to specific agent
npx skills add EdwinMurari/sub-par-powers --agent claude-code
npx skills add EdwinMurari/sub-par-powers --agent antigravity
npx skills add EdwinMurari/sub-par-powers --agent cursor

# Install to all detected agents
npx skills add EdwinMurari/sub-par-powers --agent '*'

# Install globally (available in all projects)
npx skills add EdwinMurari/sub-par-powers --agent claude-code -g
```

### Claude Code Plugin (alternative)

```bash
# Add as plugin marketplace
/plugin marketplace add EdwinMurari/sub-par-powers
```

### Local Development

```bash
git clone https://github.com/EdwinMurari/sub-par-powers.git
claude --plugin-dir ./sub-par-powers
```

### Memory File (Optional)

For always-on code quality rules, copy content from [`docs/recommended-memory-rules.md`](docs/recommended-memory-rules.md) to:
- **Claude Code:** `~/.claude/CLAUDE.md`
- **Antigravity:** `GEMINI.md` in project root

## Skills

| Skill | Description | Invoke |
|-------|-------------|--------|
| `requirement-gathering` | Socratic interview to clarify requirements | `/sub-par-powers:requirement-gathering` |
| `writing-haiku-plans` | Create exact implementation plans for Haiku | `/sub-par-powers:writing-haiku-plans` |
| `executing-haiku-plans` | Execute plans verbatim with no additions | `/sub-par-powers:executing-haiku-plans` |
| `reviewing-implementation` | Verify implementation matches plan exactly | `/sub-par-powers:reviewing-implementation` |
| `optimizing-prompts` | Audit prompts for token efficiency | `/sub-par-powers:optimizing-prompts` |

## Workflow

```
┌─────────────────────────┐
│ 1. requirement-gathering│  ← Socratic interview
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ 2. writing-haiku-plans  │  ← Create exact plan
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ 3. executing-haiku-plans│  ← Execute verbatim (Haiku session)
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ 4. reviewing-implementation│  ← Verify exact match
└─────────────────────────┘
```

## Core Principles

1. **Token Efficiency** — Short, structured prompts; no filler
2. **Exact Execution** — Haiku executes plans verbatim, no additions
3. **Clean Code** — No workarounds, no TODO/FIXME, no dead code
4. **Verification** — Every task has verification; every execution reviewed

## Plan Storage

Implementation plans are saved to:

```
docs/plans/YYYY-MM-DD-<name>.md
```

## Compatibility

- Claude Code version 1.0.33 or later
- Designed for Haiku model execution in separate sessions

## License

MIT
