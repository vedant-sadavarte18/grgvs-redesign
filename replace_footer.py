import os
import glob
import re

new_footer = """    <footer style="background: var(--dark-bg); color: var(--text-light); padding: 60px 0 20px;">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-about">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                        <img src="./assets/Logo.jpg" alt="GRGVS Logo" style="height: 50px; width: auto; border-radius: 5px; background: white; padding: 2px;">
                        <h3 style="color: white; margin: 0;">GRGVS</h3>
                    </div>
                    <p style="color: #aaa; margin-bottom: 20px;">Empowering rural communities through impactful initiatives since 1988.</p>
                    <p style="color: #aaa; margin-bottom: 20px; line-height: 1.6;">
                        <a href="https://maps.app.goo.gl/5NwYgCD4VFd7RQA37?g_st=iw" target="_blank" style="color: inherit; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--secondary-color)'" onmouseout="this.style.color='inherit'">
                            <i class="fas fa-map-marker-alt" style="color: var(--secondary-color); margin-right: 10px;"></i>
                            <strong>GRGVS NGO (GUJARAT GRAM VIKAS)</strong><br>
                            BLOCK A, Siddhivinayak Business Tower, 508,<br>
                            off Sarkhej - Gandhinagar Highway, Makarba,<br>
                            Ahmedabad, Gujarat 380051
                            <br><span style="color: var(--secondary-color); font-size: 0.9rem; margin-top: 8px; display: inline-block;">Get Directions &rarr;</span>
                        </a>
                    </p>
                </div>
                <div class="footer-links">
                    <h3 style="color: white; margin-bottom: 20px;">Quick Links</h3>
                    <ul style="list-style: none; padding: 0;">
                        <li style="margin-bottom: 10px;"><a href="index.html" style="color: #aaa; text-decoration: none;">Home</a></li>
                        <li style="margin-bottom: 10px;"><a href="about.html" style="color: #aaa; text-decoration: none;">About Us</a></li>
                        <li style="margin-bottom: 10px;"><a href="goals.html" style="color: #aaa; text-decoration: none;">Our Goals</a></li>
                        <li style="margin-bottom: 10px;"><a href="contact.html" style="color: #aaa; text-decoration: none;">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-contact">
                    <h3 style="color: white; margin-bottom: 20px;">Contact Us</h3>
                    <p style="color: #aaa; margin-bottom: 10px;"><i class="fas fa-envelope" style="margin-right: 10px;"></i> info@gujaratgramvikas.org</p>
                    <p style="color: #aaa; margin-bottom: 10px;"><i class="fas fa-phone" style="margin-right: 10px;"></i> +91 98254 57786</p>
                    <div class="social-links" style="margin-top: 25px;">
                        <a href="https://www.linkedin.com/company/gujarat-rajya-gram-vikas-samiti" target="_blank" rel="noopener noreferrer" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                        <a href="https://x.com/gujratgramvikas" target="_blank" rel="noopener noreferrer" title="X (Twitter)"><i class="fa-brands fa-x-twitter"></i></a>
                        <a href="#" target="_blank" rel="noopener noreferrer" title="YouTube"><i class="fab fa-youtube"></i></a>
                        <a href="https://www.facebook.com/gujarat.gram.vikas/" target="_blank" rel="noopener noreferrer" title="Facebook"><i class="fab fa-facebook-f"></i></a>
                        <a href="https://www.instagram.com/gujaratgramvikas" target="_blank" rel="noopener noreferrer" title="Instagram"><i class="fab fa-instagram"></i></a>
                        <a href="https://web.whatsapp.com/send?phone=919825457786&text=Hello!" target="_blank" rel="noopener noreferrer" title="WhatsApp"><i class="fab fa-whatsapp"></i></a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom" style="text-align: center; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); color: #888;">
                <p>&copy; 2026 Gujarat Rajya Gram Vikas Samiti. All Rights Reserved.</p>
            </div>
        </div>
    </footer>"""

html_files = glob.glob('*.html')
pattern = re.compile(r'<footer[\s\S]*?</footer>')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if re.search(pattern, content):
        content = re.sub(pattern, new_footer, content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
            print(f"Updated footer in {f}")
    else:
        print(f"No footer found in {f}")
