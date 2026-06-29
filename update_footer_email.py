import os
import glob

html_files = glob.glob('*.html')

search_str = '<p style="color: #aaa; margin-bottom: 10px;"><i class="fas fa-envelope" style="margin-right: 10px;"></i> info@gujaratgramvikas.org</p>'
replace_str = '<p style="color: #aaa; margin-bottom: 10px;"><i class="fas fa-envelope" style="margin-right: 10px;"></i> info@gujaratgramvikas.org</p>\n                    <p style="color: #aaa; margin-bottom: 10px;"><i class="fas fa-envelope" style="margin-right: 10px;"></i> CSR@gujaratgramvikas.org</p>'

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if search_str in content:
        content = content.replace(search_str, replace_str)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Updated {count} files.")
