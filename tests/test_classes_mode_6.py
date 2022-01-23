from classes.game import Game
from classes.player import Player
from classes.exceptions import ImpossibleMove, CoordsOfNotActivePoint
import pytest


def test_board():
    game = Game(2)
    board = game.board()
    assert str(board) == """╒════╤═════╤═════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │  3  │  4  │
╞════╪═════╪═════╪═════╪═════╪═════╡
│ 0  │  •  │     │  •  │     │  •  │
├────┼─────┼─────┼─────┼─────┼─────┤
│ 1  │     │  •  │  •  │  •  │     │
├────┼─────┼─────┼─────┼─────┼─────┤
│ 2  │  •  │  •  │     │  •  │  •  │
├────┼─────┼─────┼─────┼─────┼─────┤
│ 3  │     │  •  │  •  │  •  │     │
├────┼─────┼─────┼─────┼─────┼─────┤
│ 4  │  •  │     │  •  │     │  •  │
╘════╧═════╧═════╧═════╧═════╧═════╛"""


def test_move_piece_imppossible_move():
    game = Game(2)
    board = game.board()
    point00 = board.get_point((0, 0))
    point11 = board.get_point((1, 1))
    player1 = Player(1)
    player1.place_piece(point00)
    with pytest.raises(ImpossibleMove):
        player1.move_piece(point00, point11)
    with pytest.raises(CoordsOfNotActivePoint):
        board.get_point((5, 5))
