
from classes import Point, Player, Board, Mode, ImpossibleMove, CoordsOfNotActivePoint, PointOccupiedError
from game import Game
import pytest


def pick_mode():
    """player enters mode"""

    game_mode = input("""Choose Game Mode
    1 : Three men's morris
    2 : Six men's morris
    3 : Nine men's morris
    4 : Twelve men's morris\nMode number:""")
    modes = [1, 2, 3, 4]
    while (not game_mode.isdigit()) or (not int(game_mode) in modes):
        print("Wrong mode number, choose from given (1,2,3,4)\n")
        game_mode = input("Mode number:")
    return int(game_mode)


def main():
    game_mode = pick_mode()
    game = Game(game_mode)
    player1 = Player(1)
    player2 = Player(2)
    board = game.board()
    print(board.print_board())
    while game.win() == False:
        for player in [player1, player2]:
            game.make_move(player)


if __name__ == "__main__":
    main()
