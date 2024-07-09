from snake_and_ladder.game import Game

if __name__ == '__main__':
    "Creating game"
    game = Game(100, 6)
    "Adding snakes to game"
    game.add_snake(62, 5)
    game.add_snake(33, 6)
    game.add_snake(49, 9)
    game.add_snake(88, 16)
    game.add_snake(41, 20)
    game.add_snake(56, 53)
    game.add_snake(98, 64)
    game.add_snake(93, 73)
    game.add_snake(95, 75)

    "Adding ladders to game"
    game.add_ladder(2, 37)
    game.add_ladder(27, 46)
    game.add_ladder(10, 32)
    game.add_ladder(51, 68)
    game.add_ladder(61, 79)
    game.add_ladder(65, 84)
    game.add_ladder(71, 91)
    game.add_ladder(81, 100)

    "Adding players"
    game.add_player("Gaurav")
    game.add_player("Sagar")

    game.play()
