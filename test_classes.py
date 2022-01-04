from classes import ImpossibleMove, FreePointError, Player, Point, Board, PointOccupiedError
import pytest


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
    assert point00._taken == False
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
    assert point00._taken == True
    assert point00.owner() == player1
    assert point00.symbol() == "O"


def test_print_board():
    board = Board()
    assert board.print_board() == """╒════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │  3  │  4  │  5  │  6  │
╞════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ 0  │ []  │  _  │  _  │ []  │  _  │  _  │ []  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 1  │  _  │ []  │  _  │ []  │  _  │ []  │  _  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 2  │  _  │  _  │ []  │ []  │ []  │  _  │  _  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 3  │ []  │ []  │ []  │  _  │ []  │ []  │ []  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 4  │  _  │  _  │ []  │ []  │ []  │  _  │  _  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 5  │  _  │ []  │  _  │ []  │  _  │ []  │  _  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 6  │ []  │  _  │  _  │ []  │  _  │  _  │ []  │
╘════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛"""


def test_get_point_by_coord():
    board = Board()
    assert board.get_point((1, 1)).coord() == (1, 1)
    point00 = board.get_point((0, 0))
    point11 = board.get_point((1, 1))
    assert point11.coord() in point00.posbl_mov()


def test_board_status_change():
    board = Board()
    point00 = board.get_point((0, 0))
    player1 = Player(1)
    player2 = Player(2)
    player1.place_piece(point00)
    assert board.print_board() == """╒════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │  3  │  4  │  5  │  6  │
╞════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ 0  │  O  │  _  │  _  │ []  │  _  │  _  │ []  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 1  │  _  │ []  │  _  │ []  │  _  │ []  │  _  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 2  │  _  │  _  │ []  │ []  │ []  │  _  │  _  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 3  │ []  │ []  │ []  │  _  │ []  │ []  │ []  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 4  │  _  │  _  │ []  │ []  │ []  │  _  │  _  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 5  │  _  │ []  │  _  │ []  │  _  │ []  │  _  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 6  │ []  │  _  │  _  │ []  │  _  │  _  │ []  │
╘════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛"""
    point22 = board.get_point((2, 2))
    player2.place_piece(point22)
    assert board.print_board() == """╒════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│    │  0  │  1  │  2  │  3  │  4  │  5  │  6  │
╞════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ 0  │  O  │  _  │  _  │ []  │  _  │  _  │ []  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 1  │  _  │ []  │  _  │ []  │  _  │ []  │  _  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 2  │  _  │  _  │  X  │ []  │ []  │  _  │  _  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 3  │ []  │ []  │ []  │  _  │ []  │ []  │ []  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 4  │  _  │  _  │ []  │ []  │ []  │  _  │  _  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 5  │  _  │ []  │  _  │ []  │  _  │ []  │  _  │
├────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
│ 6  │ []  │  _  │  _  │ []  │  _  │  _  │ []  │
╘════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛"""
    assert player1.occupied()[0] == point00


def test_point_remove_owner():
    board = Board()
    point00 = board.get_point((0, 0))
    player1 = Player(1)
    player1.place_piece(point00)
    point00.remove_owner()
    assert not point00.owner()


def test_point_remove_owner_free_point():
    board = Board()
    point00 = board.get_point((0, 0))
    with pytest.raises(FreePointError):
        point00.remove_owner()


def test_board_players_collision():
    board = Board()
    point00 = board.get_point((0, 0))
    player1 = Player(1)
    player2 = Player(2)
    player1.place_piece(point00)
    with pytest.raises(PointOccupiedError):
        player2.place_piece(point00)


def test_move_piece():
    board = Board()
    point00 = board.get_point((0, 0))
    point11 = board.get_point((1, 1))
    player1 = Player(1)
    player1.place_piece(point00)
    player1.move_piece(point00, point11)
    assert point11._taken
    assert not point00._taken
    assert point11.owner() == player1
    assert point00.owner() == None


def test_move_piece_imppossible_move():
    board = Board()
    point00 = board.get_point((0, 0))
    point66 = board.get_point((6, 6))
    player1 = Player(1)
    player1.place_piece(point00)
    with pytest.raises(ImpossibleMove):
        player1.move_piece(point00, point66)


def test_move_impossible_move_piece_not_owned():
    board = Board()
    point00 = board.get_point((0, 0))
    point11 = board.get_point((1, 1))
    player1 = Player(1)
    with pytest.raises(ImpossibleMove):
        player1.move_piece(point00, point11)


def test_remove_owner():
    board = Board()
    point00 = board.get_point((0, 0))
    player1 = Player(1)
    player1.place_piece(point00)
    point00.remove_owner()
    assert point00.owner() == None
    assert player1.occupied() == []
    assert point00.taken() == False


def test_fly_piece():
    board = Board()
    point00 = board.get_point((0, 0))
    point66 = board.get_point((6, 6))
    player1 = Player(1)
    player1.place_piece(point00)
    player1.move_piece(point00, point66, True)
    assert point00.owner() == None
    assert point66.owner() == player1
