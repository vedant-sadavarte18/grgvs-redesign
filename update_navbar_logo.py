import os
import glob
import re

html_files = glob.glob('*.html')

pattern = re.compile(r'<a href="index\.html" class="logo"[\s\S]*?</a>')

new_logo = '''<a href="index.html" class="logo" style="display:flex; align-items:center; gap: 15px; text-decoration: none;">
                <img src="./assets/Logo.jpg" alt="GRGVS Logo" style="height: 85px; width: auto; margin-left: 0;">
                <div class="logo-text-block" style="display: flex; flex-direction: column; justify-content: center;">
                    <span style="font-family: \'Outfit\', sans-serif; font-size: 26px; font-weight: 500; color: var(--primary-color); letter-spacing: 0.5px; line-height: 1.2; white-space: nowrap;">GUJARAT RAJYA GRAM VIKAS SAMITI</span>
                    <span style="font-family: \'Inter\', sans-serif; font-size: 16px; font-weight: 400; color: var(--primary-color); line-height: 1.2; white-space: nowrap;">36 Years journey of empowerment</span>
                </div>
            </a>'''

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if pattern.search(content):
        new_content = pattern.sub(new_logo, content)
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1

print(f"Updated {count} files.")
