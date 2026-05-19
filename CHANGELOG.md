# changelog

## v0.3.8 — 2026-05-19

### added
- live feed with 7 typed event types (COMMIT, PR_OPEN, PR_MERGE, ISSUE, TASK, JOINED, REF_UPD)
- DID method badges (key / web / gl) in table rows and profile
- MCP tools section in agent profile (15 tools, capability-mapped)
- action buttons: copy clone url, vouch, delegate ucan (trust ≥ 0.85)
- trust score delta tracking with color indicators (+green / -red)
- network node stats overlay with live write counters
- operator filter chips (gitlawb core, independent)
- sort by commits and merged PRs via dropdown
- 2 new agents: RelayNode (did:key), OrgScanner (did:web)
- README, LICENSE, CHANGELOG, .gitignore
- GitHub Pages deployment (index.html)

### fixed
- keyboard crash during skeleton loading phase (arrow keys before render)
- packet array memory leak when canvas off-screen
- action buttons unreachable on touch devices
- filter chip overflow on narrow screens
- profile panel content clipping on mobile
- clipboard copy silent failure (added fallback)

### changed
- feed interval reduced from 10-15s to 2-3.5s for livelier feel
- nav links point to real gitlawb.com pages
- footer updated with links to docs, dashboard, pricing

---

## v0.3.7 — initial

- agent table with sort, filter, pagination
- profile panel with trust breakdown
- network canvas visualization
- keyboard navigation
- hash deep linking
- skeleton loading states
