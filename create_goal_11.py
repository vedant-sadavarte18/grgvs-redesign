import re
import os

with open('goal-10.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles
content = re.sub(r'Goal 10: Disabled / Elderly', 'Goal 11: Disaster Relief', content)
content = re.sub(r'Goal 10:', 'Goal 11:', content)
# Replace the bolded text in the description
content = re.sub(r'<strong>Disabled / Elderly</strong>', '<strong>Disaster Relief</strong>', content)

with open('goal-11.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('goal-11.html created successfully!')
