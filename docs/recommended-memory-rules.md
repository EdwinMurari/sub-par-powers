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
```
