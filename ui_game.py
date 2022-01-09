from game import Game
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


def main():
    def clear(): return os.system('clear')
    clear()
    game_mode = pick_mode()
    game = Game(game_mode)
    board = game.board()
    clear()
    print(board.print_board())
    while game.win() is False and game.draw() is False:
        for player in game.players():
            clear()
            game.check_phase()
            game.make_move(player)
            game.check_mills(player)
            game.check_win()
            if game.win() or game.draw():
                break
    clear()
    print(board.print_board())
    if game.draw():
        print("DRAW!!!")
    else:
        winner = game.reveal_winner()
        print(f'Player {winner.id()} won!!! CONGRATULATIONS')


if __name__ == "__main__":
    main()
