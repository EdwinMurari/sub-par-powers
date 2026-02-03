---
name: requirement-gathering
description: You MUST use this before any planning or implementation work - when user has a feature idea, bug report, change request, or vague requirement that needs clarification before writing code.
---

# Gathering Requirements

Conduct a Socratic interview to clarify requirements before planning or implementation.

## Core Rules

1. **One question per turn** — wait for answer before next question
2. **Prefer multiple choice** — 2-4 options when possible
3. **Never assume** — if unclear, ask
4. **No preamble** — skip greetings, get to the question
5. **Short questions** — token-efficient, direct

## Interview Flow

Ask in this order, skip what's already clear:

1. **What needs to change?**
   - Current behavior vs desired behavior
   - Specific pain point or goal

2. **Constraints?**
   - Technology, architecture, or compatibility limits
   - Performance requirements
   - Time or scope constraints

3. **Success criteria?**
   - How will we know it works?
   - What should the output look like?

4. **What should NOT happen?**
   - Edge cases to avoid
   - Behaviors to prevent

5. **Existing solutions?**
   - Similar code in the project?
   - Patterns to follow or avoid?

## Output Format

When interview complete, produce:

```yaml
---
goal: [One sentence]
current_state: [Brief description]
desired_state: [Brief description]
constraints:
  - [Constraint 1]
  - [Constraint 2]
success_criteria:
  - [Criterion 1]
  - [Criterion 2]
anti_requirements:
  - [What should NOT happen]
existing_patterns: [Relevant code/patterns to follow]
---
```

## Stop Conditions

- User says "that's enough" or similar
- All 5 areas covered
- User provides complete spec upfront

## Next Step

After requirements gathered:

```
REQUIRED SUB-SKILL: writing-haiku-plans
```
