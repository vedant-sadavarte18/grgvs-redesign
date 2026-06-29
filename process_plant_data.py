import glob
import re

# 1. Read plant-data.html to extract the info
with open('plant-data.html', 'r', encoding='utf-8') as f:
    plant_data_content = f.read()

# Extract everything inside the Native Tree Species Guide content-block
pattern = r'(<div class="content-block"[^>]*>\s*<h2[^>]*>Native Tree Species Guide.*?</div>\s*</div>\s*</div>\s*</div>)'
match = re.search(pattern, plant_data_content, re.DOTALL)
if match:
    extracted_data = match.group(1)
    # The regex might not capture all divs perfectly if there are multiple nested ones.
    # Let's use a simpler pattern since we know the structure.
    # It starts with <!-- Native Tree Species Guide -->
    # and we can just extract the whole container content.
else:
    # Fallback to extracting the entire container div content
    start_str = '<!-- Native Tree Species Guide -->'
    end_str = '<!-- Sub-Tree Layer -->'
    
    # Actually, let's just grab the whole content-block
    start_idx = plant_data_content.find('<!-- Native Tree Species Guide -->')
    end_idx = plant_data_content.find('</section>', start_idx)
    # We just want the content-block div
    extracted_data = plant_data_content[start_idx:end_idx].strip()
    # It contains an extra </div> for the container, let's trim it
    if extracted_data.endswith('</div>\n        </div>'):
        extracted_data = extracted_data[:-14].strip()
    elif extracted_data.endswith('</div>'):
        extracted_data = extracted_data[:-6].strip()

# 2. Add to goal-1.html (Green Gujarat)
with open('goal-1.html', 'r', encoding='utf-8') as f:
    goal1 = f.read()

# Insert before the back button
insertion_point_g1 = '<div style="margin-top:40px;">\n                    <a href="goals.html"'
if insertion_point_g1 in goal1:
    goal1 = goal1.replace(insertion_point_g1, f"{extracted_data}\n\n                {insertion_point_g1}")
    with open('goal-1.html', 'w', encoding='utf-8') as f:
        f.write(goal1)
    print("Added to goal-1.html")
else:
    print("Could not find insertion point in goal-1.html")

# 3. Add to urban-forest.html
with open('urban-forest.html', 'r', encoding='utf-8') as f:
    uf = f.read()

# Insert at the end of the urban-forest content section, before the footer or before the contact icon
insertion_point_uf = '<a href="contact.html" class="floating-contact">'
if insertion_point_uf in uf:
    uf = uf.replace(insertion_point_uf, f'<section style="padding: 60px 0;">\n        <div class="container">\n            {extracted_data}\n        </div>\n    </section>\n    {insertion_point_uf}')
    with open('urban-forest.html', 'w', encoding='utf-8') as f:
        f.write(uf)
    print("Added to urban-forest.html")
else:
    print("Could not find insertion point in urban-forest.html")

# 4. Remove from Navbar in all HTML files
files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to remove the Plant Data list item
    new_content = re.sub(r'\s*<li><a href="plant-data\.html"[^>]*>Plant Data</a></li>', '', content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed nav tab from {file}")

print("Done processing plant data!")
