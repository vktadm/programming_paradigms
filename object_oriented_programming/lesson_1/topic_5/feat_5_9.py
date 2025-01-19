from random import randint

class Cell:

    def __init__(self, around_mines: int = 0, mine: bool = False):
        self.around_mines = around_mines # Кол-во мин вокруг клетки
        self.mine = mine # Является ли поле миной
        self.fl_open = False # Открыта ли клетка

class GamePole:

    def __init__(self, n: int, m: int):
        self.m = m # Кол-во мин на поле
        self.n = n # Размер поля

        # Игровое поле
        self.pole = [[Cell() for _ in range(self.n)] for _ in range(self.n)]
        # Инициализация поля
        self.init()

    def init(self):
        # self.pole = [Cell(mine=rnd.choice([True, False])) for _ in range(self.N)]

        current_mine_number = 0
        while current_mine_number < self.m:
            i = randint(0, self.n - 1)
            j = randint(0, self.n - 1)

            if self.pole[i][j].mine:
                continue

            self.pole[i][j].mine = True
            current_mine_number += 1

        idx = [(x, y) for x in range(-1, 2)
               for y in range(-1, 2) if not (x == 0 and y == 0)]

        for i in range(self.n):
            for j in range(self.n):
                if not self.pole[i][j].mine:
                    self.pole[i][j].around_mines = sum(self.pole[i + x][j + y].mine
                                                       for x, y in idx if 0 <= i + x < self.n
                                                       and 0 <= j + y < self.n)

                print(f'{self.pole[i][j].mine}, {self.pole[i][j].around_mines}', end=' ')
            print('\n')

    def show(self):
        for i in range(self.n):
            for j in range(self.n):
                if not self.pole[i][j].fl_open:
                    print('#', end=' ')
                elif self.pole[i][j].mine:
                    print('#', end=' ')
                else:
                    print(' ', end=' ')
            print()


if __name__ == '__main__':
    gp = GamePole(10, 12)
    gp.show()