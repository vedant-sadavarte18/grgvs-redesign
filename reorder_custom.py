import re

with open('partners.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<!-- Gov Logos -->'
end_marker = 'Corporate & CSR Partners'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    end_idx = text.rfind('</div>', start_idx, end_idx) 
    end_idx = text.rfind('</div>', start_idx, end_idx) 
    
    grid_content = text[start_idx:end_idx]
    
    cards = grid_content.split('<div class="partner-card"')
    
    prefix = cards[0]
    cards = cards[1:]
    
    order = {}
    for c in cards:
        if '3GOG.jpg' in c: order['GOG'] = c
        elif '1AMC.jpg' in c: order['AMC'] = c
        elif 'DRDA.jpg' in c: order['DRDA'] = c
        elif 'WASMO.jpg' in c: order['WASMO'] = c
        elif '5GCCI.jpg' in c: order['GCCI'] = c
        elif '2ICDS.jpg' in c: order['ICDS'] = c
        elif '4NABARD.jpg' in c: order['NABARD'] = c
        elif '6WCD.jpg' in c: order['WCD'] = c
        elif '9NARMADA.jpg' in c: order['NARMADA'] = c
    
    # User's exact requested order
    new_order = ['GOG', 'AMC', 'GCCI', 'DRDA', 'NARMADA', 'WCD', 'WASMO', 'ICDS', 'NABARD']
    
    new_grid = prefix + ''.join(['<div class="partner-card"' + order[k] for k in new_order])
    
    new_text = text[:start_idx] + new_grid + text[end_idx:]
    
    with open('partners.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    
    print('Custom reordered successfully')
else:
    print('Could not find markers')
