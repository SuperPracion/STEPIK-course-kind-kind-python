import copy
import random


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[copy.copy(Cell()) for _ in range(self.N)] for _ in range(self.N)]

        self.init()
        self.counting_neighbors()

    def show(self):
        for line in self.pole:
            for cell in line:
                print(cell.mine, end=' ')
            print()

    def init(self):
        while self.M > 0:
            cell = self.pole[random.randint(0, self.N - 1)][random.randint(0, self.N - 1)]
            if not cell.mine and bool(random.randint(0, 1)):
                cell.mine = True
                self.M -= 1

    def counting_neighbors(self):
        for i in range(self.N):
            for j in range(self.N):
                cell = self.pole[i][j]
                if j > 0 and self.pole[i][j - 1].mine:  # слева
                    cell.around_mines += 1
                if j < self.N - 1 and self.pole[i][j + 1].mine:  # справа
                    cell.around_mines += 1
                if i > 0 and self.pole[i - 1][j].mine:  # сверху
                    cell.around_mines += 1
                if i < self.N - 1 and self.pole[i + 1][j].mine:  # внизу
                    cell.around_mines += 1
                if (j > 0 and i > 0) and self.pole[i - 1][j - 1].mine: # вверх в лево
                    cell.around_mines += 1
                if (j < self.N - 1 and i < self.N - 1) and self.pole[i + 1][j + 1].mine: # вниз в право
                    cell.around_mines += 1
                if (i > 0 and j < self.N - 1) and self.pole[i - 1][j + 1].mine: # вверх в право
                    cell.around_mines += 1
                if (j > 0 and i < self.N - 1) and self.pole[i + 1][j - 1].mine:
                    cell.around_mines += 1


pole_game = GamePole(3, 4)