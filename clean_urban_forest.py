import re

with open('urban-forest.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We want to remove the garbage from <!-- Tree Layer --> to just before <!-- Locations Identified -->
pattern = r'(?s)<!-- Tree Layer -->.*?</div>\s*</div>\s*</div>\s*(?=<!-- Locations Identified -->)'

# Let's be safer and just string split if regex is tricky
part1 = content.split('<!-- Tree Layer -->')[0]
# the second part should start from <!-- Locations Identified -->
part2_split = content.split('<!-- Locations Identified -->')
if len(part2_split) > 1:
    part2 = '<!-- Locations Identified -->' + part2_split[1]
    
    # Let's combine them
    new_content = part1 + part2
    
    with open('urban-forest.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Cleaned up urban-forest.html successfully!")
else:
    print("Could not find <!-- Locations Identified -->")
