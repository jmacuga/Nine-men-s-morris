from classes.cli import pick_ai_mode, pick_mode, pick_player, place_piece, move_piece, make_move, coords_input, remove_piece
from classes.game import Game
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


def test_pick_ai_mode(monkeypatch):
    inputs = iter(['e', '2', '%', '1', 'x', 'Y'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    pick_ai_mode()


def test_pick_player(monkeypatch):
    inputs = iter(['e', '2', '%', '1', 'x'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    symbol = pick_player()
    assert symbol == 'x'


def test_place_piece_incorrect_input(monkeypatch):
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


def test_place_piece_letters(monkeypatch):
    inputs = iter(['e', '2', '%', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    game = Game(1)
    player = game.player1
    board = game.board()
    point21 = board.get_point((2, 1))
    place_piece(board, player)
    assert point21 in player.occupied()


def test_make_move_placing(monkeypatch):
    game = Game(1)
    board = game.board()
    player1 = game.player1
    palyer2 = game.player2
    inputs = iter(['a', 'a', '0', '34', 'adff', '0', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    make_move(game, board, player1)
    assert str(game.board()) == """╒════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │
╞════╪═════╪═════╪═════╡
│ 0  │  O  │  •  │  •  │
├────┼─────┼─────┼─────┤
│ 1  │  •  │  •  │  •  │
├────┼─────┼─────┼─────┤
│ 2  │  •  │  •  │  •  │
╘════╧═════╧═════╧═════╛"""


def test_move_piece_correct_input(monkeypatch):
    game = Game(2)
    board = game.board()
    point20 = board.get_point((2, 0))
    point00 = board.get_point((0, 0))
    game.set_phase("Moving")
    player1 = game.player1
    player1.place_piece(point00)
    inputs = iter(['0', '0', '2', '0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    move_piece(board, player1)
    assert point20 in player1.occupied()


def test_move_piece_blocked(monkeypatch):
    game = Game(2)
    board = game.board()
    point13 = board.get_point((1, 3))
    points1 = [board.get_point((0, 0)),
               board.get_point((1, 1)),
               board.get_point((1, 2)),
               ]
    points2 = [board.get_point((0, 2)),
               board.get_point((2, 0))]
    game.set_phase("Moving")
    player1 = game.player1
    player2 = game.player2
    for point in points1:
        player1.place_piece(point)
    for point in points2:
        player2.place_piece(point)
    inputs = iter(['0', '0', '23', '0', '1', '2', 'e', '60', '1', '1', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    move_piece(board, player1)
    assert point13 in player1.occupied()


def test_remove_point_owner_error(monkeypatch):
    game = Game(2)
    board = game.board()
    point02 = board.get_point((0, 2))
    points1 = [board.get_point((0, 0)),
               board.get_point((1, 1)),
               board.get_point((1, 2)),
               ]
    for point in points1:
        game.player1.place_piece(point)
    game.player2.place_piece(point02)
    inputs = iter(['0', '0', '1', '1', '60', 'e', '2', '0', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    remove_piece(board, game.player1)
    assert point02 not in game.player2.occupied()


def test_remove_point_free_error(monkeypatch):
    game = Game(2)
    board = game.board()
    point11 = board.get_point((1, 1))
    point02 = board.get_point((0, 2))
    points1 = [board.get_point((0, 0)),
               board.get_point((1, 2)),
               ]
    for point in points1:
        game.player1.place_piece(point)
    game.player2.place_piece(point11)
    inputs = iter(['0', '2', '1', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    remove_piece(board, game.player1)
    assert point11 not in game.player2.occupied()


def test_remove_point_mill_error(monkeypatch):
    game = Game(2)
    board = game.board()
    player2 = game.player2
    point44 = board.get_point((4, 4))
    points1 = [board.get_point((0, 0)),
               board.get_point((1, 2)),
               board.get_point((1, 1)),
               point44,
               ]
    for point in points1:
        game.player1.place_piece(point)
    inputs = iter(['0', '0', '0', '2 ', '0', '4' '', '4', '4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    remove_piece(board, player2)
    assert point44 not in game.player2.occupied()

