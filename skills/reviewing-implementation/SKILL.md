---
name: reviewing-implementation
description: Use after plan execution to verify work matches plan exactly - when implementation claims to be complete and you need to confirm nothing extra was added and nothing was missed.
---

# Reviewing Implementation Against Plan

Verify implementation matches plan exactly. Catch gaps and extras.

## Before Reviewing

1. **Load original plan** — the approved plan file
2. **Load implementation** — current state of modified files
3. **Prepare checklist** — one per task

## Review Process

For each task in plan:

### 1. Check Specified Changes

<specified>
- [ ] All files in `<files>` modified/created/deleted?
- [ ] Each `<step>` executed exactly?
- [ ] Code matches plan verbatim?
- [ ] Verification command passes?
</specified>

### 2. Check for Extras

<extras>
- [ ] No unplanned files modified?
- [ ] No extra code added?
- [ ] No extra logging?
- [ ] No extra comments?
- [ ] No extra imports?
- [ ] No "helpful improvements"?
</extras>

### 3. Check for Gaps

<gaps>
- [ ] All steps completed?
- [ ] All files accounted for?
- [ ] All deletions performed?
- [ ] All verifications run?
</gaps>

## Review Report Format

```markdown
## Implementation Review: [Plan Name]

### Summary
- Status: PASS | GAPS | EXTRAS | FAIL
- Tasks reviewed: N
- Issues found: N

### Task-by-Task

#### Task 1: [Name]
- Specified: ✓ All correct
- Extras: ✓ None found
- Gaps: ✓ None found

#### Task 2: [Name]
- Specified: ✓ All correct
- Extras: ⚠ Added logging at line 42
- Gaps: ✓ None found

### Issues

<gaps>
- [List missing implementations]
</gaps>

<extras>
- [List unplanned additions]
</extras>

### Verdict
- PASS: Proceed to merge/deploy
- GAPS: Execute missing items
- EXTRAS: Remove unplanned additions
- FAIL: Re-execute from plan
```

## Severity Levels

| Level | Description | Action |
|-------|-------------|--------|
| PASS | Exact match | Proceed |
| GAPS | Missing items | Execute missing |
| EXTRAS | Added items | Remove additions |
| FAIL | Major deviations | Re-execute |

## No Tolerance Policy

- Extra comments = EXTRAS
- Extra logging = EXTRAS  
- Extra error handling = EXTRAS
- Missing deletion = GAPS
- Partial implementation = GAPS
