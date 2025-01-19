TYPE_OS = 2 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:

    def __new__(cls, *args, **kwargs):
        obj = None
        if TYPE_OS == 1:
            obj = cls.__instance = object.__new__(DialogWindows)
        elif TYPE_OS == 2:
            obj = cls.__instance = object.__new__(DialogLinux)

        obj.name = args[0]
        return obj


if __name__ == "__main__":
    dlg = Dialog('Окно 1')
    print(type(dlg))
    dlg1 = Dialog('Окно 2')
    print(type(dlg1))