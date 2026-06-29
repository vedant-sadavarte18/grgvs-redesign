import os
import glob

html_files = glob.glob('*.html')
old_text = "Gujarat Rajya Gram Vikas Samiti (GRGVS) is a registered NGO since 1988. Our Public Trust Registration no is F/308 under Bombay Public Trust Act 1950 and Society Registration no. is GUJ/321 under society registration act 1860. GRGVS has 12AA and 80G registration under IT Act, 1961. Our CSR Registration Number is CSR 00014330 under the Central Government. Our FCRA registration no. is 41910403. We have registration with NITI Aayog and our Unique Darpan ID is GJ/2018/0217432."

new_text = "Gujarat Rajya Gram Vikas Samiti (GRGVS) is a registered NGO since 1988. Our Public Trust Registration no is <strong>F/308 under Bombay Public Trust Act 1950</strong> and Society Registration no. is <strong>GUJ/321 under society registration act 1860</strong>. GRGVS has <strong>12AA and 80G registration under IT Act, 1961</strong>. Our CSR Registration Number is <strong>CSR 00014330 under the Central Government</strong>. Our FCRA registration no. is <strong>41910403</strong>. We have registration with NITI Aayog and our Unique Darpan ID is <strong>GJ/2018/0217432</strong>."

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f"Updated {count} files.")
