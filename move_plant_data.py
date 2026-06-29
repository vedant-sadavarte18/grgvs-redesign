import glob
import re

# 1. Read urban-forest.html
with open('urban-forest.html', 'r', encoding='utf-8') as f:
    urban_content = f.read()

# Extract the Native Tree Species Guide
pattern = r'(<!-- Native Tree Species Guide -->.*?</div>\s*</div>)'
match = re.search(pattern, urban_content, re.DOTALL)
if match:
    plant_data_html = match.group(1)
    # Remove from urban-forest.html
    urban_content = urban_content.replace(plant_data_html, '')
    
    with open('urban-forest.html', 'w', encoding='utf-8') as f:
        f.write(urban_content)
else:
    print("Could not find plant data in urban-forest.html")
    plant_data_html = "<h1>Plant Data</h1>"

# 2. Create plant-data.html
# Use about.html as template to get header/footer
with open('about.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace title
template = re.sub(r'<title>.*?</title>', '<title>Plant Data - GRGVS</title>', template)

# Replace everything inside <main> or between header and footer
# Actually, it's better to just replace the main content sections
body_pattern = r'(</header>\s*)(.*?)(\s*<footer)'
match_body = re.search(body_pattern, template, re.DOTALL)
if match_body:
    # Build new body
    new_body = f"""
    <section class="page-header" style="background:var(--primary-color); padding: 60px 0; color: white; text-align: center;">
        <div class="container">
            <h1 style="font-size: 2.5rem; margin-bottom: 10px;">Plant Data</h1>
            <p style="font-size: 1.1rem; opacity: 0.9;">Native tree species data for our afforestation projects</p>
        </div>
    </section>
    
    <section style="padding: 60px 0;">
        <div class="container">
            {plant_data_html}
        </div>
    </section>
    """
    plant_data_full = template[:match_body.start(2)] + new_body + template[match_body.end(2):]
    with open('plant-data.html', 'w', encoding='utf-8') as f:
        f.write(plant_data_full)
else:
    print("Could not find body in template")

# 3. Add to Navbar across all files
files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if Plant Data is already in navbar to avoid duplicates
    if 'plant-data.html' not in content:
        # Insert Plant Data after Urban Forest or Volunteer.
        # Let's insert it before Volunteer
        content = content.replace('<li><a href="volunteer.html">Volunteer</a></li>',
                                  '<li><a href="plant-data.html">Plant Data</a></li>\n                <li><a href="volunteer.html">Volunteer</a></li>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Plant data moved successfully!")
