import glob
import os
import re

steps_dir = r"C:\Users\User\.gemini\antigravity\brain\649fa217-c1a4-47fb-8ca5-80b48b15bf7e\.system_generated\steps"

for path in glob.glob(os.path.join(steps_dir, "*", "content.md")):
    with open(path, encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    title_match = re.search(r'Source:\s*(\S+)', text)
    if title_match:
        url = title_match.group(1)
        print("=== URL:", url)
        # Find readme text or main elements
        readme_match = re.search(r'<article[^>]*>(.*?)</article>', text, re.DOTALL)
        if readme_match:
            # strip html tags roughly
            clean_readme = re.sub(r'<[^>]+>', '', readme_match.group(1)).strip()
            print("README Snippet:", clean_readme[:500])
        else:
            print("No <article> tag found.")
        print("-" * 50)
