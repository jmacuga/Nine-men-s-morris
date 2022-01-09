from game import Game
import pytest
from classes import ImpossibleMove, FreePointError, Player, PointOccupiedError
import sys
sys.path.append('../')


def test_print_board():
    game = Game(4)
    board = game.board()
    assert board.print_board() == """╒════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │  3  │  4  │  5  │  6  │
╞════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ 0  │ []  │  -  │  -  │ []  │  -  │  -  │ []  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 1  │  -  │ []  │  -  │ []  │  -  │ []  │  -  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 2  │  -  │  -  │ []  │ []  │ []  │  -  │  -  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 3  │ []  │ []  │ []  │  -  │ []  │ []  │ []  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 4  │  -  │  -  │ []  │ []  │ []  │  -  │  -  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 5  │  -  │ []  │  -  │ []  │  -  │ []  │  -  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 6  │ []  │  -  │  -  │ []  │  -  │  -  │ []  │
╘════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛"""


def test_get_point_by_coord():
    game = Game(4)
    board = game.board()
    assert board.get_point((1, 1)).coord() == (1, 1)
    point00 = board.get_point((0, 0))
    point11 = board.get_point((1, 1))
    assert point11.coord() in point00.posbl_mov()


def test_board_status_change():
    game = Game(4)
    board = game.board()
    point00 = board.get_point((0, 0))
    player1 = Player(1)
    player2 = Player(2)
    player1.place_piece(point00)
    assert board.print_board() == """╒════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │  3  │  4  │  5  │  6  │
╞════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ 0  │  O  │  -  │  -  │ []  │  -  │  -  │ []  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 1  │  -  │ []  │  -  │ []  │  -  │ []  │  -  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 2  │  -  │  -  │ []  │ []  │ []  │  -  │  -  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 3  │ []  │ []  │ []  │  -  │ []  │ []  │ []  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 4  │  -  │  -  │ []  │ []  │ []  │  -  │  -  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 5  │  -  │ []  │  -  │ []  │  -  │ []  │  -  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 6  │ []  │  -  │  -  │ []  │  -  │  -  │ []  │
╘════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛"""
    point22 = board.get_point((2, 2))
    player2.place_piece(point22)
    assert board.print_board() == """╒════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │  3  │  4  │  5  │  6  │
╞════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ 0  │  O  │  -  │  -  │ []  │  -  │  -  │ []  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 1  │  -  │ []  │  -  │ []  │  -  │ []  │  -  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 2  │  -  │  -  │  X  │ []  │ []  │  -  │  -  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 3  │ []  │ []  │ []  │  -  │ []  │ []  │ []  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 4  │  -  │  -  │ []  │ []  │ []  │  -  │  -  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 5  │  -  │ []  │  -  │ []  │  -  │ []  │  -  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 6  │ []  │  -  │  -  │ []  │  -  │  -  │ []  │
╘════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛"""
    assert player1.occupied()[0] == point00


def test_point_remove_owner():
    game = Game(4)
    board = game.board()
    point00 = board.get_point((0, 0))
    player1 = Player(1)
    player1.place_piece(point00)
    point00.remove_owner()
    assert not point00.owner()


def test_point_remove_owner_free_point():
    game = Game(4)
    board = game.board()
    point00 = board.get_point((0, 0))
    with pytest.raises(FreePointError):
        point00.remove_owner()


def test_board_players_collision():
    game = Game(4)
    board = game.board()
    point00 = board.get_point((0, 0))
    player1 = Player(1)
    player2 = Player(2)
    player1.place_piece(point00)
    with pytest.raises(PointOccupiedError):
        player2.place_piece(point00)


def test_move_piece():
    game = Game(4)
    board = game.board()
    point00 = board.get_point((0, 0))
    point11 = board.get_point((1, 1))
    player1 = Player(1)
    player1.place_piece(point00)
    player1.move_piece(point00, point11)
    assert point11.owner()
    assert not point00.owner()
    assert point11.owner() == player1
    assert point00.owner() == None


def test_move_piece_imppossible_move():
    game = Game(4)
    board = game.board()
    point00 = board.get_point((0, 0))
    point66 = board.get_point((6, 6))
    player1 = Player(1)
    player1.place_piece(point00)
    with pytest.raises(ImpossibleMove):
        player1.move_piece(point00, point66)


def test_move_impossible_move_piece_not_owned():
    game = Game(4)
    board = game.board()
    point00 = board.get_point((0, 0))
    point11 = board.get_point((1, 1))
    player1 = Player(1)
    with pytest.raises(ImpossibleMove):
        player1.move_piece(point00, point11)


def test_remove_owner():
    game = Game(4)
    board = game.board()
    point00 = board.get_point((0, 0))
    player1 = Player(1)
    player1.place_piece(point00)
    point00.remove_owner()
    assert point00.owner() == None
    assert player1.occupied() == []
    assert not point00.owner()


def test_fly_piece():
    game = Game(4)
    board = game.board()
    point00 = board.get_point((0, 0))
    point66 = board.get_point((6, 6))
    player1 = Player(1)
    player1.place_piece(point00)
    player1.move_piece(point00, point66, True)
    assert point00.owner() == None
    assert point66.owner() == player1
