import os
import glob

# 1. Update styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()
    
css = css.replace('background: rgba(255, 255, 255, 0.95);', 'background: #ffffff;')
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
    
# 2. Update new_styles.css
with open('new_styles.css', 'r', encoding='utf-8') as f:
    new_css = f.read()

new_css = new_css.replace('background: rgba(255, 255, 255, 0.95);', 'background: #ffffff;')
with open('new_styles.css', 'w', encoding='utf-8') as f:
    f.write(new_css)

# 3. Update all HTML files
html_files = glob.glob('*.html')

old_img_1 = '<img src="./assets/Logo.jpg" alt="GRGVS Logo" style="height: 80px; width: auto;">'
new_img = '<img src="./assets/Logo.jpg" alt="GRGVS Logo" style="height: 100px; width: 140px; object-fit: fill;">'

old_a_1 = '<a href="index.html" class="logo" style="display:flex; align-items:center;">'
# Actually, the user wants "when i click the logo i am taken to the home page"
# It's already wrapped in <a href="index.html">. 
# Let's ensure it is.

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if old_img_1 in content:
        content = content.replace(old_img_1, new_img)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Replaced logo in {file}')
    else:
        print(f'Logo not found in {file}')
