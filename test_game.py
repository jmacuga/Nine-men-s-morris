
from game import Game
# import sys
# sys.path.append('../')


def test_check_phase_moving():
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
               board.get_point((4, 4)),
               board.get_point((3, 3)),
               board.get_point((3, 1))]
    player1 = game.player1
    player2 = game.player2
    for point in points1:
        player1.place_piece(point)
    for point in points2:
        player2.place_piece(point)
    assert player1.placed_num() == 6
    assert player2.placed_num() == 6
    assert game.check_if_phase_moving()
    game.check_phase()
    assert game._phase == "moving"


def test_phase_flying_mode3():
    game = Game(3)
    board = game.board()
    game.set_phase("moving")
    player1 = game.player1
    player2 = game.player2
    points1 = [board.get_point((0, 0)),
               board.get_point((0, 3)),
               board.get_point((6, 3))]
    points2 = [board.get_point((6, 6)),
               board.get_point((5, 1)),
               board.get_point((5, 3))]
    for point in points1:
        player1.place_piece(point)
    for point in points2:
        player2.place_piece(point)
    assert game.check_if_phase_flying()
    game.check_phase()
    assert game.phase() == "flying"


def test_check_phase_flyng_mode2():
    game = Game(2)
    board = game.board()
    game.set_phase("moving")
    player1 = game.player1
    player2 = game.player2
    points1 = [board.get_point((0, 0)),
               board.get_point((0, 4)),
               board.get_point((2, 3))]
    points2 = [board.get_point((0, 2)),
               board.get_point((2, 0)),
               board.get_point((3, 1))]
    for point in points1:
        player1.place_piece(point)
    for point in points2:
        player2.place_piece(point)
    assert game.check_if_phase_flying()
    game.check_phase()
    assert game.phase() == "moving"


def test_opponent_removable():
    game = Game(3)
    board = game.board()
    player1 = game.player1
    player2 = game.player2
    points1 = [board.get_point((0, 0)),
               board.get_point((0, 3)),
               board.get_point((0, 6))]
    points2 = [board.get_point((5, 1)),
               board.get_point((3, 0)),
               board.get_point((3, 1))]
    for point in points1:
        player1.place_piece(point)
    for point in points2:
        player2.place_piece(point)
    player1.find_mills()
    player2.find_mills()
    assert not game.opponent_removable(player2)
    assert game.opponent_removable(player1)


def test_check_win_mode_1():
    game = Game(1)
    board = game.board()
    points1 = [board.get_point((0, 0)),
               board.get_point((0, 1)),
               board.get_point((0, 2)),
               ]
    player1 = game.player1
    for point in points1:
        player1.place_piece(point)
    player1.find_mills()
    assert player1.is_mill()
    game.check_win()
    assert game.win()

def test_check_win_mode_2():
    game = Game(2)
    board = game.board()
    game.set_phase("moving")
    player1 = game.player1
    player2 = game.player2
    points1 = [board.get_point((0, 0)),
               board.get_point((0, 4)),]
    points2 = [board.get_point((0, 2)),
               board.get_point((2, 0)),
               board.get_point((3, 1))]
    for point in points1:
        player1.place_piece(point)
    for point in points2:
        player2.place_piece(point)
    game.check_win()
    assert game.win()
    assert game.reveal_winner() == player2

def test_check_win_draw_mode_2():
    game = Game(2)
    board = game.board()
    player1 = game.player1
    player2 = game.player2
    points1 = [board.get_point((0, 0)),
               board.get_point((0, 4)),
               board.get_point((1, 1)),
               board.get_point((1, 2)),
               board.get_point((2, 1)),
               board.get_point((2, 3))
               ]
    points2 = [board.get_point((1, 3)),
               board.get_point((0, 2)),
               board.get_point((2, 0)),
               board.get_point((2, 4)),
               board.get_point((3, 1)),
               board.get_point((3, 3)),
               ]
    for point in points1:
        player1.place_piece(point)
    for point in points2:
        player2.place_piece(point)
    game.check_win()
    assert not player1.possible_moves(board)
    assert game.win()
    assert not game.reveal_winner()

