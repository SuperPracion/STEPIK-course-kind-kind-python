class Translator:
    word_pairs = {}

    def add(self, eng, rus):
        if eng in self.word_pairs:
            if rus not in self.word_pairs[eng]:
                self.word_pairs[eng] += [rus]
        else:
            self.word_pairs[eng] = [rus]

    def remove(self, eng):
        del self.word_pairs[eng]

    def translate(self, eng):
        return self.word_pairs[eng]


words = [('tree', 'дерево'), ('car', 'машина'), ('car', 'автомобиль'), ('leaf', 'лист'), ('river', 'река'),
         ('go', 'идти'), ('go', 'ехать'), ('go', 'ходить'), ('milk', 'молоко')]

tr = Translator()

for eng, rus in words:
    tr.add(eng, rus)

tr.remove('car')
print(*tr.translate('go'))

assert isinstance(tr, Translator)
assert hasattr(Translator, 'add') and hasattr(Translator, 'remove') and hasattr(Translator, 'translate')
assert tr.translate('tree')[0] == "дерево"