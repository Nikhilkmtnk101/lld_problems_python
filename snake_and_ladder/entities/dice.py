import random


class Dice:
    def __init__(self, no_of_faces):
        self.no_of_faces = no_of_faces

    def get_no_of_faces(self):
        return self.no_of_faces

    def roll(self):
        return random.randint(1, self.no_of_faces)
