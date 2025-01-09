import sys

class StreamData:

    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False

        for key, value in zip(fields, lst_values):
            setattr(self, key, value)
        return True

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = (10, 'Питон - основы мастерства', 512)
        # lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        print(sd.__dict__)
        return sd, res

if __name__ == '__main__':
    sr = StreamReader()
    data, result = sr.readlines()
