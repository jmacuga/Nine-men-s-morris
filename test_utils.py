from classes import Player, Point, Board
import utils


def test_get_mils():
    board = Board()
    point00 = board.get_point((0, 0))
    point11 = board.get_point((1, 1))
    point03 = board.get_point((0, 3))
    point06 = board.get_point((0, 6))
    player1 = Player(1)
    player1.place_piece(point00)
    player1.place_piece(point11)
    player1.place_piece(point03)
    player1.place_piece(point06)
    mills = utils.find_mills(player1)
    assert len(mills) == 1
    assert point00 in mills[0]
    assert point03 in mills[0]
    assert point06 in mills[0]

def test_get_mills():
    board = Board()
    point51 = board.get_point((5,1))
    point53 = board.get_point((5,3))
    point55 = board.get_point((5,5))
    point43 = board.get_point((4,3))
    point44 = board.get_point((4,4))
    point63 = board.get_point((6,3))
    player1 = Player(1)
    player1.place_piece(point51)
    player1.place_piece(point53)
    player1.place_piece(point55)
    player1.place_piece(point43)
    player1.place_piece(point44)
    mills = utils.find_mills(player1)
    assert len(mills) == 1
    assert len(mills[0]) == 3
    assert point51 in mills[0]
    assert point53 in mills[0]
    assert point55 in mills[0]

def test_get_mills_eq_2():
    board = Board()
    point51 = board.get_point((5,1))
    point53 = board.get_point((5,3))
    point55 = board.get_point((5,5))
    point43 = board.get_point((4,3))
    point44 = board.get_point((4,4))
    point63 = board.get_point((6,3))
    player1 = Player(1)
    player1.place_piece(point51)
    player1.place_piece(point53)
    player1.place_piece(point55)
    player1.place_piece(point43)
    player1.place_piece(point44)
    player1.place_piece(point63)
    mills = utils.find_mills(player1)
    assert len(mills) == 2


# board = Board()
# point00 = board.get_point((0, 0))
# point11 = board.get_point((1, 1))
# point03 = board.get_point((0, 3))
# point06 = board.get_point((0, 6))
# player1 = Player(1)
# player1.place_piece(point00)
# player1.place_piece(point11)
# player1.place_piece(point03)
# player1.place_piece(point06)
# print(utils.find_mills(player1))
