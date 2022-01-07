
from classes import Point, Player, Board, Mode, ImpossibleMove, CoordsOfNotActivePoint, PointOccupiedError
from game import Game
import pytest
import os


def pick_mode():
    """player enters mode"""
    print("""Choose Game Mode
    1 : Three men's morris
    2 : Six men's morris
    3 : Nine men's morris
    4 : Twelve men's morris\n""")
    modes = [1, 2, 3, 4]
    valid = False
    while not valid:
        game_mode = input("Mode number:")
        if  not game_mode.isdigit():
            print("Wrong mode number, choose from given (1,2,3,4)\n")
            continue
        elif not int(game_mode) in modes:
            print("Wrong mode number, choose from given (1,2,3,4)\n")
            continue
        else:
            valid = True
    return int(game_mode)

def main():
    import os
    clear = lambda: os.system('clear')
    clear()
    game_mode = pick_mode()
    game = Game(game_mode)
    player1 = game.player1
    player2 = game.player2
    board = game.board()
    clear()
    print(board.print_board())
    while game.win() == False:
        for player in [player1, player2]:
            clear()
            game.check_phase()
            game.make_move(player)
            game.check_mills(player)




if __name__ == "__main__":
    main()
