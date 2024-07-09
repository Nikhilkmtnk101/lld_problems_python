class Board:
    def __init__(self, size):
        self.size = size
        self.snakes = []
        self.ladders = []

    def get_size(self):
        return self.size

    def set_snakes(self, snakes):
        self.snakes = snakes

    def get_snakes(self):
        return self.snakes

    def set_ladders(self, ladders):
        self.ladders = ladders

    def get_ladders(self):
        return self.ladders

    def add_snake(self, snake):
        self.snakes.append(snake)

    def add_ladder(self, ladder):
        self.ladders.append(ladder)
