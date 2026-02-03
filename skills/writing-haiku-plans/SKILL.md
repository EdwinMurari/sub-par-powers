---
name: writing-haiku-plans
description: Use when requirements are gathered and approved, before touching code - when you need an exact implementation plan for Haiku models to execute verbatim with no interpretation.
---

# Writing Implementation Plans for Haiku

Create exact, bite-sized implementation plans that Haiku can execute verbatim.

## Before Writing

1. **Quick explore first** — use Haiku agent to check existing code
2. **Identify files** — exact paths with line ranges
3. **Check for existing solutions** — don't duplicate

## Plan Header

```yaml
---
goal: [One sentence]
approach: [2-3 sentences max]
files_to_modify:
  - path/file.ext:L10-50
files_to_delete:
  - path/old.ext
files_to_create:
  - path/new.ext
---
```

## Task Format

Each task: 2-5 minutes, single action focus.

```markdown
### Task N: [Descriptive Name]

<files>
MODIFY: `path/file.ext:L10-50`
DELETE: `path/old.ext`
CREATE: `path/new.ext`
</files>

<step n="1">
[Exact action with complete code]
</step>

<step n="2">
[Next exact action]
</step>

<verify>
Command: `[exact command]`
Expected: `[exact expected output]`
</verify>
```

## Core Rules

1. **Complete code blocks** — no placeholders, no "..."
2. **Exact file paths** — with line ranges when modifying
3. **Bite-sized tasks** — 2-5 minutes each
4. **One action per step** — atomic operations
5. **Delete old immediately** — in same task as adding new
6. **No editorial comments** — no TODO, FIXME, HACK
7. **Verification commands** — with expected output

## Clean Refactor Rules

- Never two implementations of same thing
- No fallbacks or "just in case" logic
- No migration strategies
- No backwards compatibility shims
- Delete unused code immediately
- No commented-out code

## Naming Rules

- Descriptive names only, no marketing terms
- No: enhanced, optimized, improved, better, v2, advanced
- Names explain WHAT code does

## Plan Storage

Save to: `docs/plans/YYYY-MM-DD-<name>.md`

## Next Step

After plan written:

```
REQUIRED SUB-SKILL: executing-haiku-plans
```
