

from classes.game import Game
import pytest
from classes.player import Player
from classes.point import Point
from classes.exceptions import FreePointError, PointOccupiedError, ImpossibleMove


def test_player_class():
    player1 = Player(1)
    player2 = Player(2)
    assert player1.id() == 1
    assert player2._occupied == []


def test_point():
    point00 = Point((0, 0), [(0, 3), (1, 1), (3, 0)])
    assert point00.coord() == (0, 0)
    assert point00.posbl_mov()[0] == (0, 3)
    assert len(point00.posbl_mov()) == 3
    assert not point00.owner()
    assert point00.symbol() == '•'


def test_point_posbl_mov():
    point00 = Point((0, 0), [(0, 3), (1, 1), (3, 0)])
    point03 = Point((0, 3), [(1, 3), (0, 0), (0, 6)])
    assert point00.coord() in point03.posbl_mov()


def test_player_place_piece():
    point00 = Point((0, 0), [(0, 3), (1, 1), (3, 0)])
    player1 = Player(1)
    player1.place_piece(point00)
    assert player1.occupied()[0].coord() == (0, 0)
    assert point00.owner()
    assert point00.owner() == player1
    assert point00.symbol() == "O"


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


def test_player_possible_moves():
    game = Game(2)
    board = game.board()
    points1 = [board.get_point((0, 0)),
               board.get_point((0, 4)),
               board.get_point((1, 1)),
               board.get_point((1, 2)),
               board.get_point((2, 1)),
               board.get_point((2, 3)),
               ]
    points2 = [board.get_point((0, 2)),
               board.get_point((2, 0)),
               board.get_point((1, 3)),
               board.get_point((2, 4)),
               board.get_point((3, 3)),
               board.get_point((3, 1))]
    player1 = game.player1
    player2 = game.player2
    for point in points1:
        player1.place_piece(point)
    for point in points2:
        player2.place_piece(point)
    assert not player1.possible_moves(board)
    assert player2.possible_moves(board)
    assert player1.possible_fly_moves(board)
    assert player2.possible_fly_moves(board)


def test_player_placed_num():
    game = Game(2)
    board = game.board()
    points = [board.get_point((0, 0)),
              board.get_point((0, 4)),
              board.get_point((1, 1)),
              board.get_point((1, 2)),
              board.get_point((2, 1)),
              board.get_point((2, 3)),
              ]
    player1 = game.player1
    for point in points:
        player1.place_piece(point)
    assert player1.placed_num() == 6
