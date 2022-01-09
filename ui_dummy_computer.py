from classes import Player, ComputerPlayer
from game import Game
import os


def pick_mode():
    print("""Choose Game Mode
    1 : Three men's morris
    2 : Six men's morris
    3 : Nine men's morris
    4 : Twelve men's morris\n""")
    modes = [1, 2, 3, 4]
    valid = False
    try:
        while not valid:
            game_mode = input("Mode number:")
            if not game_mode.isdigit():
                print("Wrong mode number, choose from given (1,2,3,4)\n")
                continue
            elif not int(game_mode) in modes:
                print("Wrong mode number, choose from given (1,2,3,4)\n")
                continue
            else:
                valid = True
    except ValueError:
        print("Sorry, try again")
        pick_mode()
    return int(game_mode)

def pick_player(game):
    print("Pick symbol you wanna play with (Enter O or X).'O' goes always first. ")
    symbols = ["X","x", "O","o"]
    symbol = input("symbol:")
    while symbol not in symbols:
        symbol = input("symbol:")
    if symbol == "O" or symbol == "o":
        game.player2 = ComputerPlayer(2)
        game.computer_player = game.player2
    elif symbol == "X" or symbol == "x":
        game.player1 = ComputerPlayer(1)
        game.computer_player = game.player1


def main():
    def clear(): return os.system('clear')
    clear()
    game_mode = pick_mode()
    game = Game(game_mode)
    pick_player(game)
    board = game.board()
    clear()
    print(board.print_board())
    while game.win() is False:
        for player in game.players():
            clear()
            game.check_phase()
            if type(player) == ComputerPlayer:
                game.computer_move(player)
                game.check_computer_mills(player)
                game.check_win()
            else:
                game.make_move(player)
                game.check_mills(player)
                game.check_win()
            if game.win():
                break
    clear()
    print(board.print_board())
    winner = game.reveal_winner()
    if not winner:
        print("DRAW!!!")
    else:
        print(f'Player {winner.id()} won!!! CONGRATULATIONS')


if __name__ == "__main__":
    main()