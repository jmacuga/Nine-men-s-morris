from classes import Mode, Player, Point, Board
from game import Game
from ui_game import pick_mode
import pytest


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
    inputs = iter(['a','a', '0', '34','adff', '0', '0'])
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

def test_check_phase(monkeypatch):
    game = Game(3)
    player1 = game.player1
    palyer2 = game.player2
    game.set_phase("moving")




