from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
    
    def handle_starttag(self, tag, attrs):
        if tag not in ['meta', 'link', 'img', 'br', 'hr', 'input', 'source']:
            self.stack.append(tag)
            
    def handle_endtag(self, tag):
        if tag not in ['meta', 'link', 'img', 'br', 'hr', 'input', 'source']:
            if not self.stack:
                self.errors.append(f'Extra end tag </{tag}>')
            elif self.stack[-1] == tag:
                self.stack.pop()
            else:
                self.errors.append(f'Mismatched tag: expected </{self.stack[-1]}>, got </{tag}>')

parser1 = MyHTMLParser()
with open('urban-forest.html', 'r', encoding='utf-8') as f:
    parser1.feed(f.read())
print('Urban Forest errors:', parser1.errors[:5])

parser2 = MyHTMLParser()
with open('plant-data.html', 'r', encoding='utf-8') as f:
    parser2.feed(f.read())
print('Plant Data errors:', parser2.errors[:5])
