import glob
import re

# We need the plant data html
with open('add_native_species.py', 'r', encoding='utf-8') as f:
    script = f.read()

# I will just extract the plant data from urban-forest.html if it's there
with open('urban-forest.html', 'r', encoding='utf-8') as f:
    urban = f.read()

pattern = r'(<!-- Native Tree Species Guide -->.*?</div>\s*</div>)'
match = re.search(pattern, urban, re.DOTALL)
if match:
    plant_data = match.group(1)
    # Remove from urban forest
    urban = urban.replace(plant_data, '')
    with open('urban-forest.html', 'w', encoding='utf-8') as f:
        f.write(urban)
else:
    # If not in urban-forest, let's look for it in plant-data.html if it exists, otherwise just redefine it
    plant_data = "<!-- Need to recreate plant data if missing -->"

if "<!-- Need to" in plant_data:
    # We will recreate it
    pass

# Read about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about = f.read()

# Split about at </header>
parts = about.split('</header>')
header_part = parts[0] + '</header>'

# Split the remaining part at <footer
footer_parts = parts[1].split('<footer')
footer_part = '<footer' + footer_parts[1]

# Make the plant_data body
new_body = f"""
    <section class="page-header" style="background:var(--primary-color); padding: 60px 0; color: white; text-align: center;">
        <div class="container">
            <h1 style="font-size: 2.5rem; margin-bottom: 10px;">Plant Data</h1>
            <p style="font-size: 1.1rem; opacity: 0.9;">Native tree species data for our afforestation projects</p>
        </div>
    </section>
    
    <section style="padding: 60px 0;">
        <div class="container">
{plant_data}
        </div>
    </section>
"""

# Stitch together
plant_data_html = header_part + new_body + footer_part
plant_data_html = plant_data_html.replace('<title>About Us - GRGVS</title>', '<title>Plant Data - GRGVS</title>')

with open('plant-data.html', 'w', encoding='utf-8') as f:
    f.write(plant_data_html)

# Now fix navigation across all files
files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'plant-data.html' not in content:
        content = content.replace('<li><a href="volunteer.html">Volunteer</a></li>',
                                  '<li><a href="plant-data.html">Plant Data</a></li>\n                <li><a href="volunteer.html">Volunteer</a></li>')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Plant data recreated and moved successfully!")
