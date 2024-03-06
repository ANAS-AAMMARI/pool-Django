from elements import *

class Page:
    def __init__(self, elem: elem.Elem) -> None:
        self.elem = elem

    def __str__(self) -> str:
        rslt = ''
        if isinstance(self.elem, Html):
            rslt = '<!DOCTYPE html>\n' + str(self.elem)
        else:
            rslt = str(self.elem)
        return rslt
    
    def write_to_file(self, filename: str) -> None:
        with open(filename, 'w') as file:
            file.write(str(self))
    
    
    def is_valid(self) -> bool:
        allowed_tags = (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, elem.Text)
        if not isinstance(self.elem, allowed_tags):
            return False
        if isinstance(self.elem, Html) and (len(self.elem.content) != 2 or not all([isinstance(e, (Head, Body)) for e in self.elem.content])):
            return False
        if isinstance(self.elem, Head) and [isinstance(e, Title) for e in self.elem.content].count(True) != 1:
            return False
        if isinstance(self.elem, (Body, Div)) and not all(isinstance(e, (H1, H2, Div, Table, Ul, Ol, Span, elem.Text)) for e in self.elem.content):
            return False
        if isinstance(self.elem, (Title, H1, H2, Li, Th, Td)) and not [isinstance(e, elem.Text) for e in self.elem.content].count(True) == 1:
            return False
        if isinstance(self.elem, P) and not all([isinstance(e, elem.Text) for e in self.elem.content]):
            return False
        if isinstance(self.elem, Span) and not all([isinstance(e, (elem.Text, P)) for e in self.elem.content]):
            return False
        if isinstance(self.elem, (Ul, Ol)):
            if[isinstance(e, Li) for e in self.elem.content].count(True) < 1 or not all([isinstance(e, Li) for e in self.elem.content]):
                return False
        if isinstance(self.elem, Tr):
            has_th = [isinstance(e, Th) for e in self.elem.content].count(True) > 0
            has_td = [isinstance(e, Td) for e in self.elem.content].count(True) > 0
            if (not has_th and not has_td) or (has_th and has_td):
                return False
        if isinstance(self.elem, Table) and not all([isinstance(e, Tr) for e in self.elem.content]):
            return False
        return True

def __print_test(target: Page, toBe: bool):
    print("================START===============")
    print(str(target))
    print("===============IS_VALID=============")
    assert target.is_valid() == toBe
    print("{:^36s}".format(str(target.is_valid())))
    print("=================END================")


def __test_Table():
    print("\n%{:=^34s}%\n".format("Table"))
    target = Page(Table())

    __print_test(target, True)
    target = Page(
        Table(
            [
                Tr(Th(elem.Text("title"))),
            ]))
    # print(target.is_valid())
    __print_test(target, True)
    target = Page(
        Table(
            [
                H1(
                    elem.Text("Hello World!")
                ),
            ]))
    __print_test(target, False)


def __test_Tr():
    print("\n%{:=^34s}%\n".format("Tr"))
    target = Page(Tr())
    __print_test(target, False)
    target = Page(
        Tr(
            [
                Th(elem.Text("title")),
                Th(elem.Text("title")),
                Th(elem.Text("title")),
                Th(elem.Text("title")),
                Th(elem.Text("title")),
            ]))
    __print_test(target, True)
    target = Page(
        Tr(
            [
                Td(elem.Text("content")),
                Td(elem.Text("content")),
                Td(elem.Text("content")),
                Td(elem.Text("content")),
                Td(elem.Text("content")),
                Td(elem.Text("content")),
            ]))
    __print_test(target, True)
    target = Page(
        Tr(
            [
                Th(elem.Text("title")),
                Td(elem.Text("content")),
            ]))
    __print_test(target, False)


