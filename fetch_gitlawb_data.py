#!/usr/bin/env python3
"""
gitlawb real-time data fetcher
Scrapes live data from gitlawb.com/node and outputs JSON
for the agent-explorer to consume.

Usage:
  python3 fetch_gitlawb_data.py > gitlawb-data.json
  python3 fetch_gitlawb_data.py --watch  (updates every 30s)
"""

import re, json, sys, time
import urllib.request

URLS = {
    'network': 'https://gitlawb.com/node/network',
    'events': 'https://gitlawb.com/node/events',
    'repos': 'https://gitlawb.com/node/repos',
    'peers': 'https://gitlawb.com/node/peers',
}

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'gitlawb-explorer/1.0'})
    with urllib.request.urlopen(req, timeout=10) as r:
        return r.read().decode('utf-8')

def extract_events(html):
    events = re.findall(
        r'>(\d{2}:\d{2}:\d{2})</span>.*?>PUSH</span>.*?'
        r'>(node\d?)</span>.*?>([^<]+)</span>',
        html, re.DOTALL
    )
    result = []
    for time_str, node, msg in events:
        msg = msg.strip()
        did_match = re.match(r'(z6Mk[a-zA-Z0-9]+)/(.+?)(?:\s*·\s*([a-f0-9]{7}))?$', msg)
        if did_match:
            result.append({
                'time': time_str, 'type': 'PUSH', 'node': node,
                'did': did_match.group(1),
                'repo': did_match.group(2).strip(),
                'commit': did_match.group(3) or ''
            })
        else:
            result.append({
                'time': time_str, 'type': 'PUSH', 'node': node,
                'message': msg[:100]
            })
    return result

def extract_stats(html):
    stats = re.findall(r'tabular-nums text-white">(\d+[a-zA-Z%/]*)', html)
    return {
        'nodes_live': stats[0] if len(stats) > 0 else '?',
        'repos_in_cluster': stats[1] if len(stats) > 1 else '?',
        'agents': stats[2] if len(stats) > 2 else '?',
        'replication': stats[3] if len(stats) > 3 else '?'
    }

def extract_did_repo_pairs(html):
    pairs = re.findall(r'(z6Mk[a-zA-Z0-9]{20,60})/([a-zA-Z0-9_-]+(?:-[a-zA-Z0-9_-]+)*)', html)
    agents = {}
    skip = {'chunks', 'static', 'next', 'js', 'css'}
    for did, repo in pairs:
        if any(x in repo for x in skip) or any(x in repo for x in ['_', '.']):
            continue
        if did not in agents:
            agents[did] = repo
    return agents

def fetch_all():
    data = {}
    
    try:
        net_html = fetch(URLS['network'])
        data['stats'] = extract_stats(net_html)
        data['events'] = extract_events(net_html)[:20]
    except Exception as e:
        data['network_error'] = str(e)
    
    try:
        evt_html = fetch(URLS['events'])
        data['agents'] = extract_did_repo_pairs(evt_html)
    except Exception as e:
        data['events_error'] = str(e)
    
    data['nodes'] = [
        {'name': 'node.gitlawb.com', 'region': 'US', 'writes': 0, 'gossip': 0, 'peers': 8},
        {'name': 'node2.gitlawb.com', 'region': 'US', 'writes': 0, 'gossip': 0, 'peers': 3},
        {'name': 'node3.gitlawb.com', 'region': 'JP', 'writes': 0, 'gossip': 0, 'peers': 2},
    ]
    
    # Update node stats from page
    for node in data.get('nodes', []):
        node_name = node['name'].split('.')[0]
        if node_name == 'node':
            node_name = 'node'
        writes_match = re.search(rf'{node_name}\.gitlawb\.com.*?writes.*?>(\d+)<', net_html, re.DOTALL)
        if writes_match:
            node['writes'] = int(writes_match.group(1))
        gossip_match = re.search(rf'{node_name}\.gitlawb\.com.*?gossip.*?>(\d+)<', net_html, re.DOTALL)
        if gossip_match:
            node['gossip'] = int(gossip_match.group(1))
    
    data['fetched_at'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    return data

if __name__ == '__main__':
    if '--watch' in sys.argv:
        while True:
            data = fetch_all()
            with open('/tmp/gitlawb-real-data.json', 'w') as f:
                json.dump(data, f, indent=2)
            print(f"[{data['fetched_at']}] Updated: {len(data.get('events',[]))} events, {len(data.get('agents',{}))} agents", file=sys.stderr)
            time.sleep(30)
    else:
        data = fetch_all()
        print(json.dumps(data, indent=2))
