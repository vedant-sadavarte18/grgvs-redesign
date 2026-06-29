import re

with open('partners.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<h2 style="text-align: center; color: var(--primary-color); margin-bottom: 40px; font-size: 2rem;">Corporate & CSR Partners</h2>'
end_marker = '</section>'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    grid_start_idx = text.find('<div class="partners-grid"', start_idx, end_idx)
    grid_end_idx = text.rfind('</div>', grid_start_idx, end_idx) 
    
    grid_content = text[grid_start_idx:end_idx]
    
    cards = grid_content.split('<div class="partner-card"')
    
    prefix = cards[0]
    cards = cards[1:]
    
    order = {}
    for c in cards:
        if '2SPGlobal.jpg' in c: order['SP'] = c
        elif '3TTECGlobal.jpg' in c: order['TTEC'] = c
        elif '4Nasscom.jpg' in c: order['Nasscom'] = c
        elif '5WelspunFoundation.jpg' in c: order['Welspun'] = c
        elif '6QXGlobal.jpg' in c: order['QX'] = c
        elif '7Gulbrandsen.jpg' in c: order['Gulbrandsen'] = c
        elif '8Apexonignite.jpg' in c: order['Apexon'] = c
        elif '9ClianthaResearch.jpg' in c: order['Cliantha'] = c
        elif '10Jadeblue.jpg' in c: order['JadeBlue'] = c
        elif '11MegaCommunication.jpg' in c: order['Mega'] = c
        elif '12MuscleMonk.jpg' in c: order['MuscleMonk'] = c
        elif '13Shethinfo.jpg' in c: order['Sheth'] = c
        elif 'mastek--600.png' in c: order['Mastek'] = c
        elif 'BIL.png' in c: order['BIL'] = c
        elif 'UT.png' in c: order['UT'] = c
        elif 'packemUT.png' in c: order['Packem'] = c
        
    if 'Packem' not in order:
        order['Packem'] = """ style="background:#fff; border-radius:15px; padding:5px; box-shadow:0 4px 15px rgba(0,0,0,0.05); display:flex; align-items:center; justify-content:center; width:100%; aspect-ratio: 3/2; transition:transform 0.3s;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                    <img src="./assets/logos/packemUT.png" alt="Packem" style="width:90%; height:90%; object-fit:contain;">
                </div>\n                """

    # Apexon, BIL, Cliantha, Gulbrandsen, JadeBlue, Mastek, Mega Communication, MuscleMonk, Nasscom, Packem, QX, S&P, Sheth, TTEC, UT, Welspun
    new_order = ['Apexon', 'BIL', 'Cliantha', 'Gulbrandsen', 'JadeBlue', 'Mastek', 'Mega', 'MuscleMonk', 'Nasscom', 'Packem', 'QX', 'SP', 'Sheth', 'TTEC', 'UT', 'Welspun']
    
    new_grid = prefix + ''.join(['<div class="partner-card"' + order[k] for k in new_order])
    
    new_text = text[:grid_start_idx] + new_grid + text[end_idx:]
    
    with open('partners.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Added Packem and sorted.")
else:
    print("Could not find section.")

