import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to move <li><a href="csr.html">CSR</a></li> to be after Partners
    # Let's find the nav-links block
    
    # Remove existing CSR li
    content = re.sub(r'\s*<li><a href=\"csr.html\">CSR</a></li>', '', content)
    
    # Insert it after Partners
    content = content.replace(
        '<li><a href="partners.html">Partners</a></li>',
        '<li><a href="partners.html">Partners</a></li>\n                <li><a href="csr.html">CSR</a></li>'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f'Updated {len(html_files)} files.')
