import re

sdgs = [
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
    ('12', 'Responsible<br>Consumption', '#BF8B2E', 'fa-recycle'),
    ('13', 'Climate<br>Action', '#3F7E44', 'fa-earth-americas'),
    ('14', 'Life<br>Below Water', '#0A97D9', 'fa-fish'),
    ('15', 'Life<br>on Land', '#56C02B', 'fa-tree'),
    ('16', 'Peace, Justice<br>Strong Institutions', '#00689D', 'fa-scale-balanced'),
    ('17', 'Partnerships<br>for the Goals', '#19486A', 'fa-handshake')
]

html_grid = []
for idx, (num, title, color, icon) in enumerate(sdgs):
    html_grid.append(f'''
                <div class="sdg-item" style="position: relative; aspect-ratio: 1/1; overflow: hidden;">
                    <img src="https://picsum.photos/seed/sdg{num}/400/400" alt="{title.replace('<br>', ' ')}" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease;">
                    <div class="sdg-overlay" style="position: absolute; bottom: 0; left: 0; width: 60%; height: 60%; background: {color}; padding: 10px; color: white; display: flex; flex-direction: column; justify-content: space-between;">
                        <div style="display: flex; gap: 8px; align-items: flex-start;">
                            <span style="font-size: 1.8rem; font-weight: 800; line-height: 1;">{num}</span>
                            <span style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; line-height: 1.1;">{title}</span>
                        </div>
                        <i class="fas {icon}" style="font-size: 2.2rem; align-self: flex-start; margin-left: 5px; opacity: 0.9;"></i>
                    </div>
                </div>''')

# 18th block
html_grid.append(f'''
                <div class="sdg-item" style="background: white; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px; aspect-ratio: 1/1;">
                    <i class="fas fa-globe" style="font-size: 3rem; color: #00A9E0; margin-bottom: 10px;"></i>
                    <h3 style="color: #00A9E0; font-weight: 800; font-size: 1.1rem; text-align: center; text-transform: uppercase; line-height: 1.2;">Sustainable<br>Development<br>Goals</h3>
                </div>''')

grid_str = ''.join(html_grid)

new_section = f'''    <section class="sdg-gallery-section" style="padding: 80px 0; background: #fff;">
        <div class="container-fluid" style="max-width: 1600px; padding: 0 15px;">
            <h2 style="text-align: center; color: #0D47A1; font-size: 2.5rem; margin-bottom: 50px;">United Nations Sustainable Development Goals (SDGs)</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0;">{grid_str}
            </div>
        </div>
    </section>'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# find the old sdg-section and replace it
pattern = re.compile(r'<section class="sdg-section".*?</section>', re.DOTALL)
new_content = pattern.sub(new_section, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Done!')
