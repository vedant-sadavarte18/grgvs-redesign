import re

with open('partners.html', 'r', encoding='utf-8') as f:
    text = f.read()

adani_html = """
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/Adani_2012_logo.png" alt="Adani" style="width:90%; height:90%; object-fit:contain;">
                </div>"""

# Insert it immediately after the grid container starts
target_string = '<!-- Corporate Logos -->'

idx = text.find(target_string)
if idx != -1:
    new_text = text[:idx + len(target_string)] + adani_html + text[idx + len(target_string):]
    with open('partners.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Adani added.")
else:
    print("Could not find insertion point.")
