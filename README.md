# Sub-Par-Powers

A Claude Code plugin with skills for token-efficient requirement gathering, implementation planning, and exact plan execution for Haiku models.

## Installation

### Option 1: From GitHub (recommended)

```bash
# In Claude Code, add this repository as a marketplace
/plugin marketplace add EdwinMurari/sub-par-powers

# Install the plugin
/plugin install sub-par-powers@EdwinMurari
```

### Option 2: Local Development

```bash
# Clone the repository
git clone https://github.com/EdwinMurari/sub-par-powers.git

# Run Claude Code with the plugin
claude --plugin-dir ./sub-par-powers
```

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
