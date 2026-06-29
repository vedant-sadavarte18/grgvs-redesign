import re

with open('csr.html', 'r', encoding='utf-8') as f:
    csr_content = f.read()

goals_data = [
    ("Goal 1: Green Gujarat", "Initiatives and milestones for plantation drives.", "fas fa-tree", "goal-1.html"),
    ("Goal 2: Anganwadi", "Initiatives and milestones for Anganwadi and ICDS.", "fas fa-child", "goal-2.html"),
    ("Goal 3: Rural Development", "Initiatives and milestones for rural development.", "fas fa-tractor", "goal-3.html"),
    ("Goal 4: Women Empowerment", "Initiatives and milestones for women empowerment.", "fas fa-female", "goal-4.html"),
    ("Goal 5: Sanitation for all", "Initiatives and milestones for sanitation.", "fas fa-toilet", "goal-5.html"),
    ("Goal 6: Water Projects", "Initiatives and milestones for water projects.", "fas fa-tint", "goal-6.html"),
    ("Goal 7: Education Support", "Initiatives and milestones for education support.", "fas fa-book-reader", "goal-7.html"),
    ("Goal 8: Solar energy", "Initiatives and milestones for solar energy.", "fas fa-sun", "goal-8.html"),
    ("Goal 9: Nari Gruh", "Initiatives and milestones for Nari Gruh.", "fas fa-home", "goal-9.html"),
    ("Goal 10: Disabled / Elderly", "Initiatives and milestones for disabled and elderly support.", "fas fa-wheelchair", "goal-10.html"),
    ("Goal 11: Disaster Relief", "Initiatives and milestones for disaster relief.", "fas fa-hands-helping", "goal-11.html")
]

grid_html = '<div class="stats-grid grid-3" style="margin-top: 40px; margin-bottom: 40px;">\n'
for title, desc, icon, link in goals_data:
    grid_html += f"""
        <a href="{link}" style="text-decoration: none; display: block; color: inherit;">
            <div class="stat-card" style="background: #fff; padding: 30px; border-radius: 15px; box-shadow: var(--shadow); text-align: center; height: 100%; transition: transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                <i class="{icon}" style="font-size: 2.5rem; color: var(--secondary-color); margin-bottom: 15px;"></i>
                <h4 style="color: var(--primary-color); font-size: 1.3rem; margin-bottom: 10px;">{title}</h4>
                <p style="color: var(--text-muted); font-size: 1rem; line-height: 1.6;">{desc}</p>
            </div>
        </a>
    """
grid_html += '</div>'

# We replace everything between <div class="stats-grid grid-3"...> and </div> that immediately follows it
# Since the grid contains nested divs, we can use regex or string split.
start_marker = '<div class="stats-grid grid-3" style="margin-top: 40px; margin-bottom: 40px;">'
end_marker = '        <div class="stat-card" style="background: #fff; padding: 30px; border-radius: 15px; box-shadow: var(--shadow); text-align: center;">\n            <i class="fas fa-apple-alt"'

# Wait, it's easier to just use regex to match the whole grid block.
# Let's find the start marker and the next <h2 style='color: var(--primary-color); margin-top: 60px; margin-bottom: 20px; font-size: 2rem;'>What is CSR?</h2>
end_section = "<h2 style='color: var(--primary-color); margin-top: 60px; margin-bottom: 20px; font-size: 2rem;'>What is CSR?</h2>"

if start_marker in csr_content and end_section in csr_content:
    before = csr_content.split(start_marker)[0]
    after = end_section + csr_content.split(end_section)[1]
    
    new_csr = before + grid_html + '\n' + after
    
    with open('csr.html', 'w', encoding='utf-8') as f:
        f.write(new_csr)
    print("Successfully replaced grid with 11 goals.")
else:
    print("Could not find markers.")
