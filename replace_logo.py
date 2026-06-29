import os
import glob

# The string to search for
old_logo = '<a href="index.html" class="logo"><span class="logo-text">GRGVS</span></a>'

# The replacement string
new_logo = '''<a href="index.html" class="logo" style="display:flex; align-items:center;">
                <img src="./assets/logo.png" alt="GRGVS Logo" style="height: 55px; width: auto; margin-top: 5px;">
            </a>'''

# Files to process
html_files = glob.glob('*.html')

for file in html_files:
    if file == 'index.html':
        continue # Already done manually
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if old_logo in content:
        content = content.replace(old_logo, new_logo)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Replaced logo in {file}')
    else:
        # Some files might have slightly different whitespace
        # Let's do a more robust check if needed
        old_logo_2 = '<a href="index.html" class="logo">\n                <span class="logo-text">GRGVS</span>\n            </a>'
        if old_logo_2 in content:
            content = content.replace(old_logo_2, new_logo)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Replaced logo (multi-line) in {file}')
        else:
            print(f'No matching logo found in {file}')
