import re
with open('goal-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<title>.*?</title>', '<title>GRGVS | Main Project: Urban Forest</title>', content)
content = re.sub(r'<h1>.*?</h1>', '<h1>Main Project: Urban Forest</h1>', content)
content = re.sub(r'<strong>.*?</strong>', '<strong>Urban Forest</strong>', content, count=1)

with open('urban-forest.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('urban-forest.html created')
