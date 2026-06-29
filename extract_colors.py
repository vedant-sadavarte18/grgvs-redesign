from PIL import Image
from collections import Counter
import sys

def get_dominant_colors(image_path, num_colors=5):
    img = Image.open(image_path)
    img = img.resize((100, 100)) # Resize for faster processing
    
    # Convert to RGB if it's RGBA or other
    if img.mode != 'RGB':
        img = img.convert('RGB')
        
    pixels = list(img.getdata())
    
    # Quantize a bit to group similar colors
    quantized_pixels = [(r//10*10, g//10*10, b//10*10) for (r, g, b) in pixels]
    
    counter = Counter(quantized_pixels)
    most_common = counter.most_common(20)
    
    for color, count in most_common:
        hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
        print(f"Color: {hex_color} - rgb({color[0]}, {color[1]}, {color[2]}) - Count: {count}")

print("Analyzing Logo.jpg...")
get_dominant_colors(r"assets\website_\Logo.jpg")
