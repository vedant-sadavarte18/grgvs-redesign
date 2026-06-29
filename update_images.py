import re

keywords = [
    'poverty,slum', 'agriculture,farm', 'hospital,health', 'school,classroom',
    'women,equality', 'clean,drinking,water', 'solar,panel', 'business,economy',
    'factory,industry', 'diversity,people', 'sustainable,city', 'recycle,waste',
    'climate,nature', 'ocean,fish', 'forest,wildlife', 'peace,justice', 'partnership,handshake'
]

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

for idx, kw in enumerate(keywords):
    num = idx + 1
    # Replace the picsum URL with loremflickr
    # e.g., https://picsum.photos/seed/sdg1/400/400 -> https://loremflickr.com/400/400/poverty,slum/all
    old_url = f'https://picsum.photos/seed/sdg{num}/400/400'
    new_url = f'https://loremflickr.com/400/400/{kw}/all'
    content = content.replace(old_url, new_url)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated images!')
