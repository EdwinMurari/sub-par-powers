# Recommended CLAUDE.md / GEMINI.md Rules

Copy these rules to your memory file for always-on enforcement.

**Claude Code:** `~/.claude/CLAUDE.md` or `<project>/CLAUDE.md`
**Antigravity:** `~/.gemini/GEMINI.md` or `<project>/GEMINI.md`

---

```markdown
# Code Quality Standards

## Architecture
- Respect existing architecture; extend, don't replace without reason
- SOLID principles required for OOP code
- DRY: extract common patterns, no duplication
- Check for existing solutions before writing new code
- Use quick explore agents (Haiku) before implementing

## Naming Conventions
- Names must be strictly descriptive, not marketing terms
- No: enhanced, optimized, improved, better, new, v2, advanced
- Yes: descriptive names that explain what code does
- Comments only when name cannot convey meaning

## Clean Code
- No quick solutions or workarounds
- No brittle solutions
- No fallbacks or migration strategies
- No backwards compatibility shims
- No dead code, unused imports, commented-out code
- No editorial comments: TODO, FIXME, HACK, XXX, NOTE

## Tool Efficiency
- Targeted searches only, no broad searches (bloats context)
- Don't load entire files when ranges suffice
- Use @imports sparingly (force-loads consume context)

## Verification
- Never claim success without running verification command
- Evidence before assertions, always
- No "should work" or "probably passes"

---

# Prompt Optimization Rules

## Structure
- Use XML tags for sections: `<task>`, `<files>`, `<step>`, `<verify>`
- Use YAML/JSON for structured data instead of prose
- Use tables for comparisons

## Token Compression
- Remove filler: "please note that", "it's important to", "make sure to"
- One strong example beats many weak ones
- Cross-reference with `REQUIRED SUB-SKILL:` instead of duplicating
- Progressive disclosure: teach how to find info, don't embed all

## Latency Optimization
- Skeleton-of-Thought: outline first, expand in parallel

## Context Management
- Link to files instead of force-loading (@)
- Check context before reading: "Have I already read this file?"
- If already read in this session, use that — don't re-read
- Read only needed sections (use offset+limit for partial reads)

## Anti-Hallucination
- NEVER assume file contents not explicitly read
- NEVER fabricate function signatures, APIs, or behaviors
- When making claims about code, cite: `[source: file.py#L45-80]`
- Before answering from memory, verify: "Did I read this in context?"
```

