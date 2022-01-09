# import sys
# sys.path.append('../')
from classes import Player, Point, Board
from ui_game import pick_mode
from game import Game
import pytest
import os


def test_pick_mode(monkeypatch):
    inputs = iter(['1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pick_mode() == 1


def test_pick_mode_letter(monkeypatch):
    inputs = iter(['e', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pick_mode() == 2


def test_pick_mode_float(monkeypatch):
    inputs = iter(['3.5', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert pick_mode() == 2


def test_place_piece(monkeypatch):
    game = Game(1)
    player1 = game.player1
    palyer2 = game.player2
    inputs = iter(['a', 'a', '0', '34', 'adff', '0', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    game.make_move(player1)
    assert game.board().print_board() == """╒════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │
╞════╪═════╪═════╪═════╡
│ 0  │  O  │ []  │ []  │
├────┼─────┼─────┼─────┤
│ 1  │ []  │ []  │ []  │
├────┼─────┼─────┼─────┤
│ 2  │ []  │ []  │ []  │
╘════╧═════╧═════╧═════╛"""

# def test_check_phase(monkeypatch):
#     game = Game(3)
#     player1 = game.player1
#     palyer2 = game.player2
#     game.set_phase("moving")


# def moving():
#     def clear(): return os.system('clear')
#     clear()
#     game = Game(2)
#     player1 = game.player1
#     player2 = game.player2
#     board = game.board()
#     point00 = board.get_point((0, 0))
#     point02 = board.get_point((0, 2))
#     point04 = board.get_point((0, 4))
#     point11 = board.get_point((1, 1))
#     player1.place_piece(point00)
#     player1.place_piece(point02)
#     player2.place_piece(point04)
#     player2.place_piece(point11)
#     game.set_phase("flying")
#     print(board.print_board())
#     while game.win() == False:
#         for player in [player1, player2]:
#             clear()
#             game.check_phase()
#             game.make_move(player)
#             game.check_mills(player)


# moving()
