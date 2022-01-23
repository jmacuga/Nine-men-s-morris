from classes.game import Game
import pytest
from classes.player import Player
from classes.exceptions import PointInMillError


def test_find_mils():
    game = Game(4)
    board = game.board()
    player1 = Player(1)
    point00 = board.get_point((0, 0))
    point11 = board.get_point((1, 1))
    point03 = board.get_point((0, 3))
    point06 = board.get_point((0, 6))
    player1.place_piece(point00)
    player1.place_piece(point11)
    player1.place_piece(point03)
    player1.place_piece(point06)
    player1.find_mills()
    mills = player1.mills_list()
    assert len(mills) == 1
    assert point00 in mills[0]
    assert point03 in mills[0]
    assert point06 in mills[0]


def test_find_mills():
    game = Game(4)
    board = game.board()
    point51 = board.get_point((5, 1))
    point53 = board.get_point((5, 3))
    point55 = board.get_point((5, 5))
    point43 = board.get_point((4, 3))
    point44 = board.get_point((4, 4))
    player1 = Player(1)
    player1.place_piece(point51)
    player1.place_piece(point53)
    player1.place_piece(point55)
    player1.place_piece(point43)
    player1.place_piece(point44)
    player1.find_mills()
    mills = player1.mills_list()
    assert len(mills) == 1
    assert len(mills[0]) == 3
    assert point51 in mills[0]
    assert point53 in mills[0]
    assert point55 in mills[0]


def test_find_mills_eq_2():
    game = Game(4)
    player1 = Player(1)
    board = game.board()
    coords = [(5, 3), (5, 1), (5, 5), (4, 3), (4, 4), (6, 3)]
    points = list(map(board.get_point, coords))
    list(map(player1.place_piece, points))

    player1.find_mills()
    mills = player1.mills_list()
    assert len(mills) == 2


def test_find_mills_middle_case():
    game = Game(4)
    board = game.board()
    player = Player(1)
    coords = [(3, 0), (3, 2), (3, 4), (2, 2)]
    points = list(map(board.get_point, coords))
    list(map(player.place_piece, points))
    mills = player.mills_list()
    assert mills == []


def test_find_mills_all_points():
    game = Game(4)
    board = game.board()
    player = Player(1)
    player._occupied = board._points_list
    player.find_mills()
    mills = player.mills_list()
    assert len(mills) == 16


def test_locked_mills():
    game = Game(4)
    board = game.board()
    point00 = board.get_point((0, 0))
    point03 = board.get_point((0, 3))
    point06 = board.get_point((0, 6))
    point11 = board.get_point((1, 1))
    player1 = Player(1)
    player2 = Player(2)
    player1.place_piece(point00)
    player1.place_piece(point03)
    player1.place_piece(point06)
    player1.find_mills()
    mills = player1.mills_list()
    with pytest.raises(PointInMillError):
        player2.remove_opponents_piece(point00)
    player1.move_piece(point00, point11)
    player2.remove_opponents_piece(point11)
    assert point11.owner() == None
    assert point11.locked() == False


def test_locked_1p_2mills():
    game = Game(4)
    board = game.board()
    point51 = board.get_point((5, 1))
    point53 = board.get_point((5, 3))
    point55 = board.get_point((5, 5))
    point43 = board.get_point((4, 3))
    point44 = board.get_point((4, 4))
    point63 = board.get_point((6, 3))
    point42 = board.get_point((4, 2))
    player1 = Player(1)
    player2 = Player(2)
    player1.place_piece(point51)
    player1.place_piece(point53)
    player1.place_piece(point55)
    player1.place_piece(point43)
    player1.place_piece(point44)
    player1.place_piece(point63)
    player1.find_mills()
    mills = player1.mills_list()
    with pytest.raises(PointInMillError):
        player2.remove_opponents_piece(point51)
    player1.move_piece(point43, point42)
    player2.remove_opponents_piece(point63)
    assert point63.owner() == None
    assert point63.locked() == False
    assert point53.locked() == False


def test_checking_last_mill():
    game = Game(4)
    board = game.board()
    point00 = board.get_point((0, 0))
    point11 = board.get_point((1, 1))
    point03 = board.get_point((0, 3))
    point06 = board.get_point((0, 6))
    point30 = board.get_point((3, 0))
    player1 = Player(1)
    assert player1.is_mill() == False
    player1.place_piece(point00)
    player1.place_piece(point11)
    player1.place_piece(point03)
    player1.place_piece(point06)
    player1.find_mills()
    assert player1.is_mill() == True
    player1.move_piece(point00, point30)
    assert player1.is_mill() == False


def test_checking_last_mill_2():
    game = Game(4)
    board = game.board()
    point00 = board.get_point((0, 0))
    point11 = board.get_point((1, 1))
    point03 = board.get_point((0, 3))
    point06 = board.get_point((0, 6))
    point30 = board.get_point((3, 0))
    player1 = Player(1)
    assert player1.is_mill() == False
    player1.place_piece(point00)
    player1.place_piece(point11)
    player1.place_piece(point03)
    player1.place_piece(point06)
    player1.find_mills()
    assert player1.is_mill() == True
    player1.place_piece(point30)
    player1.find_mills()
    assert player1.is_mill() == False


def test_3_mode():
    game = Game(1)
    board = game.board()
    coords1 = [(0, 0), (2, 0), (2, 2)]
    coords2 = [(1, 0), (0, 2), (1, 2)]
    player1 = Player(1)
    player2 = Player(2)
    points1 = list(map(board.get_point, coords1))
    points2 = list(map(board.get_point, coords2))
    list(map(player1.place_piece, points1))
    list(map(player2.place_piece, points2))
    assert player1.is_mill() == False
    player1.find_mills()
    player2.find_mills()
    assert player1.is_mill() == False
    assert player2.is_mill() == False
