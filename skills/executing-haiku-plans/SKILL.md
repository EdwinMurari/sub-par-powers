---
name: executing-haiku-plans
description: Use when you have a written implementation plan to execute - when plan exists and is approved, execution must be verbatim with no additions, no interpretation, stopping on any ambiguity.
---

# Executing Implementation Plans

Execute plans exactly as written. Nothing more, nothing less.

## Before Executing

1. **Load plan file** — read entire plan
2. **Review critically** — identify any concerns
3. **If concerns** — STOP and ask before starting
4. **If clear** — proceed with execution

## Execution Rules

<rules>
1. Execute VERBATIM — nothing more than plan says
2. No additions — no helpful improvements
3. No extra logging — unless plan specifies
4. No interpretation — if unclear, STOP and ask
5. Clean as you go — delete old code in same task
6. Verify each task — run verification before next
7. Report blockers — immediately when found
</rules>

## Forbidden Actions

- Adding code not in plan
- Adding comments not in plan
- Adding logging not in plan
- Refactoring beyond plan scope
- "Improving" the plan while executing
- Skipping verification steps

## Stop Conditions

STOP immediately and report when:

- Instruction is ambiguous
- File doesn't exist at specified path
- Code doesn't match plan description
- Verification command fails
- Conflict with existing code

## Batch Execution

Default: 3 tasks per batch, then checkpoint.

For each task:
1. Mark as in_progress
2. Execute each step exactly
3. Run verification command
4. Mark as completed
5. Report status

## Status Report Format

```markdown
## Batch Complete: Tasks N-M

<completed>
- Task N: [name] ✓
- Task M: [name] ✓
</completed>

<verification>
- [Command]: [Result]
</verification>

<issues>
- [None or list issues]
</issues>

<next>
- Ready for next batch / Blocked on [issue]
</next>
```

## Next Step

After execution complete:

```
REQUIRED SUB-SKILL: reviewing-implementation
```
