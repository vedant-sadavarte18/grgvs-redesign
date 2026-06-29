import re

with open('partners.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<h2 style="text-align: center; color: var(--primary-color); margin-bottom: 40px; font-size: 2rem;">Corporate & CSR Partners</h2>'
end_marker = '</section>'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    # Look for the grid container inside
    grid_start_idx = text.find('<div class="partners-grid"', start_idx, end_idx)
    grid_end_idx = text.rfind('</div>', grid_start_idx, end_idx) # Inner </div> before section closes, wait actually the grid closes and then container closes.
    
    # We can just split on <div class="partner-card"
    grid_content = text[grid_start_idx:end_idx]
    
    cards = grid_content.split('<div class="partner-card"')
    
    prefix = cards[0]
    cards = cards[1:]
    
    # map cards by filename
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

    # Alphabetical order based on company names
    # Apexon, Bulk Corp (BIL), Cliantha, Gulbrandsen, JadeBlue, Mastek, Mega Communication, MuscleMonk, Nasscom, QX, S&P, Sheth, TTEC, UT (Umasree), Welspun
    new_order = ['Apexon', 'BIL', 'Cliantha', 'Gulbrandsen', 'JadeBlue', 'Mastek', 'Mega', 'MuscleMonk', 'Nasscom', 'QX', 'SP', 'Sheth', 'TTEC', 'UT', 'Welspun']
    
    new_grid = prefix + ''.join(['<div class="partner-card"' + order[k] for k in new_order])
    
    new_text = text[:grid_start_idx] + new_grid + text[end_idx:]
    
    with open('partners.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Corporate partners sorted alphabetically.")
else:
    print("Could not find section.")

