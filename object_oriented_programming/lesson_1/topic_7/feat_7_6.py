class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


class Viber:
    MSG_LST = []

    @classmethod
    def add_message(cls, msg):
        cls.MSG_LST.append(msg)

    @classmethod
    def remove_message(cls, msg):
        try:
            cls.MSG_LST.remove(msg)
        except ValueError:
            print('Такого элемента не существует')

    @staticmethod
    def set_like(msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, number):
        print(cls.MSG_LST[-number:-1])

    @classmethod
    def total_messages(cls):
        return len(cls.MSG_LST)


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
