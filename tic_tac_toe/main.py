from collections import deque
from enum import Enum


class Piece(Enum):
    PIECE_X = 'X'
    PIECE_O = 'O'


class Player:
    def __init__(self, name: str, piece: str):
        self.name = name
        self.piece = piece

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_piece(self) -> str:
        return self.piece

    def set_piece(self, piece: str):
        self.piece = piece


class Board:
    def __init__(self, board_size: int):
        self.board_size = board_size
        self.cells = [['-' for i in range(board_size)] for j in range(board_size)]
        self.empty_cells_count = board_size * board_size

    def get_board_size(self) -> int:
        return self.board_size

    def set_board_size(self, board_size: int):
        self.board_size = board_size

    def get_cells(self) -> list[list[str]]:
        return self.cells

    def set_cells(self, cells: list[list[str]]):
        self.cells = cells

    def get_cell_value(self, x: int, y: int):
        return self.cells[x][y]

    def set_cell_value(self, x: int, y: int, value: str):
        self.cells[x][y] = value
        self.empty_cells_count -= 1

    def is_empty_cell(self, x: int, y: int) -> bool:
        return self.cells[x][y] == '-'

    def get_empty_cell_count(self) -> int:
        return self.empty_cells_count


class Game:
    def __init__(self, no_players: int, board_size: int):
        self.is_game_completed = False
        self.no_players = no_players
        self.board_size = board_size
        self.board = Board(board_size)
        self.players = deque()

    "Private Methods"

    def __validate_move(self, x: int, y: int) -> bool:
        if x < 0 or y < 0 or x >= self.board_size or y >= self.board_size:
            return False
        return self.board.is_empty_cell(x, y)

    def __is_game_completed(self):
        return self.is_game_completed

    def __display_board(self):
        cells = self.board.get_cells()
        res = f''
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                res += cells[i][j] + ' '
            res += '\n'
        print(res)
        print()

    def __check_winner(self, piece: str) -> bool:
        # Check row wise
        for i in range(0, self.board_size):
            count = 0
            for j in range(0, self.board_size):
                if piece == self.board.get_cell_value(i, j):
                    count += 1
            if count == self.board_size:
                return True

        # Check column wise
        for j in range(0, self.board_size):
            count = 0
            for i in range(0, self.board_size):
                if piece == self.board.get_cell_value(i, j):
                    count += 1
            if count == self.board_size:
                return True

        # Check Left Diagonal
        count = 0
        for i in range(0, self.board_size):
            if piece == self.board.get_cell_value(i, i):
                count += 1

        if count == self.board_size:
            return True

        # Check Right Diagonal
        count = 0
        for i in range(0, self.board_size):
            if piece == self.board.get_cell_value(i, self.board_size-i-1):
                count += 1

        if count == self.board_size:
            return True

        return False

    "Public Methods"

    def add_players(self, name: str, piece: str):
        if len(self.players) == self.no_players:
            raise Exception("Player cannot be added")

        self.players.append(Player(name, piece))

    def make_move(self, x: int, y: int):
        i = x-1
        j = y-1

        if self.__is_game_completed():
            print("Game Ended")
            return

        if not self.__validate_move(i, j):
            print("Invalid move")
            return

        player = self.players.popleft()
        self.board.set_cell_value(i, j, player.get_piece())
        self.players.append(player)
        if self.__check_winner(player.get_piece()):
            self.is_game_completed = True
            print(f"{player.get_name()} won the game")
            self.__display_board()
            return

        if self.board.get_empty_cell_count() == 0:
            self.is_game_completed = True
            print(f'Game Draw')

        self.__display_board()

if __name__ == '__main__':
    game = Game(2, 3)
    game.add_players("Gaurav", 'X')
    game.add_players("Sagar", 'O')

    game.make_move(2, 2)
    game.make_move(1, 3)
    game.make_move(1, 1)
    game.make_move(1, 2)
    game.make_move(2, 2)
    game.make_move(3, 3)
