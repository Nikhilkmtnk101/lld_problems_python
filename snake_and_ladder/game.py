from collections import deque
from snake_and_ladder.entities.board import Board
from snake_and_ladder.entities.dice import Dice
from snake_and_ladder.entities.jumps.ladder import Ladder
from snake_and_ladder.entities.jumps.snake import Snake
from snake_and_ladder.entities.player import Player


class Game:
    def __init__(self, board_size, no_of_faces):
        self.board = Board(board_size)
        self.dice = Dice(no_of_faces)
        self.players = deque()

    "Private Methods"
    def __move_player_to_end(self, player):
        self.players.append(player)

    def __validate_move(self, new_position):
        if new_position > self.board.get_size():
            return False
        return True

    def __does_player_won(self, player):
        return player.get_position() == self.board.get_size()

    def __get_new_position(self, current_position, dice_value):
        new_position = current_position + dice_value

        if not self.__validate_move(new_position):
            return current_position

        can_be_jumped = True
        snakes = self.board.get_snakes()
        ladders = self.board.get_ladders()

        while can_be_jumped:
            for snake in snakes:
                if new_position == snake.get_start_position():
                    new_position = snake.get_end_position()
                    break

            for ladder in ladders:
                if new_position == ladder.get_start_position():
                    new_position = ladder.get_end_position()
                    break

            can_be_jumped = False

        return new_position

    "Public Methods"

    def add_player(self, name):
        player = Player(name)
        self.players.append(player)

    def add_snake(self, head, tail):
        snake = Snake(head, tail)
        self.board.add_snake(snake)

    def add_ladder(self, start, end):
        ladder = Ladder(start, end)
        self.board.add_ladder(ladder)

    def play(self):
        while len(self.players) > 0:
            player = self.players.popleft()
            current_position = player.get_position()
            dice_value = self.dice.roll()
            new_position = self.__get_new_position(current_position, dice_value)
            player.set_position(new_position)
            if self.__does_player_won(player):
                print(f'{player.get_name()} rolled a {dice_value} and moved from {current_position} to {new_position}')
                print(f'{player.get_name()} wins the game')
            else:
                print(f'{player.get_name()} rolled a {dice_value} and moved from {current_position} to {new_position}')
                self.__move_player_to_end(player)
