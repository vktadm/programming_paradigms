class Table:

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price

class TV:

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price

class Notebook:

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price

class Cup:

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price

class Cart():

    def __init__(self):
        self.goods = []

    def add(self, gd: Table | TV | Notebook | Cup) -> None:
        self.goods.append(gd)

    def remove(self, indx: int) -> None:
        self.goods.pop(indx)

    def get_list(self) -> list:
        return [f'{good.name}:{good.price}' for good in self.goods]

if __name__ == '__main__':
    cart = Cart()

    # Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup).
    cart.add(TV('LG', 15_000))
    cart.add(Table('Тот самый стол', 10_000))
    cart.add(Notebook('Apple MacBook Pro', 250_000))
    cart.add(Notebook('Lenovo', 100_000))
    cart.add(Cup('Кружка из Skuratov', 2_500))

    print(cart.get_list())