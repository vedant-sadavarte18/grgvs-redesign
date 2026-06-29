import re

with open('csr.html', 'r', encoding='utf-8') as f:
    csr_content = f.read()

# Let's see where to inject the image
# We can inject it below the What is CSR? section or create a new section
# Let's search for "What is CSR?"
if 'What is CSR?' in csr_content:
    print("Found 'What is CSR?'")
else:
    print("Not found 'What is CSR?'")
