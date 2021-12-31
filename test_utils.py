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
    assert len(utils.find_mills(player1)) == 1


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
print(utils.find_mills(player1))
