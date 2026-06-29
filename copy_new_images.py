import shutil
import os

artifact_dir = r"C:\Users\HP\.gemini\antigravity\brain\681070d0-73dc-4b63-b394-c8f161e0a98f"
assets_dir = r"C:\Users\HP\.gemini\antigravity\scratch\grgvs-redesign\assets"

files_to_copy = [
    "media__1782370547074.jpg",
    "media__1782370555318.jpg",
    "media__1782370571524.jpg",
    "media__1782370593961.jpg",
    "media__1782370605613.jpg"
]

for i, filename in enumerate(files_to_copy):
    src = os.path.join(artifact_dir, filename)
    dst = os.path.join(assets_dir, f"proj_img{i+1}.jpg")
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {filename} to proj_img{i+1}.jpg")
    else:
        print(f"File not found: {filename}")
