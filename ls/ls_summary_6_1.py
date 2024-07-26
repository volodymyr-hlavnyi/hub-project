# Напишите игру "морской бой"
# в рамках этого задания реализовать класс клетки,
# класс корабля ( корабли могут состоять из 1-2-3 клеток)
# класс игрока ( у игрока есть набор кораблей)
# класс игрового поля
# и класс самой игры.
# ход должен переходить от одного игрока к другому
# в зависимости от результатов хода (попал - стреляй еще,
# не попал - передай ход) игра заканчивается,
# когда у одного из игроков закончатся корабли
#
# Задача со звёздочкой - на каждом ходу отображать в консоли игровое поле
# X - клетка с подбитым корабликом
# @ - попадание в воду
# ? - не обстрелянная клетка
from random import randint


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = '?'

    def __str__(self):
        return self.status

    def __repr__(self):
        return self.status

    def shoot(self):
        if self.status == '?':
            self.status = '@'
            return False
        return True

    def set_ship(self):
        self.status = 'X'

    def is_ship(self):
        return self.status == 'X'

    def is_empty(self):
        return self.status == '?'

    def is_shot(self):
        return self.status == '@'


class Ship:
    def __init__(self, cells):
        self.cells = cells

    def is_alive(self):
        for cell in self.cells:
            if cell.is_empty():
                return True
        return False

    def shoot(self, x, y):
        for cell in self.cells:
            if cell.x == x and cell.y == y:
                return cell.shoot()
        return False

    def set_ship(self, x, y):
        for cell in self.cells:
            if cell.x == x and cell.y == y:
                cell.set_ship()
                return True
        return False


class Player:
    def __init__(self, name):
        self.name = name
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def is_alive(self):
        for ship in self.ships:
            if ship.is_alive():
                return True
        return False

    def shoot(self, x, y):
        for ship in self.ships:
            if ship.shoot(x, y):
                return True
        return False

    def set_ship(self, x, y):
        for ship in self.ships:
            if ship.set_ship(x, y):
                return True
        return False


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play(self):
        while self.player1.is_alive() and self.player2.is_alive():
            x, y = map(int, input(f'{self.current_player.name} enter x y: ').split())
            if self.current_player.shoot(x, y):
                print('Hit')
            else:
                print('Miss')
            self.switch_player()
        print(f'{self.current_player.name} wins')


if __name__ == '__main__':
    player1 = Player(input("Enter name 1 player: "))
    player2 = Player(input("Enter name 2 player (empty - Robot): "))
    if player2.name == '':
        player2.name = 'Robot'

    print(f'{player1.name} set ships')
    for i in range(4):  # 0, 1, 2, 3
        # 4 cells  - 1 pcs
        x, y = map(int, input(f'{player1.name} enter x y for ship {i + 1} (4 length): ').split())
        player1.set_ship(x, y)
        ship4_1 = Ship([Cell(x, y)])
        player1.add_ship(ship4_1)
        # 3 cells  - 2 pcs
        for k in range(3):
            x, y = map(int, input(f'{player1.name} enter x y for ship {i + 1} (1 length): ').split())
            player1.set_ship(x, y)
            ship3_2 = Ship([Cell(x, y)])
            player1.add_ship(ship3_2)
        # 2 cells  - 3 pcs
        for k in range(2):
            x, y = map(int, input(f'{player1.name} enter x y for ship {i + 1} (2 length): ').split())
            player1.set_ship(x, y)
        # 1 cells  - 4 pcs
        for k in range(1):
            x, y = map(int, input(f'{player1.name} enter x y for ship {i + 1} (3 length): ').split())
            player1.set_ship(x, y)

    player1.add_ship(ship1)
    player1.add_ship(ship2)
    player1.add_ship(ship3)

    print(f'{player2.name} set ships')
    is2robot = player2.name == 'Robot'
    for i in range(4):  # 0, 1, 2, 3
        if is2robot:
            # 4 cells  - 1 pcs
            player2.set_ship(randint(1, 10), randint(1, 10))
            # 3 cells  - 2 pcs
            for k in range(3):
                player2.set_ship(randint(1, 10), randint(1, 10))
            # 2 cells  - 3 pcs
            for k in range(2):
                player2.set_ship(randint(1, 10), randint(1, 10))
            # 1 cells  - 4 pcs
            for k in range(1):
                player2.set_ship(randint(1, 10), randint(1, 10))
        else:
            # 4 cells  - 1 pcs
            x, y = map(int, input(f'{player2.name} enter x y for ship {i + 1} (4 length): ').split())
            player2.set_ship(x, y)
            # 3 cells  - 2 pcs
            for k in range(3):
                x, y = map(int, input(f'{player2.name} enter x y for ship {i + 1} (1 length): ').split())
                player2.set_ship(x, y)
            # 2 cells  - 3 pcs
            for k in range(2):
                x, y = map(int, input(f'{player2.name} enter x y for ship {i + 1} (2 length): ').split())
                player2.set_ship(x, y)
            # 1 cells  - 4 pcs
            for k in range(1):
                x, y = map(int, input(f'{player2.name} enter x y for ship {i + 1} (3 length): ').split())
                player2.set_ship(x, y)



    ship4 = Ship([Cell(1, 1), Cell(2, 1), Cell(3, 1)])
    ship5 = Ship([Cell(1, 2), Cell(2, 2)])
    ship6 = Ship([Cell(1, 3)])

    player2.add_ship(ship4)
    player2.add_ship(ship5)
    player2.add_ship(ship6)

    game = Game(player1, player2)
    game.play()
