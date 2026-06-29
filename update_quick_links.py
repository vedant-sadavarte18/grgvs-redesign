import os
import glob

html_files = glob.glob('*.html')

old_str = """                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 10px;"><a href="index.html" style="color: #aaa; text-decoration: none;">Home</a></li>
                        <li style="margin-bottom: 10px;"><a href="about.html" style="color: #aaa; text-decoration: none;">About Us</a></li>
                        <li style="margin-bottom: 10px;"><a href="goals.html" style="color: #aaa; text-decoration: none;">Our Goals</a></li>
                        <li style="margin-bottom: 10px;"><a href="contact.html" style="color: #aaa; text-decoration: none;">Contact</a></li>
                    </ul>"""

new_str = """                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 10px;"><a href="index.html" style="color: #aaa; text-decoration: none;">Home</a></li>
                        <li style="margin-bottom: 10px;"><a href="about.html" style="color: #aaa; text-decoration: none;">About Us</a></li>
                        <li style="margin-bottom: 10px;"><a href="goals.html" style="color: #aaa; text-decoration: none;">Our Goals</a></li>
                        <li style="margin-bottom: 10px;"><a href="partners.html" style="color: #aaa; text-decoration: none;">Partners</a></li>
                        <li style="margin-bottom: 10px;"><a href="contact.html" style="color: #aaa; text-decoration: none;">Contact</a></li>
                        <li style="margin-bottom: 10px;"><a href="donate.html" style="color: #aaa; text-decoration: none;">Donate</a></li>
                    </ul>"""

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
