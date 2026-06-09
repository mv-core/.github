#!/usr/bin/env python3
import json
import os
import re
import urllib.request

ORG = 'mv-core'
README_PATH = 'profile/README.md'
TOKEN = os.environ.get('GITHUB_TOKEN', '')

PRIMARY_TOPICS = {'ai-ml', 'ai-agent', 'mcp', 'infra', 'blockchain', 'runtime', 'utils', 'security', 'hardware'}

def get_repos():
    repos = []
    page = 1
    while True:
        req = urllib.request.Request(
            f'https://api.github.com/orgs/{ORG}/repos?per_page=100&page={page}',
            headers={
                'Authorization': f'Bearer {TOKEN}',
                'Accept': 'application/vnd.github+json',
                'X-GitHub-Api-Version': '2022-11-28'
            }
        )
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read())
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def main():
    repos = get_repos()
    
    counts = {
        'ai-ml': 0, 'ai-agent': 0, 'mcp': 0, 'infra': 0, 'blockchain': 0,
        'runtime': 0, 'utils': 0, 'security': 0, 'hardware': 0, 'reference': 0
    }
    
    for repo in repos:
        if repo['name'] == '.github':
            continue
        topics = set(repo.get('topics', []))
        has_primary = bool(topics & PRIMARY_TOPICS)
        
        for topic in topics:
            if topic in PRIMARY_TOPICS:
                counts[topic] += 1
            elif topic == 'reference' and not has_primary:
                counts['reference'] += 1
    
    print('Counts:', counts)
    
    with open(README_PATH, 'r') as f:
        content = f.read()
    
    badge_map = {
        'AI___ML': 'ai-ml',
        'Agents_and_Coding_Tools': 'ai-agent',
        'MCP_Ecosystem': 'mcp',
        'Infra_and_DevOps': 'infra',
        'Blockchain': 'blockchain',
        'Runtimes': 'runtime',
        'Tools_and_Utils': 'utils',
        'Security': 'security',
        'Hardware': 'hardware',
        'Reference_and_Knowledge': 'reference',
    }
    
    modified = False
    for badge, topic in badge_map.items():
        pattern = rf'https://img\.shields\.io/badge/{badge}-(\d+)-'
        replacement = f'https://img.shields.io/badge/{badge}-{counts[topic]}-'
        new_content, n = re.subn(pattern, replacement, content)
        if n > 0:
            content = new_content
            print(f'Updated {badge}: {counts[topic]}')
            modified = True
    
    if modified:
        with open(README_PATH, 'w') as f:
            f.write(content)
        print(f'Wrote {README_PATH}')
    else:
        print('No changes needed')

if __name__ == '__main__':
    main()
