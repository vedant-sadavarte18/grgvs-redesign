import os
import glob

html_files = glob.glob('*.html')

old_str = """                <li><a href="partners.html">Partners</a></li>
                <li><a href="csr.html">CSR</a></li>"""
new_str = """                <li><a href="partners.html">Partners & CSR</a></li>"""

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_str in content:
        new_content = content.replace(old_str, new_str)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated {count} files.")
