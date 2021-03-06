from classes.game import Game
from classes.player import Player


def test_place_piece():
    game = Game(1)
    board = game.board()
    point00 = board.get_point((0, 0))
    player1 = Player(1)
    player1.place_piece(point00)
    assert point00._owner == player1


def test_board():
    game = Game(1)
    board = game.board()
    assert str(board) == """╒════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │
╞════╪═════╪═════╪═════╡
│ 0  │  •  │  •  │  •  │
├────┼─────┼─────┼─────┤
│ 1  │  •  │  •  │  •  │
├────┼─────┼─────┼─────┤
│ 2  │  •  │  •  │  •  │
╘════╧═════╧═════╧═════╛"""
