import urllib.request
import re
import time

keywords = [
    'poverty child poor', 'agriculture farming field', 'doctor hospital health', 'classroom students school',
    'women empowerment equality', 'drinking water clean tap', 'solar panels energy', 'economic growth chart business',
    'industry factory infrastructure', 'diversity group people', 'sustainable green city ecosystem', 'recycle waste management',
    'climate change drought environment', 'underwater coral fish ocean', 'forest trees wildlife land', 'peace dove justice court', 'handshake partnership agreement'
]

urls = []
for kw in keywords:
    try:
        search_url = f'https://html.duckduckgo.com/html/?q=site:pexels.com/photo+{kw.replace(" ", "+")}'
        req = urllib.request.Request(search_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # match pexels photo id
        matches = re.findall(r'pexels\.com/photo/[a-zA-Z0-9-]+-(\d+)', html)
        if matches:
            photo_id = matches[0]
            urls.append(f'https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&w=400')
        else:
            urls.append(f'fallback for {kw}')
    except Exception as e:
        urls.append(str(e))
    time.sleep(1) # avoid rate limit

print("urls = [")
for u in urls:
    print(f"    '{u}',")
print("]")
