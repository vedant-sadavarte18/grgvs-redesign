import os

PAGES = {
    "index.html": {
        "title": "Home",
        "content": """
    <section class="hero" style="background-image: url('./assets/hero_bg.png');">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <span class="hero-subtitle">36 Years Journey of Empowerment</span>
            <h1 class="hero-title">Gujarat Rajya Gram Vikas Samiti</h1>
            <p class="hero-desc">Empowering rural communities through impactful initiatives.</p>
            <div class="hero-buttons">
                <a href="about.html" class="btn-primary">Discover Our Impact</a>
            </div>
        </div>
    </section>
"""
    },
    "about.html": {
        "title": "About Us",
        "content": """
    <section class="page-header">
        <div class="container">
            <h1>About Us & Our Work</h1>
        </div>
    </section>
    <section class="about-page-content" style="padding:60px 0;">
        <div class="container">
            <div class="content-block">
                <h2>About Us</h2>
                <p>Gujarat Rajya Gram Vikas Samiti is dedicated to uplifting the underprivileged sectors of society. For over three decades, we have been working tirelessly at the grassroots level to bring sustainable change in Gujarat.</p>
            </div>
            <div class="content-block" style="margin-top:40px;">
                <h2>Our Work (CSR)</h2>
                <p>We are a trusted partner for CSR initiatives with FCRA, CSR 1, 12AA, and 80G certifications. We focus on transparent implementation and measurable impact.</p>
            </div>
            <div class="content-block" style="margin-top:40px;">
                <h2>Volunteers' Data</h2>
                <div class="stats-grid" style="margin-top:20px;">
                    <div class="stat-card" style="background:var(--primary-color);color:#fff;padding:20px;border-radius:10px;">
                        <h3 class="counter" data-target="5000">0</h3>
                        <p>Active Volunteers</p>
                    </div>
                    <div class="stat-card" style="background:var(--primary-color);color:#fff;padding:20px;border-radius:10px;">
                        <h3 class="counter" data-target="120000">0</h3>
                        <p>Volunteer Hours</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
    },
    "goals.html": {
        "title": "Our Goals",
        "content": """
    <section class="page-header">
        <div class="container">
            <h1>Our Goals</h1>
            <p>10 Targeted Initiatives for Sustainable Development</p>
        </div>
    </section>
    <section class="goals-list" style="padding:60px 0;">
        <div class="container">
            <div class="projects-grid">
                <!-- We will generate the 10 goal cards here -->
                [[GOAL_CARDS]]
            </div>
        </div>
    </section>
"""
    },
    "impact.html": {
        "title": "Plant Data",
        "content": """
    <section class="page-header">
        <div class="container">
            <h1>Plant Data & Survival Rate</h1>
        </div>
    </section>
    <section class="impact-content" style="padding:60px 0;">
        <div class="container">
            <div class="content-block">
                <h2>Our Plantation Impact</h2>
                <p>We closely monitor the species planted and their survival rates to ensure long-term environmental sustainability.</p>
                
                <table class="data-table" style="width:100%; margin-top:30px; border-collapse:collapse; text-align:left;">
                    <thead style="background:var(--primary-color); color:white;">
                        <tr>
                            <th style="padding:15px;">Species Name</th>
                            <th style="padding:15px;">Total Planted</th>
                            <th style="padding:15px;">Survival Rate</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom:1px solid #eee;"><td style="padding:15px;">Neem (Azadirachta indica)</td><td style="padding:15px;">5,000</td><td style="padding:15px;">88%</td></tr>
                        <tr style="border-bottom:1px solid #eee;"><td style="padding:15px;">Peepal (Ficus religiosa)</td><td style="padding:15px;">3,500</td><td style="padding:15px;">85%</td></tr>
                        <tr style="border-bottom:1px solid #eee;"><td style="padding:15px;">Banyan (Ficus benghalensis)</td><td style="padding:15px;">2,000</td><td style="padding:15px;">90%</td></tr>
                        <tr style="border-bottom:1px solid #eee;"><td style="padding:15px;">Mango (Mangifera indica)</td><td style="padding:15px;">4,500</td><td style="padding:15px;">82%</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>
"""
    },
    "partners.html": {
        "title": "Partners",
        "content": """
    <section class="page-header">
        <div class="container">
            <h1>Partnership Data & Logos</h1>
        </div>
    </section>
    <section class="partners-content" style="padding:60px 0;">
        <div class="container">
            <p style="text-align:center;margin-bottom:40px;font-size:1.2rem;">We are proud to collaborate with leading organizations to maximize our CSR impact.</p>
            <div class="partners-grid" style="display:flex; flex-wrap:wrap; gap:30px; justify-content:center;">
                <div class="partner-logo" style="width:200px; height:100px; background:#eee; display:flex; align-items:center; justify-content:center; border-radius:10px; font-weight:bold; color:#888;">Partner Logo 1</div>
                <div class="partner-logo" style="width:200px; height:100px; background:#eee; display:flex; align-items:center; justify-content:center; border-radius:10px; font-weight:bold; color:#888;">Partner Logo 2</div>
                <div class="partner-logo" style="width:200px; height:100px; background:#eee; display:flex; align-items:center; justify-content:center; border-radius:10px; font-weight:bold; color:#888;">Partner Logo 3</div>
                <div class="partner-logo" style="width:200px; height:100px; background:#eee; display:flex; align-items:center; justify-content:center; border-radius:10px; font-weight:bold; color:#888;">Partner Logo 4</div>
            </div>
        </div>
    </section>
"""
    },
    "contact.html": {
        "title": "Contact Us",
        "content": """
    <section class="page-header">
        <div class="container">
            <h1>Contact & Locations</h1>
        </div>
    </section>
    <section class="contact-content" style="padding:60px 0;">
        <div class="container" style="display:flex; flex-wrap:wrap; gap:40px;">
            <div class="content-block" style="flex:1; min-width:300px;">
                <h2>Contact Details</h2>
                <div style="margin-top:20px; display:flex; flex-direction:column; gap:15px; font-size:1.1rem;">
                    <p><i class="fas fa-envelope" style="color:var(--primary-color);width:30px;"></i> info@gujaratgramvikas.org</p>
                    <p><i class="fas fa-phone" style="color:var(--primary-color);width:30px;"></i> +91 98254 57786</p>
                </div>
                
                <h2 style="margin-top:40px;">Social Media Links</h2>
                <div class="social-links" style="margin-top:20px;">
                    <a href="#" style="background:var(--primary-color);"><i class="fab fa-facebook-f"></i></a>
                    <a href="#" style="background:var(--primary-color);"><i class="fab fa-twitter"></i></a>
                    <a href="#" style="background:var(--primary-color);"><i class="fab fa-instagram"></i></a>
                    <a href="#" style="background:var(--primary-color);"><i class="fab fa-linkedin-in"></i></a>
                </div>
            </div>
            <div class="content-block" style="flex:1; min-width:300px; background:#fff; padding:30px; border-radius:15px; box-shadow:var(--shadow);">
                <h2>Addresses & Sites</h2>
                <ul style="list-style:none; margin-top:20px;">
                    <li style="margin-bottom:20px;">
                        <strong><i class="fas fa-map-marker-alt" style="color:var(--secondary-color);"></i> Head Office</strong><br>
                        123 Main Street, Ahmedabad, Gujarat, 380001
                    </li>
                    <li style="margin-bottom:20px;">
                        <strong><i class="fas fa-map-marker-alt" style="color:var(--secondary-color);"></i> Site 1 (Plantation Project)</strong><br>
                        Village XYZ, District ABC, Gujarat
                    </li>
                    <li style="margin-bottom:20px;">
                        <strong><i class="fas fa-map-marker-alt" style="color:var(--secondary-color);"></i> Site 2 (Community Shelter)</strong><br>
                        Village LMN, District PQR, Gujarat
                    </li>
                </ul>
            </div>
        </div>
    </section>
"""
    },
    "donate.html": {
        "title": "Donate",
        "content": """
    <section class="page-header">
        <div class="container">
            <h1>Donate Tab / Details</h1>
        </div>
    </section>
    <section class="donate-content" style="padding:60px 0;">
        <div class="container">
            <div class="content-block" style="text-align:center; max-width:700px; margin:0 auto;">
                <h2>Support Our Cause</h2>
                <p style="font-size:1.1rem; color:var(--text-muted);">Your contribution helps us plant more trees, build shelters, and support Anganwadis. We accept CSR funds and individual donations.</p>
                <div style="background:#fff; padding:40px; border-radius:15px; margin-top:40px; box-shadow:var(--shadow); text-align:left;">
                    <h3 style="color:var(--primary-color); border-bottom:2px solid var(--secondary-color); padding-bottom:10px; margin-bottom:20px;">Bank Transfer Details</h3>
                    <p style="margin-bottom:10px; font-size:1.1rem;"><strong>Bank Name:</strong> State Bank of India</p>
                    <p style="margin-bottom:10px; font-size:1.1rem;"><strong>Account Name:</strong> Gujarat Rajya Gram Vikas Samiti</p>
                    <p style="margin-bottom:10px; font-size:1.1rem;"><strong>Account Number:</strong> XXXXXXXXXX</p>
                    <p style="margin-bottom:10px; font-size:1.1rem;"><strong>IFSC Code:</strong> SBIN000XXXX</p>
                    
                    <div style="margin-top:30px; text-align:center;">
                        <a href="contact.html" class="btn-primary">Contact us for Tax Exemption Receipts (80G)</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
    }
}

