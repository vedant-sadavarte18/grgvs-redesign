import re

canopy = ["Aghedo", "Amla", "Amba", "Anjan", "Banni", "Behda", "Bhadraaksh", "Coconut", "Dudalo", "Fanas", "Gajpipal", "Gangeti", "Garmalo", "Jarul", "Vad", "Kadam", "Kalo Arjun", "Kapok", "Karanj", "Khalosiris", "Krishanvad", "Krishnaparni", "Kusum", "Limdo", "Mahudo", "Manvel Bamboo", "Marvo", "Neer Fanas", "Panervo", "Umaro", "Pipal / Pipalo", "Pinkasiya", "Pragvad", "Rain Tree", "Rudraksh", "Rukhdo", "Sag / Teak", "Safedsiris", "Samudravad", "Setur", "Sisam", "Sisu", "Tebubiya", "Timru", "Umbh"]

tree_layer = ["Asopalav", "Aaval", "Ambali", "Aniyar", "Anjir", "Arduso", "Ashok", "Bauchi", "Bangali Baval", "Bili", "Bordar", "Bordi", "Charoli", "Chandan", "Khajuri", "Kharek", "Khati Amli", "Kilai", "Kidakhari", "Kothi / Kothu", "Kali Rayan", "Miletia", "Modal", "Mordhundhiyu", "Nagod", "Paras Piplo", "Parijat", "Peltroform", "Pendula", "Vasant", "Chiku", "Baval", "Dhaman", "Dheki", "Gando Baval", "Ghatbor", "Gorad", "Goras Ambali", "Gulmohar", "Gugal", "Haldarvo", "Indravjav", "Jambu", "Jakranta", "Khair", "Piloo", "Pipado", "Pongaro", "Putranjiva", "Ragat Rohido", "Ramfal", "Ravana", "Raktchandan", "Rijado", "Rubber Tree", "Rukado", "Sadad", "Salai", "Samdi", "Vas", "Kachnar", "Kadayo", "Kadipatta", "Kadvi Harde", "Kaijelia", "Kaju", "Kakad", "Kala Dhau", "Kamrakh", "Kantas Bamboo", "Karamadi", "Karaj", "Kasid", "Kher", "Khakharo / Palas", "Sami", "Sargavo", "Sevan", "Sharu", "Shisam", "Sirus", "Sopari", "Spathodia", "Subaval", "Tad", "Tanachh", "Techma", "Tentu", "Varun", "Varakhdo"]

sub_tree = ["Agathiyo", "Ankol Pabdi", "Aralu", "Ardusi", "Badam", "Bijora", "Bor", "Dadam", "Falsa", "Galtoriya", "Gugal", "Gundo / Gundi", "Hanumanfal", "Harfarevdi", "Mindhol", "Igoriya", "Jamfal (Guava)", "Kai Baval", "Kakchiya", "Kanji", "Karmada", "Kerda", "Kel (Banana)", "Khijado", "Khara Pilu", "Limbu / Limboo", "Mardasingi", "Marodfali", "Sinduri", "Viklo", "Mitha Pila", "Mitho Limdo", "Mosanbi", "Nagol", "Papaiya", "Raktrolido", "Salaigugal", "Samudra Fal", "Santara", "Simaruba"]

ground_cover = ["Vantulsi", "Vila Mehandi", "Ajamo", "Arani", "Aranda", "Ashwagandha", "Chakotara", "Chandani", "Chitrak", "Din Ka Raja", "Dikamari", "Dhanturo", "Galgota", "Gulab", "Variyali", "Jangali Tamaku", "Jasud", "Karen", "Kasumbi", "Lemon Grass", "Madhukamini", "Panfutti", "Prabat", "Ratanjyot", "Ratrani", "Shalparni", "Shivlingi", "Takmariya"]

def generate_badges(items):
    html = ""
    for item in sorted(list(set(items))): # deduplicate and sort alphabetically
        html += f'<span style="background: #e8f5e9; color: var(--primary-color); padding: 8px 15px; border-radius: 20px; font-size: 0.95rem; border: 1px solid rgba(44, 95, 45, 0.2); box-shadow: 0 2px 4px rgba(0,0,0,0.02);">{item}</span>\n                    '
    return html

native_species_html = f"""
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

with open('urban-forest.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before "<!-- Locations Identified -->"
content = content.replace("<!-- Locations Identified -->", native_species_html + "\n            <!-- Locations Identified -->")

with open('urban-forest.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added Native Tree Species Guide successfully!")
