class FileAcceptor:
    def __init__(self, *args):
        self.extensions = set(args)

    def __call__(self, extension):
        return extension.split('.')[-1] in self.extensions

    def __add__(self, other):
        return FileAcceptor(*list(self.extensions | other.extensions))

filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames)