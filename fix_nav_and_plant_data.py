import glob
import re

canopy = ["Aghedo", "Amla", "Amba", "Anjan", "Banni", "Behda", "Bhadraaksh", "Coconut", "Dudalo", "Fanas", "Gajpipal", "Gangeti", "Garmalo", "Jarul", "Vad", "Kadam", "Kalo Arjun", "Kapok", "Karanj", "Khalosiris", "Krishanvad", "Krishnaparni", "Kusum", "Limdo", "Mahudo", "Manvel Bamboo", "Marvo", "Neer Fanas", "Panervo", "Umaro", "Pipal / Pipalo", "Pinkasiya", "Pragvad", "Rain Tree", "Rudraksh", "Rukhdo", "Sag / Teak", "Safedsiris", "Samudravad", "Setur", "Sisam", "Sisu", "Tebubiya", "Timru", "Umbh"]

tree_layer = ["Asopalav", "Aaval", "Ambali", "Aniyar", "Anjir", "Arduso", "Ashok", "Bauchi", "Bangali Baval", "Bili", "Bordar", "Bordi", "Charoli", "Chandan", "Khajuri", "Kharek", "Khati Amli", "Kilai", "Kidakhari", "Kothi / Kothu", "Kali Rayan", "Miletia", "Modal", "Mordhundhiyu", "Nagod", "Paras Piplo", "Parijat", "Peltroform", "Pendula", "Vasant", "Chiku", "Baval", "Dhaman", "Dheki", "Gando Baval", "Ghatbor", "Gorad", "Goras Ambali", "Gulmohar", "Gugal", "Haldarvo", "Indravjav", "Jambu", "Jakranta", "Khair", "Piloo", "Pipado", "Pongaro", "Putranjiva", "Ragat Rohido", "Ramfal", "Ravana", "Raktchandan", "Rijado", "Rubber Tree", "Rukado", "Sadad", "Salai", "Samdi", "Vas", "Kachnar", "Kadayo", "Kadipatta", "Kadvi Harde", "Kaijelia", "Kaju", "Kakad", "Kala Dhau", "Kamrakh", "Kantas Bamboo", "Karamadi", "Karaj", "Kasid", "Kher", "Khakharo / Palas", "Sami", "Sargavo", "Sevan", "Sharu", "Shisam", "Sirus", "Sopari", "Spathodia", "Subaval", "Tad", "Tanachh", "Techma", "Tentu", "Varun", "Varakhdo"]

sub_tree = ["Agathiyo", "Ankol Pabdi", "Aralu", "Ardusi", "Badam", "Bijora", "Bor", "Dadam", "Falsa", "Galtoriya", "Gugal", "Gundo / Gundi", "Hanumanfal", "Harfarevdi", "Mindhol", "Igoriya", "Jamfal (Guava)", "Kai Baval", "Kakchiya", "Kanji", "Karmada", "Kerda", "Kel (Banana)", "Khijado", "Khara Pilu", "Limbu / Limboo", "Mardasingi", "Marodfali", "Sinduri", "Viklo", "Mitha Pila", "Mitho Limdo", "Mosanbi", "Nagol", "Papaiya", "Raktrolido", "Salaigugal", "Samudra Fal", "Santara", "Simaruba"]

ground_cover = ["Vantulsi", "Vila Mehandi", "Ajamo", "Arani", "Aranda", "Ashwagandha", "Chakotara", "Chandani", "Chitrak", "Din Ka Raja", "Dikamari", "Dhanturo", "Galgota", "Gulab", "Variyali", "Jangali Tamaku", "Jasud", "Karen", "Kasumbi", "Lemon Grass", "Madhukamini", "Panfutti", "Prabat", "Ratanjyot", "Ratrani", "Shalparni", "Shivlingi", "Takmariya"]

