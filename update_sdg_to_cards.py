import re

official_sdgs = [
    ('1', 'No<br>Poverty', '#E5243B', 'fa-users'),
    ('2', 'Zero<br>Hunger', '#DDA63A', 'fa-bowl-food'),
    ('3', 'Good Health<br>and Well-being', '#4C9F38', 'fa-heart-pulse'),
    ('4', 'Quality<br>Education', '#C5192D', 'fa-book-open'),
    ('5', 'Gender<br>Equality', '#FF3A21', 'fa-venus-mars'),
    ('6', 'Clean Water<br>and Sanitation', '#26BDE2', 'fa-glass-water'),
    ('7', 'Affordable and<br>Clean Energy', '#FCC30B', 'fa-sun'),
    ('8', 'Decent Work and<br>Economic Growth', '#A21942', 'fa-chart-line'),
    ('9', 'Industry, Innovation<br>and Infrastructure', '#FD6925', 'fa-industry'),
    ('10', 'Reduced<br>Inequalities', '#DD1367', 'fa-equals'),
    ('11', 'Sustainable Cities<br>and Communities', '#FD9D24', 'fa-city'),
    ('12', 'Responsible<br>Consumption<br>and Production', '#BF8B2E', 'fa-recycle'),
    ('13', 'Climate<br>Action', '#3F7E44', 'fa-earth-americas'),
    ('14', 'Life<br>Below Water', '#0A97D9', 'fa-fish'),
    ('15', 'Life<br>on Land', '#56C02B', 'fa-tree'),
    ('16', 'Peace, Justice<br>and Strong<br>Institutions', '#00689D', 'fa-scale-balanced'),
    ('17', 'Partnerships<br>for the Goals', '#19486A', 'fa-handshake')
]

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

image_paths = []
for i in range(1, 18):
    match = re.search(fr'src="(assets/sdgs/sdg_{i}_[^"]+)"', content)
    if match:
        image_paths.append(match.group(1))
    else:
        image_paths.append(f"assets/sdgs/sdg_{i}_fallback.png")

html_grid = []
for idx, (num, title, color, icon) in enumerate(official_sdgs):
    img_src = image_paths[idx]
    
    html_grid.append(f'''
                <div class="sdg-card" style="display: flex; flex-direction: column; overflow: hidden; background: #fff; box-shadow: 0 4px 15px rgba(0,0,0,0.08); transition: transform 0.3s ease; border-radius: 8px;">
                    <div style="aspect-ratio: 4/3; overflow: hidden;">
                        <img src="{img_src}" alt="{title.replace('<br>', ' ')}" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;">
                    </div>
                    <div style="background: {color}; padding: 15px 20px; color: white; display: flex; align-items: center; justify-content: space-between; flex-grow: 1;">
                        <div style="display: flex; gap: 15px; align-items: center;">
                            <span style="font-size: 2.2rem; font-weight: 800; line-height: 1;">{num}</span>
                            <span style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase; line-height: 1.2;">{title}</span>
                        </div>
                        <i class="fas {icon}" style="font-size: 2rem; opacity: 0.9;"></i>
                    </div>
                </div>''')

html_grid.append(f'''
                <div class="sdg-card" style="background: white; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px; min-height: 250px;">
                    <i class="fas fa-globe" style="font-size: 3.5rem; color: #00A9E0; margin-bottom: 15px;"></i>
                    <h3 style="color: #00A9E0; font-weight: 800; font-size: 1.2rem; text-align: center; text-transform: uppercase; line-height: 1.2;">Sustainable<br>Development<br>Goals</h3>
                </div>''')

grid_str = ''.join(html_grid)

new_section = f'''    <section class="sdg-gallery-section" style="padding: 80px 0; background: #f8f9fa;">
        <div class="container-fluid" style="max-width: 1600px; padding: 0 30px;">
            <h2 style="text-align: center; color: #0D47A1; font-size: 2.5rem; margin-bottom: 50px;">United Nations Sustainable Development Goals (SDGs)</h2>
            <div class="sdg-grid">{grid_str}
            </div>
        </div>
    </section>'''

pattern = re.compile(r'<section class="sdg-gallery-section".*?</section>', re.DOTALL)
new_content = pattern.sub(new_section, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Update styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()
css = css.replace('.sdg-grid {\n    display: grid;\n    grid-template-columns: repeat(6, 1fr);\n    gap: 0;\n}', '.sdg-grid {\n    display: grid;\n    grid-template-columns: repeat(6, 1fr);\n    gap: 25px;\n}')
css = css.replace('.sdg-item:hover img', '.sdg-card:hover img')
css = css.replace('.sdg-item', '.sdg-card')
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated to card layout!')
