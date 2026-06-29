import urllib.request
import re

url = "https://gujaratgramvikas.org/wp-content/uploads/2022/08/CSR-Pyramid2-1-1024x630.png"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    urllib.request.urlretrieve(url, "assets/csr-pyramid.png")
    print("Downloaded to assets/csr-pyramid.png")
except Exception as e:
    print("Error:", e)
