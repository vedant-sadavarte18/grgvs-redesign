import os, re, glob

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

images = glob.glob('images/sdgs/*.png')
def get_sdg_num(filename):
    m = re.search(r'sdg_(\d+)_', filename)
    return int(m.group(1)) if m else 0

images.sort(key=get_sdg_num)

for i in range(1, 18):
    img_path = next((img for img in images if f'sdg_{i}_' in img), None)
    if img_path:
        img_path = img_path.replace('\\', '/')
        html = re.sub(r'https://loremflickr\.com/[^\"]+', img_path, html, count=1)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated HTML with local generated images!')
