from bs4 import BeautifulSoup
import re

file_path = r"C:\Users\HP\.gemini\antigravity\brain\681070d0-73dc-4b63-b394-c8f161e0a98f\.system_generated\steps\1639\content.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# The content starts with some markdown headers, find where HTML starts
html_start = content.find("<!DOCTYPE html>")
if html_start != -1:
    content = content[html_start:]

soup = BeautifulSoup(content, 'html.parser')

# Find the main content area (usually article, main, or specific divs)
main_content = soup.find('article') or soup.find('main') or soup.body

if main_content:
    # Try to extract the text
    text = main_content.get_text(separator='\n', strip=True)
    # Print the first 2000 chars to see what we have
    print("Content Preview:")
    print(text[:2000])
else:
    print("Main content not found.")
