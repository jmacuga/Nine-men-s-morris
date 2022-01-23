from classes.game import Game


def test_check_phase_moving():
    game = Game(2)
    board = game.board()
    player1 = game.player1
    player2 = game.player2
    coords1 = [(0, 0), (0, 4), (1, 1), (1, 2), (2, 1), (2, 3)]
    coords2 = [(0, 2), (2, 0), (1, 3), (4, 4), (3, 3), (3, 1)]
    points1 = list(map(board.get_point, coords1))
    points2 = list(map(board.get_point, coords2))
    list(map(player1.place_piece, points1))
    list(map(player2.place_piece, points2))
    assert player1.placed_num() == 6
    assert player2.placed_num() == 6
    assert game.check_if_phase_moving()
    game.check_phase()
    assert game._phase == "Moving"


def test_phase_flying_mode3():
    game = Game(3)
    board = game.board()
    game.set_phase("Moving")
    player1 = game.player1
    player2 = game.player2
    coords1 = [(0, 0), (0, 3), (3, 6)]
    coords2 = [(6, 6), (5, 1), (5, 3)]
    points1 = list(map(board.get_point, coords1))
    points2 = list(map(board.get_point, coords2))
    list(map(player1.place_piece, points1))
    list(map(player2.place_piece, points2))
    assert game.check_if_phase_flying()
    game.check_phase()
    assert game.phase() == "Flying"


def test_check_phase_flyng_mode2():
    game = Game(2)
    board = game.board()
    game.set_phase("Moving")
    player1 = game.player1
    player2 = game.player2
    coords1 = [(0, 0), (0, 4), (2, 3)]
    coords2 = [(0, 2), (2, 0), (3, 1)]
    points1 = list(map(board.get_point, coords1))
    points2 = list(map(board.get_point, coords2))
    list(map(player1.place_piece, points1))
    list(map(player2.place_piece, points2))
    assert game.check_if_phase_flying()
    game.check_phase()
    assert game.phase() == "Moving"


def test_opponent_removable():
    game = Game(3)
    board = game.board()
    player1 = game.player1
    player2 = game.player2
    coords1 = [(0, 0), (0, 3), (0, 6)]
    coords2 = [(5, 1), (3, 0), (3, 1)]
    points1 = list(map(board.get_point, coords1))
    points2 = list(map(board.get_point, coords2))
    list(map(player1.place_piece, points1))
    list(map(player2.place_piece, points2))
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
    list(map(player1.place_piece, points1))
    player1.find_mills()
    assert player1.is_mill()
    game.check_win()
    assert game.win()


def test_check_win_mode_2():
    game = Game(2)
    board = game.board()
    game.set_phase("Moving")
    player1 = game.player1
    player2 = game.player2
    coords1 = [(0, 0), (0, 4)]
    coords2 = [(0, 2), (2, 0), (3, 1)]
    points1 = list(map(board.get_point, coords1))
    points2 = list(map(board.get_point, coords2))
    list(map(player1.place_piece, points1))
    list(map(player2.place_piece, points2))
    game.check_win()
    assert game.win()
    assert game.reveal_winner() == player2


def test_check_win_draw_mode_2():
    game = Game(2)
    board = game.board()
    player1 = game.player1
    player2 = game.player2
    coords1 = [(0, 0), (0, 4), (1, 1), (1, 2), (2, 1), (2, 3)]
    coords2 = [(0, 2), (2, 0), (3, 1), (1, 3), (2, 4), (3, 3)]
    points1 = list(map(board.get_point, coords1))
    points2 = list(map(board.get_point, coords2))
    list(map(player1.place_piece, points1))
    list(map(player2.place_piece, points2))
    game.check_phase()
    game.check_win()
    assert game.phase() == "Moving"
    assert not player1.possible_moves(board)
    assert game.win()
    assert not game.reveal_winner()


def test_check_mills_mode_1():
    game = Game(1)
    board = game.board()
    player1 = game.player1
    coords1 = [(0, 0),(0, 1),(0, 2)]
    points1 = list(map(board.get_point, coords1))
    list(map(player1.place_piece, points1))
    assert game.check_mills(player1) is False


def test_check_mills_player_not_removable():
    game = Game(2)
    board = game.board()
    player1 = game.player1
    player2 = game.player2
    coords1 = [(0, 0),(0, 2),(0, 4)]
    coords2 = [(1, 1), (1, 2), (1, 3)]
    points1 = list(map(board.get_point, coords1))
    points2 = list(map(board.get_point, coords2))
    list(map(player1.place_piece, points1))
    list(map(player2.place_piece, points2))
    player1.find_mills()
    assert game.opponent_removable(player2) is False
    assert game.check_mills(player2) is False
