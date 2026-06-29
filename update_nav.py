import os
import glob

html_files = glob.glob('*.html')
target = '<li><a href="contact.html">Contact</a></li>'
replacement = '<li><a href="volunteer.html">Volunteer</a></li>\n                <li><a href="contact.html">Contact</a></li>'

for f in html_files:
    if f == 'volunteer.html':
        continue # volunteer already has it. Wait, I added it in volunteer.html already!
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if target in content and 'volunteer.html' not in content:
        content = content.replace(target, replacement)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
            print(f"Updated {f}")
