from classes.game import Game
from classes.computer_player import ComputerPlayer
import os
from classes.cli import pick_ai_mode, pick_player, make_move, remove_piece, pick_mode


def clear():
    return os.system('clear')

def main():
    """
    Main game function.

    Creates game and loops until game is won.
    """
    clear()
    game_mode = pick_mode()
    ai = pick_ai_mode()
    symbol = None
    if ai:
        symbol = pick_player()
    game = Game(game_mode, ai, symbol)
    human = [p for p in game.players() if type(p) != ComputerPlayer][0]
    board = game.board()
    clear()
    print(board)
    while not game.win():
        for player in game.players():
            clear()
            print(f'Phase: {game.phase()}')
            if type(player) == ComputerPlayer:
                print("Thinking... ")
                player.best_move(game, board, human)
            else:
                make_move(game, board, player)
            if game.check_mills(player):
                remove_piece(board, player)
            game.check_phase()
            game.check_win()
            if game.win():
                break
    clear()
    print(board)
    winner = game.reveal_winner()
    if not winner:
        print("DRAW!!!")
    else:
        print(f'Player {winner.id()} won!!! CONGRATULATIONS')


if __name__ == "__main__":
    main()
