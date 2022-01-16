# import sys
# sys.path.append('../')
from cli import coords_input, pick_player, pick_mode, pick_ai_mode, place_piece, move_piece, make_move
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
    board = game.board()
    player1 = game.player1
    palyer2 = game.player2
    inputs = iter(['a', 'a', '0', '34', 'adff', '0', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    make_move(game, board, player1)
    assert game.board().print_board() == """╒════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │
╞════╪═════╪═════╪═════╡
│ 0  │  O  │  •  │  •  │
├────┼─────┼─────┼─────┤
│ 1  │  •  │  •  │  •  │
├────┼─────┼─────┼─────┤
│ 2  │  •  │  •  │  •  │
╘════╧═════╧═════╧═════╛"""


def test_pick_ai_mode(monkeypatch):
    inputs = iter(['e', '9', '?', 'yes'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    ai = pick_ai_mode()
    assert ai


def test_pick_player(monkeypatch):
    inputs = iter(['e', '2', '%', '1', 'x'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    symbol = pick_player()
    assert symbol == 'x'


def test_place_piece(monkeypatch):
    inputs = iter(['e', '2', '%', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    game = Game(1)
    player = game.player1
    board = game.board()
    point21 = board.get_point((2, 1))
    place_piece(board, player)
    assert point21 in player.occupied()


def test_place_piece(monkeypatch):
    inputs = iter(['e', '2', '%', '1', 'x', '2', '1', '30', '70', '2', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    game = Game(1)
    player = game.player1
    board = game.board()
    point21 = board.get_point((2, 1))
    point22 = board.get_point((2, 2))
    place_piece(board, player)
    place_piece(board, player)
    assert point21 in player.occupied()
    assert point22 in player.occupied()


def test_cords_input(monkeypatch):
    inputs = iter(['e', '2', '%', 'ggg', 'x', 'x', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert coords_input() == ((2, 3))
