import glob
import re
from bs4 import BeautifulSoup

# 1. Parse CSR content
csr_source_file = r"C:\Users\HP\.gemini\antigravity\brain\681070d0-73dc-4b63-b394-c8f161e0a98f\.system_generated\steps\1639\content.md"

with open(csr_source_file, "r", encoding="utf-8") as f:
    content_raw = f.read()

html_start = content_raw.find("<!DOCTYPE html>")
if html_start != -1:
    content_raw = content_raw[html_start:]

soup = BeautifulSoup(content_raw, 'html.parser')
main_content = soup.find('article') or soup.find('main') or soup.body

# Extract paragraphs and lists from main content
# For simplicity, we'll extract text and format it into HTML blocks
text_elements = []
if main_content:
    for elem in main_content.find_all(['p', 'ul', 'ol', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        if elem.name.startswith('h'):
            text_elements.append(f"<h3 style='color: var(--primary-color); margin-top: 30px; margin-bottom: 15px;'>{elem.get_text(strip=True)}</h3>")
        elif elem.name in ['ul', 'ol']:
            list_items = "".join([f"<li style='margin-bottom: 10px; font-size: 1.1rem;'><i class='fas fa-check-circle' style='color: var(--secondary-color); margin-right: 10px;'></i>{li.get_text(strip=True)}</li>" for li in elem.find_all('li')])
            text_elements.append(f"<ul style='list-style: none; padding-left: 0;'>{list_items}</ul>")
        elif elem.name == 'p':
            text = elem.get_text(strip=True)
            if text and not text.lower() == 'read more':
                text_elements.append(f"<p style='font-size: 1.1rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 20px;'>{text}</p>")

csr_html_content = "\n".join(text_elements)

# 2. Read about.html as template
with open('about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

# Replace the title and page header
about_html = re.sub(r'<title>.*?</title>', '<title>CSR Initiatives - GRGVS</title>', about_html)
about_html = re.sub(r'<h1.*?>.*?</h1>', '<h1 style="font-size: 2.5rem; margin-bottom: 10px;">CSR Initiatives</h1>', about_html, count=1)
about_html = re.sub(r'<p style="font-size: 1.1rem; opacity: 0.9;">.*?</p>', '<p style="font-size: 1.1rem; opacity: 0.9;">Corporate Social Responsibility</p>', about_html, count=1)

# Replace the main content section
# We will find the section after the page-header and replace it
# For about.html, it's typically <section class="about-section">
# Let's just replace the entire content of that section
def replace_section(match):
    return f"""<section class="csr-section" style="padding: 80px 0; background: #fff;">
    <div class="container" style="max-width: 900px; margin: 0 auto;">
        {csr_html_content}
    </div>
</section>"""

# Try to find a section that's not page-header
about_html = re.sub(r'<section class="([^"]*(?!page-header)[^"]*)".*?>.*?</section>', replace_section, about_html, count=1, flags=re.DOTALL)

# Let's ensure the class is changed if it was about-section
with open('csr.html', 'w', encoding='utf-8') as f:
    f.write(about_html)

# 3. Add CSR tab to all HTML files
files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # Check if CSR is already in nav
    if 'href="csr.html"' not in file_content:
        # Find the nav-links ul and append the list item
        # Look for the last <li> before </ul> in nav-links
        # A simple string replacement before </ul> inside <ul class="nav-links">
        
        # A more robust regex replacement for nav-links:
        # We need to insert before the closing </ul> of .nav-links
        def insert_nav(m):
            nav_inner = m.group(1)
            # Make sure we don't insert duplicate
            if 'csr.html' not in nav_inner:
                return f'<ul class="nav-links">{nav_inner}\n                <li><a href="csr.html">CSR</a></li>\n            </ul>'
            return m.group(0)

        new_content = re.sub(r'<ul class="nav-links">(.*?)</ul>', insert_nav, file_content, flags=re.DOTALL)
        
        if new_content != file_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
print("Created csr.html and updated all navbars.")
