import re

# 1. Fix literal \n in plant-data.html
with open('plant-data.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace literal \n that was accidentally written
# Note: we are looking for the exact characters '\' and 'n'
content = content.replace('\\n', ' ')

with open('plant-data.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed literal \\n in plant-data.html")

# 2. Let's look at styles.css for nav-links to see why they are overlapping
with open('styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

match = re.search(r'\.nav-links\s*{(.*?)}', css_content, re.DOTALL)
if match:
    print(".nav-links {", match.group(1), "}")

match2 = re.search(r'\.nav-links a\s*{(.*?)}', css_content, re.DOTALL)
if match2:
    print(".nav-links a {", match2.group(1), "}")

match3 = re.search(r'\.nav-links li\s*{(.*?)}', css_content, re.DOTALL)
if match3:
    print(".nav-links li {", match3.group(1), "}")
