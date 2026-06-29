import glob
import re

# 1. Update Navigation Bar in all HTML files
files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to find the nav-links and swap CSR and Donate
    # Look for:
    # <li><a href="donate.html" class="btn-primary" style="color:white !important;">Donate</a></li>
    # (whitespace)
    # <li><a href="csr.html">CSR</a></li>
    
    # Let's just find the CSR link and the Donate link and ensure CSR comes before Donate.
    # The safest way is to find the entire ul block and reconstruct it.
    
    def reorder_nav(match):
        nav_inner = match.group(1)
        # Extract all li tags
        lis = re.findall(r'<li.*?>.*?</li>', nav_inner, flags=re.DOTALL)
        
        # Filter out Donate and CSR
        other_lis = []
        donate_li = None
        csr_li = None
        
        for li in lis:
            if 'donate.html' in li:
                donate_li = li
            elif 'csr.html' in li:
                csr_li = li
            else:
                other_lis.append(li)
                
        # Reconstruct
        new_lis = other_lis.copy()
        if csr_li:
            new_lis.append(csr_li)
        if donate_li:
            new_lis.append(donate_li)
            
        # Join them back with newlines
        return '<ul class="nav-links">\n                ' + '\n                '.join(new_lis) + '\n            </ul>'
        
    new_content = re.sub(r'<ul class="nav-links">(.*?)</ul>', reorder_nav, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

# 2. Rebuild CSR.html to have a header and look much better
# We will read csr.html and parse its content, then rebuild it.

with open('csr.html', 'r', encoding='utf-8') as f:
    csr_content = f.read()

# We need to inject the page-header right after the closing </nav>
if '<section class="page-header">' not in csr_content:
    header_html = """
    <section class="page-header" style="background:var(--primary-color); padding: 180px 0 60px; color: white; text-align: center;">
        <div class="container">
            <h1 style="font-size: 2.5rem; margin-bottom: 10px;">CSR Initiatives</h1>
            <p style="font-size: 1.1rem; opacity: 0.9;">Corporate Social Responsibility</p>
        </div>
    </section>
    """
    csr_content = re.sub(r'(</nav>)', r'\1\n' + header_html, csr_content)

# Let's style the 11 projects into a nice grid
# The projects are currently represented as <h3> followed by <p>
# 1. Anganwadi : Building Strong Foundations
projects_data = [
    ("Anganwadi", "Transforming Anganwadis with Modern Infrastructure in association with ICDS", "fas fa-child"),
    ("Rural Development", "Building Resilient Communities through Holistic Rural Development : Adopt a Village", "fas fa-tractor"),
    ("Education", "Building a Brighter Future : Our Education Initiatives", "fas fa-book-reader"),
    ("Water for Life", "Water Wisdom : Our Holistic Approach to Drinking Water, Conservation & Recharge", "fas fa-tint"),
    ("Women Empowerment", "Breaking Barriers : Empowering Women & Children", "fas fa-female"),
    ("Mission Solar", "Empowering Rural Communities with Solar Energy : SSL , Roof Top Solar & Other Renewable Options", "fas fa-sun"),
    ("Green Gujarat", "Join Our Mission to Combat Climate Change Through Tree Plantation & Agri. Initiatives", "fas fa-tree"),
    ("Sanitation for All", "Sanitation for All: Our Journey Towards a Swachh Bharat (WASH)", "fas fa-toilet"),
    ("Support Nari Gruh", "Renovation of Nari Gruh for rehabilitation of mentally challenged and HIV positive women", "fas fa-home"),
    ("Sports", "A Comprehensive CSR Initiative for Sports Education, Scholarships, and Facilities", "fas fa-running"),
    ("Health & Nutrition", "Fighting Malnutrition: A Corporate Responsibility Project for Providing Access to Nutritious Food and Health", "fas fa-apple-alt")
]

grid_html = '<div class="stats-grid grid-3" style="margin-top: 40px; margin-bottom: 40px;">\n'
for title, desc, icon in projects_data:
    grid_html += f"""
        <div class="stat-card" style="background: #fff; padding: 30px; border-radius: 15px; box-shadow: var(--shadow); text-align: center;">
            <i class="{icon}" style="font-size: 2.5rem; color: var(--secondary-color); margin-bottom: 15px;"></i>
            <h4 style="color: var(--primary-color); font-size: 1.3rem; margin-bottom: 10px;">{title}</h4>
            <p style="color: var(--text-muted); font-size: 1rem; line-height: 1.6;">{desc}</p>
        </div>
    """
grid_html += '</div>\n'

# We'll locate the "1. Anganwadi" h3 and everything up to "What is CSR?" and replace it with the grid.
# Because regex can be tricky with HTML, we'll use a string split approach.
start_marker = "<h3 style='color: var(--primary-color); margin-top: 30px; margin-bottom: 15px;'>1. Anganwadi : Building Strong Foundations</h3>"
end_marker = "<h3 style='color: var(--primary-color); margin-top: 30px; margin-bottom: 15px;'>What is CSR?</h3>"

if start_marker in csr_content and end_marker in csr_content:
    before = csr_content.split(start_marker)[0]
    after = csr_content.split(end_marker)[1]
    
    # We should also replace the title "CSR Initiatives of Gujarat Rajya Gram Vikas Samiti..." 
    # to be a nice section title.
    title_marker = "<h3 style='color: var(--primary-color); margin-top: 30px; margin-bottom: 15px;'>CSR Initiatives of Gujarat Rajya Gram Vikas Samiti in line with Schedule – VII of Companies Act and United Nations Sustainable Development Goals (SDGs)</h3>"
    
    if title_marker in before:
        before = before.replace(title_marker, "<h2 style='text-align: center; color: var(--primary-color); font-size: 2rem; margin-top: 60px;'>CSR Initiatives in line with Schedule VII & SDGs</h2>")
    
    csr_content = before + grid_html + "<h2 style='color: var(--primary-color); margin-top: 60px; margin-bottom: 20px; font-size: 2rem;'>What is CSR?</h2>" + after

with open('csr.html', 'w', encoding='utf-8') as f:
    f.write(csr_content)
    
print("Updated navigation bars and improved CSR page design.")
