class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


class AppStore:
    def __init__(self):
        self.app_lst = []

    def add_application(self, app):
        """Добавление нового приложения app в магазин"""
        self.app_lst.append(app)


    def remove_application(self, app):
        """Удаление приложения app из магазина"""
        try:
            self.app_lst.remove(app)
        except ValueError:
            print('Такого элемента не существует')

    def block_application(self, app):
        """Блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True)"""
        app.blocked = True

    def total_apps(self):
        """Возвращает общее число приложений в магазине"""
        return len(self.app_lst)


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
