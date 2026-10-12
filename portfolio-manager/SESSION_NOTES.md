# Session Notes

Running log of work sessions on `portfolio-manager`. Add the newest entry at the top. See `CLAUDE.md` for stable project guidance; this file is for what changed and what is next.

## How to use

At the end of each session, add an entry with the template below. Keep it short and factual. Do not paste contents of `input/*.json`, which holds real financial data.

```markdown
## YYYY-MM-DD: <short title>

**Branch:** <branch name>
**Goal:** <what this session set out to do>

### Done
- ...

### Decisions
- <decision> (why: ...)

### Open questions / blockers
- ...

### Next steps
- [ ] ...

### Files touched
- `path`: what changed
```

---

## 2026-10-11: Add CLAUDE.md and session notes

**Branch:** claude-code-demo
**Goal:** Document the project for Claude Code and start a session log.

### Done
- Added `CLAUDE.md` covering commands, layout, data model, code style and gotchas.
- Created this `SESSION_NOTES.md`.

### Decisions
- Kept `SESSION_NOTES.md` separate from `CLAUDE.md` (why: `CLAUDE.md` holds stable guidance, while this file records history and next steps).

### Open questions / blockers
- `/save` is not atomic, so a failure after `cc` is written can leave a partial update (see Gotchas in `CLAUDE.md`).
- There are no tests. `build_sql` and the validation helpers in `app.py` are good first candidates.
- Several MCP servers from the product-management plugin failed to connect this session (`InvalidHTTPResponse`), and monday needs authentication. They are unrelated to this project.

### Next steps
- [ ] Decide whether to make `/save` atomic (write to temp files, then rename).
- [ ] Add basic tests for `build_sql` and date/key validation.

### Files touched
- `CLAUDE.md`: new
- `SESSION_NOTES.md`: new
