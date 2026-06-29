import re

with open('partners.html', 'r', encoding='utf-8') as f:
    text = f.read()

corp_html = """
            <h2 style="text-align: center; color: var(--primary-color); margin-bottom: 40px; font-size: 2rem;">Corporate & CSR Partners</h2>
            <div class="partners-grid" style="display:grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap:30px; justify-items:center;">
                <!-- Corporate Logos -->
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/8Apexonignite.jpg" alt="Apexon Ignite" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/BIL.png" alt="BIL" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/9ClianthaResearch.jpg" alt="Cliantha Research" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/7Gulbrandsen.jpg" alt="Gulbrandsen" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/10Jadeblue.jpg" alt="JadeBlue" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/mastek--600.png" alt="Mastek" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/11MegaCommunication.jpg" alt="Mega Communication" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/12MuscleMonk.jpg" alt="MuscleMonk" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/4Nasscom.jpg" alt="Nasscom Foundation" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/packemUT.png" alt="Packem" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/6QXGlobal.jpg" alt="QX Global" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/2SPGlobal.jpg" alt="S&P Global" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/13Shethinfo.jpg" alt="Sheth Info" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/3TTECGlobal.jpg" alt="TTEC" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/UT.png" alt="UT" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/5WelspunFoundation.jpg" alt="Welspun Foundation" style="width:90%; height:90%; object-fit:contain;">
                </div>
            </div>
        </div>
    </section>
"""

start_marker = '<h2 style="text-align: center; color: var(--primary-color); margin-bottom: 40px; font-size: 2rem;">Corporate & CSR Partners</h2>'
end_marker = '</section>'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker, start_idx) + len(end_marker)

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx] + corp_html.strip() + text[end_idx:]
    with open('partners.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Fixed broken HTML for Corporate grid")
else:
    print("Could not find sections")
