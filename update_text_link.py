import os
import glob
import re

html_files = glob.glob('*.html')

old_pattern = re.compile(r'<div class="logo-text-block" style="display: flex; flex-direction: column; justify-content: center;">\s*<span style="font-family: \'Outfit\', sans-serif; font-size: 28px; font-weight: 500; color: var\(--primary-color\); letter-spacing: 0\.5px; line-height: 1\.2; white-space: nowrap;">GUJARAT RAJYA GRAM VIKAS SAMITI</span>\s*<span style="font-family: \'Inter\', sans-serif; font-size: 17px; font-weight: 400; color: var\(--primary-color\); line-height: 1\.2; white-space: nowrap;">36 Years journey of empowerment</span>\s*</div>')

new_html = """<a href="index.html" class="logo-text-block" style="display: flex; flex-direction: column; justify-content: center; text-decoration: none;">
                    <span style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 500; color: var(--primary-color); letter-spacing: 0.5px; line-height: 1.2; white-space: nowrap;">GUJARAT RAJYA GRAM VIKAS SAMITI</span>
                    <span style="font-family: 'Inter', sans-serif; font-size: 17px; font-weight: 400; color: var(--primary-color); line-height: 1.2; white-space: nowrap;">36 Years journey of empowerment</span>
                </a>"""

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_pattern.search(content):
        new_content = old_pattern.sub(new_html, content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated {count} files.")
