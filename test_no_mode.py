from classes import Player, Point
from game import Game


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
    assert point00.symbol() == []


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
