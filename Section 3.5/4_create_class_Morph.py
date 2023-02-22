import re


class Morph:
    def __init__(self, *args):
        self.words = args

    def add_word(self, word):
        if word not in self.words:
            self.words = tuple([*self.words] + [word])

    def get_words(self):
        return self.words

    def __eq__(self, other):
        if type(self) == str:
            self, other = other, self
        return any([other.lower() in i for i in self.words])

    def __ne__(self, other):
        if type(self) == str:
            self, other = other, self
        return any([other.lower() not in i for i in self.words])


s = """- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях
"""

dict_words = [Morph(*line.lstrip('- ').split(', ')) for line in s.splitlines()]

text = input()

counter = 0
for word in text.split():
    word = res = re.sub(r'[^\w\s]', '', word)
    for morph in dict_words:
        if word.lower() in morph.get_words():
            counter += 1


print(counter)