GOALS = [
    "Plantation Drives", "Anganwadi Development", "Community Shelters", 
    "Women Empowerment", "Rural Healthcare", "Clean Water Access", 
    "Education Support", "Sustainable Agriculture", "Youth Skill Development", "Disaster Relief"
]

goal_cards_html = ""
for i, goal in enumerate(GOALS, 1):
    goal_cards_html += f'''
        <div class="project-card">
            <div class="project-info">
                <h3>Goal {i}: {goal}</h3>
                <p>Initiatives and milestones for {goal.lower()}. Photos and specific data will be populated here later.</p>
                <a href="goal-{i}.html" class="read-more">View Details <i class="fas fa-arrow-right"></i></a>
            </div>
        </div>
'''
    
    PAGES[f"goal-{i}.html"] = {
        "title": f"Goal {i} - {goal}",
        "content": f'''
    <section class="page-header">
        <div class="container">
            <h1>Goal {i}: {goal}</h1>
        </div>
    </section>
    <section class="goal-detail-content" style="padding:60px 0;">
        <div class="container">
            <div class="content-block" style="background:#fff; padding:40px; border-radius:15px; box-shadow:var(--shadow);">
                <h2>Overview & Photos</h2>
                <p style="font-size:1.1rem; color:var(--text-muted);">This tab is dedicated to our CSR and implementation details for <strong>{goal}</strong>. As requested, photos and specific data for this goal will be inserted here when provided.</p>
                <div style="margin-top:30px; display:flex; gap:20px; flex-wrap:wrap;">
                    <div style="width:200px; height:150px; background:#e0e0e0; border-radius:10px; display:flex; align-items:center; justify-content:center; color:#666;">Photo Placeholder 1</div>
                    <div style="width:200px; height:150px; background:#e0e0e0; border-radius:10px; display:flex; align-items:center; justify-content:center; color:#666;">Photo Placeholder 2</div>
                </div>
                <div style="margin-top:40px;">
                    <a href="goals.html" class="btn-secondary" style="color:var(--primary-color); border-color:var(--primary-color);">&larr; Back to All Goals</a>
                </div>
            </div>
        </div>
    </section>
'''
    }

