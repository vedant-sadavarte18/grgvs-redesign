import glob
import re

files = glob.glob('*.html')
removed_count = 0

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to find and remove the list item containing impact.html
    # We want to remove the whole line including leading whitespace and trailing newline
    new_content, count = re.subn(r'\s*<li><a href="impact\.html">Impacts</a></li>', '', content)
    
    if count > 0:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        removed_count += 1
        print(f"Removed Impacts tab from {file}")

print(f"Total files updated: {removed_count}")
