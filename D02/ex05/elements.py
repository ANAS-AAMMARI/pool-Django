import elem

class Html(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', content=content, attr=attr, tag_type='double')
    
class Head(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='head', content=content, attr=attr, tag_type='double')

class Body(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='body', content=content, attr=attr, tag_type='double')

class Title(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='title', content=content, attr=attr, tag_type='double')

class Meta(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='meta', content=content, attr=attr, tag_type='simple')

class Img(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='img', content=content, attr=attr, tag_type='simple')

class Table(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='table', content=content, attr=attr, tag_type='double')

class Th(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='th', content=content, attr=attr, tag_type='double')

class Tr(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='tr', content=content, attr=attr, tag_type='double')

class Td(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='td', content=content, attr=attr, tag_type='double')

class Ul(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ul', content=content, attr=attr, tag_type='double')

class Ol(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ol', content=content, attr=attr, tag_type='double')

class Li(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='li', content=content, attr=attr, tag_type='double')

class H1(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h1', content=content, attr=attr, tag_type='double')

class H2(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h2', content=content, attr=attr, tag_type='double')

class P(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='p', content=content, attr=attr, tag_type='double')

class Div(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='div', content=content, attr=attr, tag_type='double')

class Span(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='span', content=content, attr=attr, tag_type='double')

class Hr(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='hr', content=content, attr=attr, tag_type='simple')

class Br(elem.Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='br', content=content, attr=attr, tag_type='simple')

def test_html():
    html = Html([
        Head(Title(elem.Text('"Hello ground!"'))),
        Body([
            H1(elem.Text('"Oh no, not again!"')),
            Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'}),
            P(elem.Text('"The question of life, the universe and everything."')),
        ])
    ])
    print(html)

# another test with all elements
def test_all():
    html = Html(content=[
        Head(content=Title(content=elem.Text('"Hello ground!"'))),
        Body(content=[
            H1(content=elem.Text('"Oh no, not again!"')),
            Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'}),
            P(content=elem.Text('"The question of life, the universe and everything."')),
            Table(content=[
                Tr(content=[
                    Th(content=elem.Text("Header 1")),
                    Th(content=elem.Text("Header 2"))
                ]),
                Tr(content=[
                    Td(content=elem.Text("Content 1")),
                    Td(content=elem.Text("Content 2"))
                ])
            ]),
            Ul(content=[
                Li(content=elem.Text("Item 1")),
                Li(content=elem.Text("Item 2"))
            ]),
            Ol(content=[
                Li(content=elem.Text("Item 1")),
                Li(content=elem.Text("Item 2"))
            ]),
            Hr(),
            Br()
        ])
    ])
    print(html)
    

if __name__ == "__main__":
    # test_html()
    test_all()