def __test_Ul_OL():
    print("\n%{:=^34s}%\n".format("Ul_OL"))
    target = Page(
        Ul()
    )
    __print_test(target, False)
    target = Page(
        Ol()
    )
    __print_test(target, False)
    target = Page(
        Ul(
            Li(
                elem.Text('test')
            )
        )
    )
    __print_test(target, True)
    target = Page(
        Ol(
            Li(
                elem.Text('test')
            )
        )
    )
    __print_test(target, True)
    target = Page(
        Ul([
            Li(
                elem.Text('test')
            ),
            Li(
                elem.Text('test')
            ),
        ])
    )
    __print_test(target, True)
    target = Page(
        Ol([
            Li(
                elem.Text('test')
            ),
            Li(
                elem.Text('test')
            ),
        ])
    )
    __print_test(target, True)
    target = Page(
        Ul([
            Li(
                elem.Text('test')
            ),
            H1(
                elem.Text('test')
            ),
        ])
    )
    __print_test(target, False)
    target = Page(
        Ol([
            Li(
                elem.Text('test')
            ),
            H1(
                elem.Text('test')
            ),
        ])
    )
    __print_test(target, False)


def __test_Span():
    print("\n%{:=^34s}%\n".format("Span"))
    target = Page(
        Span()
    )
    __print_test(target, True)
    target = Page(
        Span([
            elem.Text("Hello?"),
            P(elem.Text("World!")),
        ])
    )
    __print_test(target, True)
    target = Page(
        Span([
            H1(elem.Text("World!")),
        ])
    )
    __print_test(target, False)


def __test_P():
    print("\n%{:=^34s}%\n".format("P"))
    target = Page(
        P()
    )
    __print_test(target, True)
    target = Page(
        P([
            elem.Text("Hello?"),
        ])
    )
    __print_test(target, True)
    target = Page(
        P([
            H1(elem.Text("World!")),
        ])
    )
    __print_test(target, False)


def __test_Title_H1_H2_Li_Th_Td():
    print("\n%{:=^34s}%\n".format("H1_H2_Li_Th_Td"))
    for c in [H1, H2, Li, Th, Td]:
        target = Page(
            c()
        )
        __print_test(target, False)
        target = Page(
            c([
                elem.Text("Hello?"),
            ])
        )
        __print_test(target, True)
        target = Page(
            c([
                H1(elem.Text("World!")),
            ])
        )
        __print_test(target, False)
        target = Page(
            c([
                elem.Text("Hello?"),
                elem.Text("Hello?"),
            ])
        )
        __print_test(target, False)


def __test_Body_Div():
    print("\n%{:=^34s}%\n".format("Body_Div"))
    for c in [Body, Div]:
        target = Page(
            c()
        )
        __print_test(target, True)
        target = Page(
            c([
                elem.Text("Hello?"),
            ])
        )
        __print_test(target, True)
        target = Page(
            c([
                H1(elem.Text("World!")),
            ])
        )
        __print_test(target, True)
        target = Page(
            c([
                elem.Text("Hello?"),
                Span(),
            ])
        )
        __print_test(target, True)
        target = Page(
            c([
                Html(),
                c()
            ])
        )
        __print_test(target, False)


def __test_Title():
    print("\n%{:=^34s}%\n".format("Title"))
    target = Page(
        Title()
    )
    __print_test(target, False)
    target = Page(
        Title([
            Title(elem.Text("Hello?")),
        ])
    )
    __print_test(target, True)
    target = Page(
        Title([
            Title(elem.Text("Hello?")),
            Title(elem.Text("Hello?")),
        ])
    )
    __print_test(target, False)


def __test_Html():
    print("\n%{:=^34s}%\n".format("Html"))
    target = Page(
        Html()
    )
    __print_test(target, False)
    target = Page(
        Html([
            Head([
                Title(elem.Text("Hello?")),
            ]),
            Body([
                H1(elem.Text("Hello?")),
            ])
        ])
    )
    __print_test(target, True)
    target = Page(
        Html(
            Div()
        )
    )
    __print_test(target, False)


def __test_Elem():
    __print_test(Page(elem.Elem()), False)


def __test_write_to_file(target: Page, path: str):
    print("================START===============")
    print(str(target))
    print("==========WRITE_TO_FILE=============")
    target.write_to_file(path)
    print("{:^36s}".format(path))
    print("=================END================")


def __test():
    __test_Table()
    __test_Tr()
    __test_Ul_OL()
    __test_Span()
    __test_P()
    __test_Title_H1_H2_Li_Th_Td()
    __test_Body_Div()
    __test_Html()
    __test_Elem()
    __test_write_to_file(
        Page(Html([Head(Title(elem.Text("hello world!"))),
             Body(H1(elem.Text("HELLO WORLD!")))])),
        "__test_write_to_file.html")


if __name__ == '__main__':
    __test()