PAGES["goals.html"]["content"] = PAGES["goals.html"]["content"].replace("[[GOAL_CARDS]]", goal_cards_html)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GRGVS | {title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
</head>
<body class="inner-page">
    <!-- Navbar -->
    <nav class="navbar scrolled">
        <div class="nav-container">
            <a href="index.html" class="logo">
                <span class="logo-text">GRGVS</span>
            </a>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="about.html">About & Work</a></li>
                <li><a href="goals.html">10 Goals</a></li>
                <li><a href="impact.html">Plant Data</a></li>
                <li><a href="partners.html">Partners</a></li>
                <li><a href="contact.html">Contact</a></li>
                <li><a href="donate.html" class="btn-primary" style="color:white !important;">Donate</a></li>
            </ul>
            <div class="hamburger">
                <i class="fas fa-bars"></i>
            </div>
        </div>
    </nav>

    {content}

    <!-- Contact Us Icon -->
    <a href="contact.html" class="floating-contact">
        <i class="fas fa-comment-dots"></i>
    </a>

    <!-- Footer -->
    <footer style="margin-top:auto;">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-about">
                    <h3>GRGVS</h3>
                    <div class="social-links">
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-twitter"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
                <div class="footer-links">
                    <h3>Quick Links</h3>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="goals.html">Our Goals</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Gujarat Rajya Gram Vikas Samiti.</p>
            </div>
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>"""

for filename, data in PAGES.items():
    with open(f"C:/Users/HP/.gemini/antigravity/scratch/grgvs-redesign/{filename}", "w", encoding="utf-8") as f:
        html = TEMPLATE.format(title=data["title"], content=data["content"])
        if filename == "index.html":
            html = html.replace('class="navbar scrolled"', 'class="navbar"')
            html = html.replace('<body class="inner-page">', '<body>')
        f.write(html)

print("Generated all HTML files successfully.")
