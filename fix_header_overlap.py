with open('styles.css', 'a', encoding='utf-8') as f:
    f.write('\n\n/* Added to fix header overlap after logo size increase */\n.page-header {\n    padding-top: 180px !important;\n}\n')
print("Appended .page-header padding-top to styles.css")
