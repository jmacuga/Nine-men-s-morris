from classes.computer_player import ComputerPlayer
import os
from classes.exceptions import CoordsOfNotActivePoint, ImpossibleMove, PointOccupiedError
from classes.exceptions import PointOwnerError, PointInMillError, FreePointError


def clear():
    return os.system('clear')


def pick_mode():
    """Get game mode from user depending on board size."""
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
                print("Wrong mode number, choose from given [1,2,3,4]\n")
                continue
            elif not int(game_mode) in modes:
                print("Wrong mode number, choose from given [1,2,3,4]\n")
                continue
            else:
                valid = True
    except ValueError:
        print("Sorry, try again")
        pick_mode()
    return int(game_mode)


def pick_ai_mode():
    """Get ai mode activation from user."""
    yes_answers = ['y', 'yes']
    no_answers = ['n', 'no']
    print('Do you want to play with computer?[Y/N]')
    answer = input().lower()
    while answer not in yes_answers + no_answers:
        try:
            print('Type "Yes" or "No"')
            answer = input().lower()
        except ValueError:
            print('Sorry, try again')
    return True if answer in yes_answers else False


def pick_player():
    """Get symbol played by user."""
    print(
        "Pick symbol you want to play with [X/O].\nNote 'O' goes always first.")
    symbols = ["x", "o", "0"]
    symbol = input("symbol:").lower()
    while symbol not in symbols:
        print("Enter O or X")
        symbol = input("symbol:").lower()
    return symbol


def make_move(game, board, player):
    """Make move depending on phase.

    PArameters
    ----------
    game : Game
        Current game.
    board : Board
        Current game board.
    player : Player
        Player who is making move.
    """
    print(board)
    if game.phase() == "Placing Pieces":
        print(
            f'Player {player.id()} move\n')
        place_piece(board, player)
    if game.phase() == "Moving":
        print(
            f'Player {player.id()} move\n')
        move_piece(board, player)
    if game.phase() == "Flying":
        print(
            f'Player {player.id()} move\n')
        move_piece(board, player, fly=True)


def place_piece(board, player):
    """Place piece on board.

    Parameters
    ----------
    player : Player
        Player making move.
    """
    print('Enter coordinates to place a piece:\n')
    coords = coords_input()
    try:
        point = board.get_point(coords)
        player.place_piece(point)
    except CoordsOfNotActivePoint:
        clear()
        print(board)
        print("This point is not an active point.\n")
        place_piece(board, player)
    except PointOccupiedError:
        clear()
        print(board)
        print('This point is already occupied. Pick another one.\n')
        place_piece(board, player)


def coords_input():
    """Get coordinates from user."""
    try:
        pointrow = input("row:")
        while not pointrow.isdigit():
            pointrow = input("row:")
        pointcol = input("col:")
        while not pointcol.isdigit():
            pointcol = input("col:")
        coords = (int(pointrow), int(pointcol))
    except ValueError:
        print("Try again")
        coords = coords_input()
    return coords


def move_piece(board, player, fly=False):
    """Move piece on the board.

    Parameters
    ----------
    board : Board
        Board of current game.
    player : Player
        Player who is making move.
    fly : bool, optional
        True if game phase is flying (default is False).
    """
    moved = False
    start_p = False
    while not start_p:
        try:
            if fly:
                print('Enter coordinates to pick a piece you want to fly:\n')
            else:
                print('Enter coordinates to pick a piece you want to move:\n')
            coords1 = coords_input()
            point1 = board.get_point(coords1)
            if point1 not in player.occupied():
                clear()
                print(board)
                raise ImpossibleMove(
                    "This point doesn't belong to you. Pick another one.\n")
            elif point1.is_blocked(board) and not fly:
                raise ImpossibleMove(
                    "This point is blocked. Pick another one.\n")
            start_p = True
        except ImpossibleMove as e:
            clear()
            print(board)
            print(e)
            continue
        except CoordsOfNotActivePoint:
            clear()
            print(board)
            print("This point is not an active point.\n")
            continue
    while not moved:
        try:
            print("Enter coordinates of destination point:\n")
            coords2 = coords_input()
            point2 = board.get_point(coords2)
            player.move_piece(point1, point2, fly)
            moved = True
        except ImpossibleMove:
            clear()
            print(board)
            print("These points are not connected.\n")
            continue
        except PointOccupiedError:
            clear()
            print(board)
            print('This point is already occupied. Pick another one.\n')
            continue
        except CoordsOfNotActivePoint:
            clear()
            print(board)
            print("This point is not an active point.\n")
            continue
        except Exception:
            clear()
            print(board)
            move_piece(board, player, fly)


def remove_piece(board, player):
    """Get from user an opponent's piece to remove and remove it.

    Parameters
    ----------
    board : Board
        Board of current game
    player : Player
        Player who is removing pieces.
    """
    clear()
    print(board)
    print("YOU HAVE A MILL CONGRATULATIONS!!!")
    removed = False
    while not removed:
        try:
            if type(player) == ComputerPlayer:
                point = player.get_remove_point(board)
            else:
                print("Pick opponent's piece to remove:\n")
                coords = coords_input()
                point = board.get_point(coords)
        except CoordsOfNotActivePoint:
            clear()
            print(board)
            print("This point is not an active point.\n")
            continue
        try:
            player.remove_opponents_piece(point)
            removed = True
        except PointOwnerError:
            clear()
            print(board)
            print("You can only remove an oponent's piece.\n")
            continue
        except PointInMillError:
            clear()
            print(board)
            print("This point is in mill.\n")
            continue
        except FreePointError:
            clear()
            print(board)
            print("There is no piece to remove from this point.\n")
            continue
