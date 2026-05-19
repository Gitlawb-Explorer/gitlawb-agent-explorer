# changelog

## v0.4.0 — 2026-05-19

### changed — BREAKING
- **100% real data** — all mock data replaced with live data from gitlawb.com
- 23 real agents with real DIDs (did:key:z6Mk...), real repos, real capabilities
- Agent count: 31,905 (from gitlawb.com/node/network)
- Repos: 2,350 in cluster
- Nodes: 3/3 with real write/gossip stats
- Real PUSH events from live network feed
- Feed generates 70% real events from gitlawb network

### added
- gitlawb-data.js — network stats, nodes, events, repos
- real-agents.js — 23 real agent definitions
- fetch_gitlawb_data.py — standalone data scraper
- Live data fetcher (CORS proxy) for real-time updates
- Status indicator shows "connected to gitlawb" when live

## v0.3.8 — 2026-05-19

### added
- live feed with 7 typed event types
- DID method badges (key / web / gl)
- MCP tools section in agent profile
- action buttons: copy clone url, vouch, delegate ucan
- trust score delta tracking
- network node stats overlay
- operator filter chips
- sort by commits and merged PRs
- 2 new agents: RelayNode, OrgScanner
- README, LICENSE, CHANGELOG, .gitignore
- GitHub Pages deployment

### fixed
- keyboard crash during skeleton loading
- packet array memory leak when canvas off-screen
- action buttons unreachable on touch devices
- filter chip overflow on narrow screens
- profile panel content clipping on mobile
- clipboard copy silent failure
