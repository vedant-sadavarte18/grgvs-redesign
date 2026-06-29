import urllib.request
import re

keywords = [
    'poverty slum', 'agriculture farming', 'hospital doctor', 'school classroom',
    'women equality', 'clean drinking water', 'solar panels', 'business economy',
    'industry factory', 'diversity people', 'sustainable green city', 'recycle waste',
    'climate change nature', 'ocean coral reef', 'forest wildlife', 'peace dove justice', 'handshake partnership'
]

ids = []
for kw in keywords:
    try:
        url = f'https://html.duckduckgo.com/html/?q=site:unsplash.com+{kw.replace(" ", "+")}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        valid_ids = re.findall(r'unsplash\.com/photos/.*?([a-zA-Z0-9_-]{11})', html)
        if valid_ids:
            ids.append(valid_ids[0])
        else:
            ids.append('fallback')
    except Exception as e:
        ids.append(str(e))
print(ids)
