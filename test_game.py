
from game import Game
import sys
sys.path.append('../')


def test_player_removable():
    game = Game(1)
    board = game.board()
    player1 = game.player1
    player2 = game.player2
    point00 = board.get_point((0, 0))
    point01 = board.get_point((0, 1))
    point02 = board.get_point((0, 2))
    point10 = board.get_point((1, 0))
    player1.place_piece(point00)
    player1.place_piece(point01)
    player1.place_piece(point02)
    player1.find_mills()
    assert game.player_removable(player2) is False
    player1.move_piece(point00, point10)
    assert game.player_removable(player2)
