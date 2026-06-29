import re

html_content = """
    <section class="partners-content" style="padding:60px 0; background: #f8f9fa;">
        <div class="container">
            <p style="text-align:center;margin-bottom:60px;font-size:1.2rem; color: var(--text-muted); max-width: 800px; margin-left: auto; margin-right: auto;">We are proud to collaborate with leading government bodies, civic organizations, and corporate partners to maximize our CSR and community development impact across Gujarat.</p>
            
            <h2 style="text-align: center; color: var(--primary-color); margin-bottom: 40px; font-size: 2rem;">Government & Civic Partners</h2>
            <div class="partners-grid" style="display:grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap:30px; justify-items:center; margin-bottom: 60px;">
                <!-- Gov Logos -->
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/3GOG.jpg" alt="Government of Gujarat" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/1AMC.jpg" alt="Ahmedabad Municipal Corporation" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/2ICDS.jpg" alt="ICDS" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/4NABARD.jpg" alt="NABARD" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/6WCD.jpg" alt="WCD" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/9NARMADA.jpg" alt="Narmada" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/DRDA.jpg" alt="DRDA" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/WASMO.jpg" alt="WASMO" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/5GCCI.jpg" alt="GCCI" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
            </div>

            <h2 style="text-align: center; color: var(--primary-color); margin-bottom: 40px; font-size: 2rem;">Corporate & CSR Partners</h2>
            <div class="partners-grid" style="display:grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap:30px; justify-items:center;">
                <!-- Corporate Logos -->
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/2SPGlobal.jpg" alt="S&P Global" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/3TTECGlobal.jpg" alt="TTEC" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/4Nasscom.jpg" alt="Nasscom Foundation" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/5WelspunFoundation.jpg" alt="Welspun Foundation" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/6QXGlobal.jpg" alt="QX Global" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/7Gulbrandsen.jpg" alt="Gulbrandsen" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/8Apexonignite.jpg" alt="Apexon Ignite" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/9ClianthaResearch.jpg" alt="Cliantha Research" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/10Jadeblue.jpg" alt="JadeBlue" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/11MegaCommunication.jpg" alt="Mega Communication" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/12MuscleMonk.jpg" alt="MuscleMonk" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/13Shethinfo.jpg" alt="Sheth Info" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/mastek--600.png" alt="Mastek" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/BIL.png" alt="BIL" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:20px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/UT.png" alt="UT" style="max-width:100%; max-height:100%; object-fit:contain;">
                </div>
            </div>
        </div>
    </section>
"""

with open('partners.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the entire <section class="partners-content"> block
text = re.sub(r'<section class="partners-content".*?</section>', html_content.strip(), text, flags=re.DOTALL)

with open('partners.html', 'w', encoding='utf-8') as f:
    f.write(text)
