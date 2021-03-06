from classes.game import Game
from classes.player import Player


def test_print_board():
    game = Game(4)
    board = game.board()
    assert str(board) == """╒════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │  3  │  4  │  5  │  6  │
╞════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ 0  │  •  │     │     │  •  │     │     │  •  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 1  │     │  •  │     │  •  │     │  •  │     │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 2  │     │     │  •  │  •  │  •  │     │     │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 3  │  •  │  •  │  •  │     │  •  │  •  │  •  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 4  │     │     │  •  │  •  │  •  │     │     │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 5  │     │  •  │     │  •  │     │  •  │     │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 6  │  •  │     │     │  •  │     │     │  •  │
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
    assert str(board) == """╒════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │  3  │  4  │  5  │  6  │
╞════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ 0  │  O  │     │     │  •  │     │     │  •  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 1  │     │  •  │     │  •  │     │  •  │     │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 2  │     │     │  •  │  •  │  •  │     │     │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 3  │  •  │  •  │  •  │     │  •  │  •  │  •  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 4  │     │     │  •  │  •  │  •  │     │     │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 5  │     │  •  │     │  •  │     │  •  │     │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 6  │  •  │     │     │  •  │     │     │  •  │
╘════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛"""
    point22 = board.get_point((2, 2))
    player2.place_piece(point22)
    assert str(board) == """╒════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │  3  │  4  │  5  │  6  │
╞════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ 0  │  O  │     │     │  •  │     │     │  •  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 1  │     │  •  │     │  •  │     │  •  │     │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 2  │     │     │  X  │  •  │  •  │     │     │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 3  │  •  │  •  │  •  │     │  •  │  •  │  •  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 4  │     │     │  •  │  •  │  •  │     │     │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 5  │     │  •  │     │  •  │     │  •  │     │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 6  │  •  │     │     │  •  │     │     │  •  │
╘════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛"""
    assert player1.occupied()[0] == point00
