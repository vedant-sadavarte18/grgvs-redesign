import re

new_content = """<section class="goal-detail-content" style="padding:60px 0;">
    <div class="container">
        <div style="max-width: 1100px; margin: 0 auto; display: flex; flex-direction: column; gap: 40px;">
            
            <!-- Intro & Targets -->
            <div class="content-block" style="background:#fff; padding:40px; border-radius:15px; box-shadow:var(--shadow);">
                <h1 style="color:var(--primary-color); margin-bottom: 20px; font-size: 2.5rem; text-align: center;">Lakshya: 100 Lakh Trees by 2030</h1>
                <h2 style="color:var(--text-dark); margin-bottom: 30px; font-size: 1.5rem; text-align: center; font-weight: 500;">High-Density Tree Plantation for Ecology Restoration & Biodiversity Enhancement</h2>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 40px;">
                    <div style="background: var(--light-bg); padding: 25px; border-radius: 10px; text-align: center; border-left: 4px solid var(--secondary-color);">
                        <h3 style="font-size: 1.8rem; color: var(--primary-color); margin-bottom: 10px;">100 Lakh</h3>
                        <p style="color: var(--text-muted); font-size: 1.1rem;">Trees Across Gujarat by 2030</p>
                    </div>
                    <div style="background: var(--light-bg); padding: 25px; border-radius: 10px; text-align: center; border-left: 4px solid var(--secondary-color);">
                        <h3 style="font-size: 1.8rem; color: var(--primary-color); margin-bottom: 10px;">10 Lakh</h3>
                        <p style="color: var(--text-muted); font-size: 1.1rem;">Trees in Gandhinagar Lok Sabha</p>
                    </div>
                    <div style="background: var(--light-bg); padding: 25px; border-radius: 10px; text-align: center; border-left: 4px solid var(--secondary-color);">
                        <h3 style="font-size: 1.8rem; color: var(--primary-color); margin-bottom: 10px;">95%</h3>
                        <p style="color: var(--text-muted); font-size: 1.1rem;">Survival Rate Guaranteed</p>
                    </div>
                    <div style="background: var(--light-bg); padding: 25px; border-radius: 10px; text-align: center; border-left: 4px solid var(--secondary-color);">
                        <h3 style="font-size: 1.8rem; color: var(--primary-color); margin-bottom: 10px;">50 Hectares</h3>
                        <p style="color: var(--text-muted); font-size: 1.1rem;">Land Secured Already</p>
                    </div>
                </div>
                
                <div style="margin-top: 40px; background: rgba(44, 95, 45, 0.05); padding: 30px; border-radius: 10px; text-align: center;">
                    <h3 style="color:var(--primary-color); margin-bottom: 15px; font-size: 1.5rem;">5 Pillars of Focus</h3>
                    <p style="font-size: 1.2rem; color: var(--text-dark); font-weight: 600;">Ecology &bull; Biodiversity &bull; Climate &bull; Water &bull; Employment</p>
                </div>
            </div>

            <!-- Objective & Expected Outcome -->
            <div class="content-block" style="background:#fff; padding:40px; border-radius:15px; box-shadow:var(--shadow);">
                <h2 style="color:var(--primary-color); margin-bottom: 30px; font-size: 2rem;">Objective and Expected Outcome</h2>
                <ul style="font-size:1.1rem; color:var(--text-muted); margin-left: 20px; line-height: 1.8; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; list-style-type: none; padding: 0;">
                    <li><i class="fas fa-check" style="color: var(--secondary-color); margin-right: 10px;"></i> Enhance biodiversity using 30+ native species</li>
                    <li><i class="fas fa-check" style="color: var(--secondary-color); margin-right: 10px;"></i> Functional habitats for birds, pollinators & small mammals</li>
                    <li><i class="fas fa-check" style="color: var(--secondary-color); margin-right: 10px;"></i> Improve air quality</li>
                    <li><i class="fas fa-check" style="color: var(--secondary-color); margin-right: 10px;"></i> Sequester carbon dioxide</li>
                    <li><i class="fas fa-check" style="color: var(--secondary-color); margin-right: 10px;"></i> Noise pollution filtration</li>
                    <li><i class="fas fa-check" style="color: var(--secondary-color); margin-right: 10px;"></i> Employee Engagement</li>
                    <li><i class="fas fa-check" style="color: var(--secondary-color); margin-right: 10px;"></i> Community Participation in plantation drives</li>
                    <li><i class="fas fa-check" style="color: var(--secondary-color); margin-right: 10px;"></i> Reduce urban heat island effect</li>
                </ul>
            </div>

            <!-- Project Impact -->
            <div class="content-block" style="background:#fff; padding:40px; border-radius:15px; box-shadow:var(--shadow);">
                <h2 style="color:var(--primary-color); margin-bottom: 30px; font-size: 2rem;">Project Impact</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 25px;">
                    <div style="padding: 20px; border: 1px solid #eee; border-radius: 10px; text-align: center;">
                        <i class="fas fa-leaf" style="font-size: 2rem; color: var(--secondary-color); margin-bottom: 15px;"></i>
                        <h4 style="font-size: 1.2rem; color: var(--text-dark); margin-bottom: 10px;">Biodiversity & Habitats</h4>
                        <p style="color: var(--text-muted); font-size: 1rem;">Restoration & habitat creation for native flora & fauna</p>
                    </div>
                    <div style="padding: 20px; border: 1px solid #eee; border-radius: 10px; text-align: center;">
                        <i class="fas fa-users" style="font-size: 2rem; color: var(--secondary-color); margin-bottom: 15px;"></i>
                        <h4 style="font-size: 1.2rem; color: var(--text-dark); margin-bottom: 10px;">Community & Employment</h4>
                        <p style="color: var(--text-muted); font-size: 1rem;">Awareness, volunteering & green employment</p>
                    </div>
                    <div style="padding: 20px; border: 1px solid #eee; border-radius: 10px; text-align: center;">
                        <i class="fas fa-wind" style="font-size: 2rem; color: var(--secondary-color); margin-bottom: 15px;"></i>
                        <h4 style="font-size: 1.2rem; color: var(--text-dark); margin-bottom: 10px;">Air Quality & Climate</h4>
                        <p style="color: var(--text-muted); font-size: 1rem;">Improved air quality & reduced urban heat island effect</p>
                    </div>
                    <div style="padding: 20px; border: 1px solid #eee; border-radius: 10px; text-align: center;">
                        <i class="fas fa-water" style="font-size: 2rem; color: var(--secondary-color); margin-bottom: 15px;"></i>
                        <h4 style="font-size: 1.2rem; color: var(--text-dark); margin-bottom: 10px;">Water & Carbon</h4>
                        <p style="color: var(--text-muted); font-size: 1rem;">Groundwater recharge & long-term carbon sequestration</p>
                    </div>
                </div>
            </div>

            <!-- Jivamrut & Miyawaki Method -->
            <div class="content-block" style="background:#fff; padding:40px; border-radius:15px; box-shadow:var(--shadow);">
                <h2 style="color:var(--primary-color); margin-bottom: 20px; font-size: 2rem;">Our Methodology</h2>
                
                <h3 style="color:var(--text-dark); margin-bottom: 15px; font-size: 1.5rem; margin-top: 30px;">The Miyawaki Method</h3>
                <p style="font-size:1.1rem; color:var(--text-muted); margin-bottom: 20px; line-height: 1.8;">The Miyawaki Method, developed by Japanese botanist Akira Miyawaki, is an innovative approach to forest creation. This method involves planting dense clusters of native species, which grow quickly and form a self-sustaining ecosystem within a few years.</p>
                <ul style="font-size:1.1rem; color:var(--text-muted); margin-left: 20px; margin-bottom: 40px; line-height: 1.8;">
                    <li>Rapid growth of trees</li>
                    <li>High biodiversity</li>
                    <li>Low maintenance once established</li>
                    <li>Enhanced ecosystem services such as air purification and temperature regulation</li>
                </ul>

                <h3 style="color:var(--text-dark); margin-bottom: 15px; font-size: 1.5rem;">Jivamrut: Life-giving medicine for soil microbes</h3>
                <p style="font-size:1.1rem; color:var(--text-muted); margin-bottom: 20px; line-height: 1.8;">A potent, 100% natural liquid bio-fertilizer and soil conditioner used in organic farming to enhance soil fertility and stimulate plant growth. Made from Jaggery, Gram Flour, Forest soil, Water, Cow Dung, and Gomutra.</p>
                <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                    <span style="background: var(--primary-color); color: white; padding: 8px 15px; border-radius: 20px; font-size: 0.95rem;">Enriches Soil Microbiome</span>
                    <span style="background: var(--primary-color); color: white; padding: 8px 15px; border-radius: 20px; font-size: 0.95rem;">Zero Chemical Input</span>
                    <span style="background: var(--primary-color); color: white; padding: 8px 15px; border-radius: 20px; font-size: 0.95rem;">Boosts Plant Immunity</span>
                    <span style="background: var(--primary-color); color: white; padding: 8px 15px; border-radius: 20px; font-size: 0.95rem;">Supports Life Below Earth</span>
                </div>
            </div>

            <!-- Project Plan -->
            <div class="content-block" style="background:#fff; padding:40px; border-radius:15px; box-shadow:var(--shadow);">
                <h2 style="color:var(--primary-color); margin-bottom: 30px; font-size: 2rem;">Project Plan for Dense Afforestation</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                    <div style="background: var(--light-bg); padding: 25px; border-radius: 10px;">
                        <h3 style="color: var(--primary-color); margin-bottom: 15px; font-size: 1.3rem;">1st Year – Plantation</h3>
                        <ul style="font-size:1rem; color:var(--text-muted); margin-left: 20px; line-height: 1.6;">
                            <li>Soil Preparation / Manure</li>
                            <li>Water Arrangement (Borewell / Tanker)</li>
                            <li>Electrical Connection & Electricity Bill</li>
                            <li>Hole Digging & Sapling Procurement</li>
                            <li>Labour — Piping & Supervisor</li>
                            <li>Small Water Body for Biodiversity</li>
                            <li>Natural Pathways for Forest Bath</li>
                        </ul>
                    </div>
                    <div style="background: var(--light-bg); padding: 25px; border-radius: 10px;">
                        <h3 style="color: var(--primary-color); margin-bottom: 15px; font-size: 1.3rem;">1st Year – Maintenance</h3>
                        <ul style="font-size:1rem; color:var(--text-muted); margin-left: 20px; line-height: 1.6;">
                            <li>Jeevamrut Application & De-weeding</li>
                            <li>Regular Labour, Security / Mali & Supervisor</li>
                            <li>Non-surviving species replaced at no cost</li>
                            <li>Quarterly Photographic Reporting</li>
                        </ul>
                    </div>
                    <div style="background: var(--light-bg); padding: 25px; border-radius: 10px;">
                        <h3 style="color: var(--primary-color); margin-bottom: 15px; font-size: 1.3rem;">2nd Year – Maintenance</h3>
                        <ul style="font-size:1rem; color:var(--text-muted); margin-left: 20px; line-height: 1.6;">
                            <li>De-weeding & Regular Labour</li>
                            <li>Security / Mali & Supervisor</li>
                            <li>Quarterly Photographic Reporting</li>
                        </ul>
                    </div>
                    <div style="background: var(--light-bg); padding: 25px; border-radius: 10px;">
                        <h3 style="color: var(--primary-color); margin-bottom: 15px; font-size: 1.3rem;">3rd Year – Maintenance</h3>
                        <ul style="font-size:1rem; color:var(--text-muted); margin-left: 20px; line-height: 1.6;">
                            <li>De-weeding & Regular Labour</li>
                            <li>Security / Mali & Supervisor</li>
                            <li>Quarterly Photographic Reporting</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Locations Identified -->
            <div class="content-block" style="background:#fff; padding:40px; border-radius:15px; box-shadow:var(--shadow);">
                <h2 style="color:var(--primary-color); margin-bottom: 30px; font-size: 2rem;">Locations Identified for Plantation</h2>
                <div style="overflow-x: auto;">
                    <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 1.1rem;">
                        <thead>
                            <tr style="background: var(--primary-color); color: white;">
                                <th style="padding: 15px;">Sr. No.</th>
                                <th style="padding: 15px;">Name of village</th>
                                <th style="padding: 15px;">Block & District</th>
                                <th style="padding: 15px;">Land ownership</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid #eee;">
                                <td style="padding: 15px;">1</td><td style="padding: 15px;">Classic highland</td><td style="padding: 15px;">Ahmedabad City</td><td style="padding: 15px;">AMC</td>
                            </tr>
                            <tr style="background: #f9f9f9; border-bottom: 1px solid #eee;">
                                <td style="padding: 15px;">2</td><td style="padding: 15px;">Sandesh bunglow</td><td style="padding: 15px;">Ahmedabad City</td><td style="padding: 15px;">AMC</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #eee;">
                                <td style="padding: 15px;">3</td><td style="padding: 15px;">Sabaspur</td><td style="padding: 15px;">Kalol Gandhinagar</td><td style="padding: 15px;">GDA</td>
                            </tr>
                            <tr style="background: #f9f9f9; border-bottom: 1px solid #eee;">
                                <td style="padding: 15px;">4</td><td style="padding: 15px;">Usmanabad</td><td style="padding: 15px;">Kalol Gandhinagar</td><td style="padding: 15px;">GDA</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #eee;">
                                <td style="padding: 15px;">5</td><td style="padding: 15px;">Naroda</td><td style="padding: 15px;">Ahmedabad City</td><td style="padding: 15px;">AUDA</td>
                            </tr>
                            <tr style="background: #f9f9f9; border-bottom: 1px solid #eee;">
                                <td style="padding: 15px;">6</td><td style="padding: 15px;">Aslali</td><td style="padding: 15px;">Daskroi, Ahmedabad</td><td style="padding: 15px;">AUDA</td>
                            </tr>
                            <tr style="border-bottom: 1px solid #eee;">
                                <td style="padding: 15px;">7</td><td style="padding: 15px;">Apoorva bunglow</td><td style="padding: 15px;">Ahmedabad City</td><td style="padding: 15px;">AMC</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <p style="color: var(--text-muted); font-size: 0.95rem; margin-top: 15px;">AMC – Ahmedabad Municipal Corporation | GDA – Gandhinagar District Administration/Collector | AUDA – Ahmedabad Urban Development Authority</p>
            </div>

            <!-- Compliance & Reporting & Partners -->
            <div class="content-block" style="background:#fff; padding:40px; border-radius:15px; box-shadow:var(--shadow);">
                <h2 style="color:var(--primary-color); margin-bottom: 30px; font-size: 2rem;">Compliance, Reporting & Partners</h2>
                
                <div style="display: flex; gap: 20px; flex-wrap: wrap; margin-bottom: 40px;">
                    <div style="flex: 1; min-width: 200px; padding: 20px; background: #e8f5e9; border-radius: 10px; text-align: center;">
                        <strong>CSR Schedule VII</strong><br>Fully aligned
                    </div>
                    <div style="flex: 1; min-width: 200px; padding: 20px; background: #e8f5e9; border-radius: 10px; text-align: center;">
                        <strong>ESG Standards</strong><br>Audit-ready docs
                    </div>
                    <div style="flex: 1; min-width: 200px; padding: 20px; background: #e8f5e9; border-radius: 10px; text-align: center;">
                        <strong>UN SDGs 11,13,15</strong><br>Documented impact
                    </div>
                    <div style="flex: 1; min-width: 200px; padding: 20px; background: #e8f5e9; border-radius: 10px; text-align: center;">
                        <strong>FCRA Registered</strong><br>International ready
                    </div>
                </div>

                <div style="background: var(--light-bg); padding: 20px; border-radius: 10px; text-align: center; margin-bottom: 40px;">
                    <p style="font-size: 1.1rem; color: var(--text-dark); margin: 0; line-height: 1.8;"><strong>Public Trust:</strong> F/308/1988 &nbsp;|&nbsp; <strong>PAN:</strong> AAATG3254G &nbsp;|&nbsp; <strong>Income Tax:</strong> 80G & 12A &nbsp;|&nbsp; <strong>CSR1:</strong> CSR 00014330 &nbsp;|&nbsp; <strong>FCRA Reg. No.:</strong> 041910403</p>
                </div>

                <h3 style="color:var(--text-dark); margin-top: 20px; margin-bottom: 20px; font-size: 1.5rem;">Visibility and Recognition for Partners</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; text-align: center; margin-bottom: 40px;">
                    <div style="padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
                        <i class="fas fa-bullhorn" style="font-size: 2rem; color: var(--secondary-color); margin-bottom: 10px;"></i>
                        <h4 style="margin-bottom: 10px;">Media Recognition</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">Recognition in media and social platforms reaching broad audiences</p>
                    </div>
                    <div style="padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
                        <i class="fas fa-sign" style="font-size: 2rem; color: var(--secondary-color); margin-bottom: 10px;"></i>
                        <h4 style="margin-bottom: 10px;">Branding Board</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">Company logo, trees planted, locations & year displayed prominently on-site</p>
                    </div>
                    <div style="padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
                        <i class="fas fa-hands-helping" style="font-size: 2rem; color: var(--secondary-color); margin-bottom: 10px;"></i>
                        <h4 style="margin-bottom: 10px;">Events & Volunteering</h4>
                        <p style="color: var(--text-muted); font-size: 0.95rem;">Invitations to plantation events & CSR volunteering drives</p>
                    </div>
                </div>

                <h3 style="color:var(--text-dark); margin-bottom: 20px; font-size: 1.5rem;">Trusted Corporate Partners & Supporters</h3>
                <p style="font-size: 1.1rem; color: var(--text-muted); line-height: 1.8;">Adani Green Energy, ONGC, TTEC India Foundation, S&P Global, Bank of America, Mastek Foundation, NISSIN ABC Logistics, Light Finance, HDB Financial Services, Rexroth Bosch, Fortune, CII, NSIC, Commerce Pundit, Young India, Priority.</p>
            </div>

            <!-- 37+ Years of Impact -->
            <div class="content-block" style="background:#fff; padding:40px; border-radius:15px; box-shadow:var(--shadow); text-align: center;">
                <h2 style="color:var(--primary-color); margin-bottom: 30px; font-size: 2rem;">GRGVS 37+ Years of Impact</h2>
                <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
                    <div style="flex: 1; padding: 20px; background: var(--primary-color); color: white; border-radius: 10px; min-width: 150px;">
                        <h3 style="font-size: 2.5rem; margin-bottom: 10px;">37+</h3>
                        <p>Years in Social & Env. Work</p>
                    </div>
                    <div style="flex: 1; padding: 20px; background: var(--primary-color); color: white; border-radius: 10px; min-width: 150px;">
                        <h3 style="font-size: 2.5rem; margin-bottom: 10px;">20+</h3>
                        <p>Urban Forests Being Developed</p>
                    </div>
                    <div style="flex: 1; padding: 20px; background: var(--primary-color); color: white; border-radius: 10px; min-width: 150px;">
                        <h3 style="font-size: 2.5rem; margin-bottom: 10px;">20,000+</h3>
                        <p>Sanitation Units Built</p>
                    </div>
                    <div style="flex: 1; padding: 20px; background: var(--primary-color); color: white; border-radius: 10px; min-width: 150px;">
                        <h3 style="font-size: 2.5rem; margin-bottom: 10px;">1,000+</h3>
                        <p>Rainwater Harvesting Sites</p>
                    </div>
                    <div style="flex: 1; padding: 20px; background: var(--primary-color); color: white; border-radius: 10px; min-width: 150px;">
                        <h3 style="font-size: 2.5rem; margin-bottom: 10px;">50+</h3>
                        <p>Anganwadi Centres</p>
                    </div>
                </div>
                <p style="margin-top: 30px; font-size: 1.2rem; color: var(--text-dark); font-weight: 600;">Established Since 1988</p>
            </div>

            <!-- Support & Get Involved -->
            <div class="content-block" style="background:#fff; padding:40px; border-radius:15px; box-shadow:var(--shadow);">
                <h2 style="color:var(--primary-color); margin-bottom: 20px; font-size: 2rem;">How You Can Get Involved</h2>
                <ul style="font-size:1.1rem; color:var(--text-muted); margin-left: 20px; margin-bottom: 30px; line-height: 1.8;">
                    <li><strong>Donate:</strong> Your financial support can make a significant impact. Every contribution helps us plant more trees.</li>
                    <li><strong>Volunteer:</strong> Join our community of volunteers and participate in tree planting, maintenance, and awareness campaigns.</li>
                    <li><strong>Corporate Partnerships:</strong> If you represent a company, consider partnering with us for your CSR activities. Together, we can create a greener future.</li>
                </ul>

                <h2 style="color:var(--primary-color); margin-bottom: 30px; margin-top: 50px; font-size: 2rem;">Find Us on the Map</h2>
                <div style="width: 100%; height: 400px; border-radius: 15px; overflow: hidden; border: 1px solid #eee; box-shadow: var(--shadow); margin-bottom: 40px;">
                    <iframe 
                        src="https://maps.google.com/maps?q=Urban%20Forest%201%20-%20Gujarat%20Rajya%20Gram%20Vikas%20Samiti&t=&z=14&ie=UTF8&iwloc=&output=embed" 
                        width="100%" 
                        height="100%" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy" 
                        referrerpolicy="no-referrer-when-downgrade">
                    </iframe>
                </div>

                <div style="margin-top:40px; text-align: center;">
                    <a href="goals.html" class="btn-secondary" style="color:var(--primary-color); border-color:var(--primary-color); padding: 12px 30px; border-radius: 30px; display: inline-block;">&larr; Back to All Goals</a>
                </div>
            </div>

        </div>
    </div>
</section>"""

with open('urban-forest.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace everything from <section class="goal-detail-content" ... to </section> before floating contact
content = re.sub(r'<section class="goal-detail-content" style="padding:60px 0;">.*?</section>\n    <a href="contact.html" class="floating-contact">', 
                 new_content + '\n    <a href="contact.html" class="floating-contact">', 
                 content, flags=re.DOTALL)

with open('urban-forest.html', 'w', encoding='utf-8') as f:
    f.write(content)
