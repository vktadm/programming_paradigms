class Point:
    def __new__(cls, *args, **kwargs):
        print(f'Вызов __new__ для {str(cls)}')
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print(f'Вызов __init__ для {str(self)}')
        self.x = x
        self.y = y

class DataBase:
    "Паттерн Singleton"
    __instance = None # Ссылка на экземпляр класса

    def __new__(cls, *args, **kwargs):
        # Будет только 1 раз создан экзкмпляр класса
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        # Иначе будем возвращать ссылку на существующий экземпляр класса
        return cls.__instance

    def __del__(cls):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user} - {self.psw} - {self.port}')

    def close(self):
        print('Закрытие соединения')

    def write(self, data):
        print(f'Запись в БД {data}')

if __name__ == '__main__':
    # pt = Point(1, 2)
    db = DataBase('user', 'psw', 'port')
    db2 = DataBase('user2', 'psw2', 'port2')

    print(db == db2)
    print(id(db), id(db2), end='\n\n')

    print(db2.__doc__)
    print(db.__dict__, end='\n\n')

    db.connect()
    db2.connect()