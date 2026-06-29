import glob
import re

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'<ul class="nav-links">(.*?)</ul>', content, re.DOTALL)
    if match:
        print(f"--- {file} ---")
        print(match.group(1).strip())
