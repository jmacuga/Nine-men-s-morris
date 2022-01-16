# import sys
# sys.path.append('../')
from game import Game
from player import Player
from exceptions import ImpossibleMove
import pytest


def test_move_piece_imppossible_move():
    game = Game(3)
    board = game.board()
    point00 = board.get_point((0, 0))
    point11 = board.get_point((1, 1))
    player1 = Player(1)
    player1.place_piece(point00)
    with pytest.raises(ImpossibleMove):
        player1.move_piece(point00, point11)


def test_print_board():
    game = Game(3)
    board = game.board()
    assert board.print_board() == """╒════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
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
