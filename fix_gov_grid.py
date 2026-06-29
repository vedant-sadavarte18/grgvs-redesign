import re

with open('partners.html', 'r', encoding='utf-8') as f:
    text = f.read()

# We need to cleanly regenerate the Gov Partners section to fix the broken HTML tags.
gov_html = """
            <h2 style="text-align: center; color: var(--primary-color); margin-bottom: 40px; font-size: 2rem;">Government & Civic Partners</h2>
            <div class="partners-grid" style="display:grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap:30px; justify-items:center; margin-bottom: 60px;">
                <!-- Gov Logos -->
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/3GOG.jpg" alt="Government of Gujarat" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/1AMC.jpg" alt="Ahmedabad Municipal Corporation" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/5GCCI.jpg" alt="GCCI" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/DRDA.jpg" alt="DRDA" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/9NARMADA.jpg" alt="Narmada" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/6WCD.jpg" alt="WCD" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/WASMO.jpg" alt="WASMO" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/2ICDS.jpg" alt="ICDS" style="width:90%; height:90%; object-fit:contain;">
                </div>
                <div class="partner-card" style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/4NABARD.jpg" alt="NABARD" style="width:90%; height:90%; object-fit:contain;">
                </div>
            </div>
"""

start_marker = '<h2 style="text-align: center; color: var(--primary-color); margin-bottom: 40px; font-size: 2rem;">Government & Civic Partners</h2>'
end_marker = '<h2 style="text-align: center; color: var(--primary-color); margin-bottom: 40px; font-size: 2rem;">Corporate & CSR Partners</h2>'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx] + gov_html.strip() + '\n\n            ' + text[end_idx:]
    with open('partners.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Fixed broken HTML")
else:
    print("Could not find sections")

