from classes.game import Game

def test_block_place1_mode1():
    game = Game(1, True, 'o')
    board = game.board()
    player2 = game.player2
    player1 = game.player1
    cords2 = [(0, 1)]
    cords1 = [(0, 0), (1, 0)]
    p20 = board.get_point((2, 0))
    pieces2 = list(map(board.get_point, cords2))
    pieces1 = list(map(board.get_point, cords1))
    list(map(player2.place_piece, pieces2))
    list(map(player1.place_piece, pieces1))
    player2.best_move(game, board, player1)
    assert p20 in player2.occupied()


def test_block_move1_mode1():
    game = Game(1, True, 'x')
    board = game.board()
    player2 = game.player2
    player1 = game.player1
    cords2 = [(0, 0), (0, 1), (2, 2)]
    cords1 = [(1, 0), (1, 1), (0, 2)]
    p12 = board.get_point((1, 2))
    pieces2 = list(map(board.get_point, cords2))
    pieces1 = list(map(board.get_point, cords1))
    list(map(player2.place_piece, pieces2))
    list(map(player1.place_piece, pieces1))
    game.check_phase()
    player1.best_move(game, board, player1)
    c = [p.coord() for p in player2.occupied()]
    assert game.phase() == "Moving"
    assert p12 in player1.occupied()


def test_block_move2_mode1():
    game = Game(1, True, 'x')
    board = game.board()
    player2 = game.player2
    player1 = game.player1
    cords2 = [(0, 0), (0, 1), (2, 2)]
    cords1 = [(1, 0), (1, 1), (0, 2)]
    p12 = board.get_point((1, 2))
    pieces2 = list(map(board.get_point, cords2))
    pieces1 = list(map(board.get_point, cords1))
    list(map(player2.place_piece, pieces2))
    list(map(player1.place_piece, pieces1))
    game.check_phase()
    player1.best_move(game, board, player1)
    c = [p.coord() for p in player2.occupied()]
    assert game.phase() == "Moving"
    assert p12 in player1.occupied()


def test_make_mill_mode1():
    game = Game(1, True, 'o')
    board = game.board()
    player2 = game.player2
    player1 = game.player1
    cords2 = [(1, 0), (0, 1), (1, 2)]
    cords1 = [(0, 0), (2, 1), (0, 2)]
    p11 = board.get_point((1, 1))
    pieces2 = list(map(board.get_point, cords2))
    pieces1 = list(map(board.get_point, cords1))
    list(map(player2.place_piece, pieces2))
    list(map(player1.place_piece, pieces1))
    game.check_phase()
    player2.best_move(game, board, player1)
    c = [p.coord() for p in player2.occupied()]
    assert game.phase() == "Moving"
    assert p11 in player2.occupied()


def test_block_mode2():
    game = Game(2, True, 'x')
    board = game.board()
    player2 = game.player2
    player1 = game.player1
    cords2 = [(0, 4), (1, 1), (4, 4)]
    cords1 = [(0, 0), (0, 2), (1, 2)]
    p24 = board.get_point((2, 4))
    pieces2 = list(map(board.get_point, cords2))
    pieces1 = list(map(board.get_point, cords1))
    list(map(player2.place_piece, pieces2))
    list(map(player1.place_piece, pieces1))
    player1.best_move(game, board, player2)
    assert p24 in player1.occupied()


def test_block_2_mode2():
    game = Game(2, True, "x")
    board = game.board()
    player1 = game.player1
    player2 = game.player2
    cords1 = [(0, 0), (0, 2)]
    cords2 = [(0, 4), (4, 0)]
    pieces1 = list(map(board.get_point, cords1))
    pieces2 = list(map(board.get_point, cords2))
    p24 = board.get_point((2, 4))
    list(map(player2.place_piece, pieces2))
    list(map(player1.place_piece, pieces1))
    player1.best_move(game, board, player2)
    assert p24 in player1.occupied()


def test_block_3_mode2():
    game = Game(2, True, "x")
    board = game.board()
    player1 = game.player1
    player2 = game.player2
    cords1 = [(0, 0), (0, 2), (1, 1), (2, 3), (2, 4)]
    cords2 = [(0, 4), (4, 0), (1, 3), (4, 4)]
    pieces1 = list(map(board.get_point, cords1))
    pieces2 = list(map(board.get_point, cords2))
    p42 = board.get_point((4, 2))
    list(map(player2.place_piece, pieces2))
    list(map(player1.place_piece, pieces1))
    player1.best_move(game, board, player2)
    assert p42 in player1.occupied()


def test_block_mode3():
    game = Game(3, True, "x")
    board = game.board()
    player1 = game.player1
    player2 = game.player2
    cords1 = [(0, 0), (0, 3)]
    cords2 = [(0, 6), (6, 6)]
    pieces1 = list(map(board.get_point, cords1))
    pieces2 = list(map(board.get_point, cords2))
    p36 = board.get_point((3, 6))
    list(map(player2.place_piece, pieces2))
    list(map(player1.place_piece, pieces1))
    player1.best_move(game, board, player2)
    assert p36 in player1.occupied()


def test_make_mill_mode3():
    game = Game(3, True, "x")
    board = game.board()
    player1 = game.player1
    player2 = game.player2
    cords1 = [(0, 0), (0, 3), (1, 3), (3, 6), (6, 3)]
    cords2 = [(0, 6), (6, 0), (1, 1), (5, 5)]
    pieces1 = list(map(board.get_point, cords1))
    pieces2 = list(map(board.get_point, cords2))
    p23 = board.get_point((2, 3))
    list(map(player2.place_piece, pieces2))
    list(map(player1.place_piece, pieces1))
    player1.best_move(game, board, player2)
    c = [p.coord() for p in player1.occupied()]
    c
    assert p23 in player1.occupied()


def test_move_mill_mode3():
    game = Game(3, True, "x")
    board = game.board()
    player1 = game.player1
    player2 = game.player2
    cords1 = [ (1, 1), (1,5), (2, 2), (2, 4), (3, 0), (5, 1)]
    cords2 = [(0, 6), (2, 3), (3, 2), (3, 6),
              (6, 3), (6, 0), (5, 5), (6, 6)]
    pieces1 = list(map(board.get_point, cords1))
    pieces2 = list(map(board.get_point, cords2))
    p31 = board.get_point((3, 1))
    list(map(player2.place_piece, pieces2))
    list(map(player1.place_piece, pieces1))
    game.set_phase("Moving")
    game.check_mills(player2)
    game.check_mills(player2)
    player1.best_move(game, board, player2)
    assert p31 in player1.occupied()
