---
name: optimizing-prompts
description: Use when auditing existing skills, agents, or CLAUDE.md files - when prompts are verbose, inefficient, or not following token optimization best practices.
---

# Optimizing Prompts and Skills

Audit and optimize skills, agents, and CLAUDE.md files for token efficiency.

## Optimization Techniques

### Structure
- Use XML tags: `<task>`, `<files>`, `<step>`, `<verify>`
- Use YAML frontmatter for metadata
- Use tables for structured comparisons

### Compression
- Remove filler words and phrases
- Replace prose with structured data (YAML/JSON)
- Use 1-2 strong examples, not many weak ones
- Cross-reference instead of duplicating

### Efficiency
- No @ force-load references (consumes context immediately)
- Link to files instead of embedding
- Progressive disclosure: teach how to find info

## Skill Description Rules

Descriptions must:
- Be third-person
- Describe ONLY when to use (triggering conditions)
- Start with "Use when..." or "You MUST use this before..."
- Be under 500 characters
- NEVER summarize the skill's process

## Audit Checklist

<checklist>
- [ ] Word count under 500
- [ ] Description: triggering conditions only
- [ ] Description: starts "Use when..." or "You MUST use..."
- [ ] Description: under 500 characters
- [ ] No @ force-load references
- [ ] No duplicate content across skills
- [ ] Examples minimal but complete
- [ ] XML tags for structure
- [ ] No filler phrases
- [ ] No marketing terms in names
</checklist>

## Banned Terms

In names and descriptions:
- enhanced, optimized, improved, better
- new, v2, advanced, upgraded
- helper, utils (unless truly general)
- manager (unless actually managing resources)

## Report Format

```markdown
## Optimization Report: [File Name]

### Metrics
- Before: [N] tokens / [N] words
- After: [N] tokens / [N] words
- Reduction: [N]%

### Changes Made
1. [Change description]
2. [Change description]

### Remaining Issues
- [Issue or "None"]
```

## Common Optimizations

| Before | After |
|--------|-------|
| "Please note that you should..." | [Delete] |
| "It's important to remember..." | [Delete] |
| "Make sure to always..." | [Direct instruction] |
| Paragraph of explanation | Bullet list |
| Repeated instructions | Cross-reference |
| Multiple similar examples | One strong example |
