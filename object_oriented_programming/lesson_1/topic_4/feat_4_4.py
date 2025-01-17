from os.path import split


class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])

        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        self.tr.pop(eng, False)

    def translate(self, eng):
        return self.tr[eng]


if __name__ == '__main__':
    tr = Translator()

    data = ['tree - дерево', 'car - машина', 'car - автомобиль',
            'leaf - лист', 'river - река', 'go - идти',
            'go - ехать', 'go - ходить', 'milk - молоко']
    for item in data:
        eng, rus = item.split('-')
        tr.add(eng.strip(), rus.strip())

    tr.remove('car')
    print(*tr.translate('go'))