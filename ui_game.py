from game import Game, ComputerGame
from classes import ComputerPlayer
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


def pick_ai_mode():
    yes_answers = ['y', 'yes']
    no_answers = ['n', 'no']
    print('Do you want to play with computer?[Y/N]')
    answer = input().lower()
    while answer not in yes_answers and answer not in  no_answers:
        try:
            print('Type "Yes" or "No"')
            answer = input().lower()
        except ValueError:
            print('Sorry, try again')
    if answer in yes_answers:
        return True
    else:
        return False



def pick_player():
    print("Pick symbol you wanna play with (Enter O or X).'O' goes always first. ")
    symbols = [ "x", "o"]
    symbol = input("symbol:").lower()
    while symbol not in symbols:
        print("Enter O or X")
        symbol = input("symbol:").lower
    return symbol


def main():
    def clear(): return os.system('clear')
    clear()
    game_mode = pick_mode()
    ai = pick_ai_mode()
    if ai:
        human_symbol = pick_player()
        game = ComputerGame(game_mode, human_symbol)
    else:
        game = Game(game_mode)
    board = game.board()
    clear()
    print(board.print_board())
    while not game.win():
        for player in game.players():
            clear()
            game.check_phase()
            if type(player) == ComputerPlayer:
                game.best_move()
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
