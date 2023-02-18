class RenderList:
    def __init__(self, type_list='ul' ):
        self.type_list = 'ol' if type_list == 'ol' else 'ul'

    def __call__(self, lst):
        lst = ''.join(map(lambda str: f'<li>{str}</li>\n', lst))
        return f"<{self.type_list}>\n{lst}</{self.type_list}>"


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)

print(html)