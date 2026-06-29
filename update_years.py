import os
import glob

html_files = glob.glob('*.html')
old_text = "36 Years journey of empowerment"
new_text = "37+ Years journey of empowerment"

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Updated {count} files.")
