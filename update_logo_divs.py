import os
import glob
import re

html_files = glob.glob('*.html')

old_pattern = re.compile(r'<a href="index\.html" class="logo" style="display:flex; align-items:center; gap: 15px; text-decoration: none;">\s*<img src="\./assets/Logo\.jpg" alt="GRGVS Logo" style="height: 85px; width: auto; margin-left: 0;">\s*<div class="logo-text-block" style="display: flex; flex-direction: column; justify-content: center;">\s*<span style="font-family: \'Outfit\', sans-serif; font-size: 26px; font-weight: 500; color: var\(--primary-color\); letter-spacing: 0\.5px; line-height: 1\.2; white-space: nowrap;">GUJARAT RAJYA GRAM VIKAS SAMITI</span>\s*<span style="font-family: \'Inter\', sans-serif; font-size: 16px; font-weight: 400; color: var\(--primary-color\); line-height: 1\.2; white-space: nowrap;">36 Years journey of empowerment</span>\s*</div>\s*</a>')

new_html = """<div class="logo-wrapper" style="display: flex; align-items: center; gap: 20px;">
                <a href="index.html" class="logo" style="text-decoration: none;">
                    <img src="./assets/Logo.jpg" alt="GRGVS Logo" style="height: 105px; width: auto; display: block;">
                </a>
                <div class="logo-text-block" style="display: flex; flex-direction: column; justify-content: center;">
                    <span style="font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 500; color: var(--primary-color); letter-spacing: 0.5px; line-height: 1.2; white-space: nowrap;">GUJARAT RAJYA GRAM VIKAS SAMITI</span>
                    <span style="font-family: 'Inter', sans-serif; font-size: 17px; font-weight: 400; color: var(--primary-color); line-height: 1.2; white-space: nowrap;">36 Years journey of empowerment</span>
                </div>
            </div>"""

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
