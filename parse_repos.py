import re
import os

filepath = r"C:\Users\User\.gemini\antigravity\brain\649fa217-c1a4-47fb-8ca5-80b48b15bf7e\.system_generated\steps\557\content.md"

with open(filepath, encoding='utf-8') as f:
    text = f.read()

repos = re.findall(r'href="/FilipeVicenteH/([^"?#/]+)"', text)
unique_repos = sorted(list(set(repos)))
print("Repositories found:")
for r in unique_repos:
    if r not in ['stargazers', 'followers', 'following']:
        print("-", r)
