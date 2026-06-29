import glob
import re

files = glob.glob('*.html')
count = 0

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to find the img tag for Logo.jpg
    # It looks like: <img src="./assets/Logo.jpg" alt="GRGVS Logo" style="height: 100px; width: auto; margin-top: 5px;">
    
    new_content, c1 = re.subn(
        r'<img src="\./assets/Logo\.jpg" alt="GRGVS Logo" style="height: \d+px; width: auto; margin-top: 5px;">',
        '<img src="./assets/Logo.jpg" alt="GRGVS Logo" style="height: 130px; width: auto; margin-top: 5px; margin-left: -30px;">',
        content
    )
    
    # What if it doesn't have the exact style string? 
    # Let's do a more robust regex if the above didn't match
    if c1 == 0:
        new_content, c2 = re.subn(
            r'<img src="\./assets/Logo\.jpg" alt="GRGVS Logo"([^>]*)>',
            r'<img src="./assets/Logo.jpg" alt="GRGVS Logo" style="height: 130px; width: auto; margin-top: 5px; margin-left: -40px;">',
            content
        )
        if c2 > 0:
            count += 1
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
    else:
        count += 1
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f"Updated logo size and position in {count} HTML files.")