def generate_badges(items):
    html = ""
    for item in sorted(list(set(items))):
        html += f'<span style="background: #e8f5e9; color: var(--primary-color); padding: 8px 15px; border-radius: 20px; font-size: 0.95rem; border: 1px solid rgba(44, 95, 45, 0.2); box-shadow: 0 2px 4px rgba(0,0,0,0.02);">{item}</span>\\n                    '
    return html

plant_data_html = f"""
            <!-- Native Tree Species Guide -->
            <div class="content-block" style="background:#fff; padding:40px; border-radius:15px; box-shadow:var(--shadow);">
                <h2 style="color:var(--primary-color); margin-bottom: 20px; font-size: 2rem;">Native Tree Species Guide</h2>
                <p style="font-size:1.1rem; color:var(--text-muted); margin-bottom: 30px;">A comprehensive list of native species categorized by their ecological layer, chosen for optimal growth and biodiversity in our Urban Forests.</p>
                
                <!-- Canopy Layer -->
                <div style="margin-bottom: 35px;">
                    <h3 style="color:var(--text-dark); margin-bottom: 15px; font-size: 1.4rem; border-bottom: 2px solid var(--secondary-color); padding-bottom: 5px; display: inline-block;">Canopy Layer</h3>
                    <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px;">
                        {generate_badges(canopy)}
                    </div>
                </div>
                
                <!-- Tree Layer -->
                <div style="margin-bottom: 35px;">
                    <h3 style="color:var(--text-dark); margin-bottom: 15px; font-size: 1.4rem; border-bottom: 2px solid var(--secondary-color); padding-bottom: 5px; display: inline-block;">Tree Layer</h3>
                    <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px;">
                        {generate_badges(tree_layer)}
                    </div>
                </div>

                <!-- Sub-Tree Layer -->
                <div style="margin-bottom: 35px;">
                    <h3 style="color:var(--text-dark); margin-bottom: 15px; font-size: 1.4rem; border-bottom: 2px solid var(--secondary-color); padding-bottom: 5px; display: inline-block;">Sub-Tree Layer</h3>
                    <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px;">
                        {generate_badges(sub_tree)}
                    </div>
                </div>

                <!-- Ground Cover -->
                <div style="margin-bottom: 15px;">
                    <h3 style="color:var(--text-dark); margin-bottom: 15px; font-size: 1.4rem; border-bottom: 2px solid var(--secondary-color); padding-bottom: 5px; display: inline-block;">Ground Cover</h3>
                    <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px;">
                        {generate_badges(ground_cover)}
                    </div>
                </div>
            </div>
"""

# Read about.html to use as template
with open('about.html', 'r', encoding='utf-8') as f:
    about = f.read()

# Fix the broken navbar if it exists
if '<li><a href="impact.html">Plant Data</a></li>' in about:
    about = about.replace('<li><a href="impact.html">Plant Data</a></li>', '<li><a href="impact.html">Impacts</a></li>')

nav_end = about.find('</nav>') + 6
footer_start = about.find('<footer')

header_part = about[:nav_end]
footer_part = about[footer_start:]

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
    <a href="contact.html" class="floating-contact"><i class="fas fa-comment-dots"></i></a>
"""

plant_data_full = header_part + new_body + footer_part
plant_data_full = plant_data_full.replace('<title>GRGVS | About Us</title>', '<title>GRGVS | Plant Data</title>')

with open('plant-data.html', 'w', encoding='utf-8') as f:
    f.write(plant_data_full)

# Now fix navigation and remove from urban-forest in all files
files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the impact link if it got corrupted
    if '<li><a href="impact.html">Plant Data</a></li>' in content:
        content = content.replace('<li><a href="impact.html">Plant Data</a></li>', '<li><a href="impact.html">Impacts</a></li>')

    # Remove the plant data guide from urban-forest if it's there
    if file == 'urban-forest.html':
        pattern = r'(<!-- Native Tree Species Guide -->.*?</div>\s*</div>)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content.replace(match.group(1), '')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Plant data recreated, moved, and navbars fixed successfully!")
