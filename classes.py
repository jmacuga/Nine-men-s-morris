from tabulate import tabulate


class IncorrectCoordsError(Exception):
    pass


class CoordsOfNotActivePoint(Exception):
    pass


class PointOccupiedError(Exception):
    pass


class Player:
    """ attributes:

        id
        points

        methods:

        place a piece
        occupied intersections
        move a piece
        remove an opponent's piece
        fly a piece

        """

    def __init__(self, id, points=0):
        self._id = id
        self._points = points
        self._occupied = []
    # occupied list may be redundant

    def id(self):
        return self._id

    def occupied(self):
        return self._occupied

    def place_piece(self, point: "Point"):
        self._occupied.append(point)
        point.set_owner(self)


class Point:
    """ attributes:

        coordinates
        possible movement points
        taken : True/False
        owner: optional


        methods:
        symbol: "_"/"O","X"
        take by player
        remove

        """

    def __init__(self, coordinates: tuple, posbl_mov: list, taken: bool = False, owner: 'Player' = None):
        self._coords = coordinates
        self._posbl_mov = posbl_mov
        self._taken = taken
        self._owner = owner if owner else None

    def coord(self):
        return self._coords

    def posbl_mov(self):
        return self._posbl_mov

    def symbol(self):
        if not self._taken:
            return []
        elif self._owner.id() == 1:
            return "O"
        else:
            return "X"

    def owner(self):
        return self._owner

    def set_owner(self, player: "Player"):
        if not self._taken:
            self._owner = player
            self._taken = True
        else:
            raise PointOccupiedError("this point is already occupied")


class Board:
    """ atrruibutes:

        list of points

        methods :

        get point by coordinates
        print board
        generate
    """

    def __init__(self):
        self._points_list = [Point((0, 0), [(0, 3), (1, 1), (3, 0)]),
                             Point((0, 3), [(1, 3), (0, 0), (0, 6)]),
                             Point((0, 6), [(0, 3), (1, 5), (3, 6)]),
                             Point((1, 1), [(0, 0), (1, 3), (3, 1), (2, 2)]),
                             Point((1, 3), [(0, 3), (1, 1), (1, 5), (2, 3)]),
                             Point((1, 5), [(0, 6), (1, 3), (3, 5), (2, 4)]),
                             Point((2, 2), [(2, 3), (1, 1), (3, 2)]),
                             Point((2, 3), [(2, 2), (1, 3), (2, 4)]),
                             Point((2, 4), [(2, 3), (3, 4), (1, 5)]),
                             Point((3, 0), [(0, 0), (6, 0), (3, 1)]),
                             Point((3, 1), [(3, 0), (1, 1), (5, 1), (3, 2)]),
                             Point((3, 2), [(2, 2), (3, 1), (4, 2)]),
                             Point((3, 4), [(2, 4), (3, 5), (4, 4)]),
                             Point((3, 5), [(3, 4), (3, 6), (1, 5), (5, 5)]),
                             Point((3, 6), [(3, 5), (0, 6), (6, 6)]),
                             Point((4, 2), [(3, 2), (5, 1), (4, 3)]),
                             Point((4, 3), [(4, 2), (5, 3), (4, 4)]),
                             Point((4, 4), [(4, 3), (3, 4), (5, 5)]),
                             Point((5, 1), [(4, 2), (3, 1), (6, 0), (5, 3)]),
                             Point((5, 3), [(5, 1), (4, 3), (5, 5), (6, 3)]),
                             Point((5, 5), [(5, 3), (4, 4), (3, 5), (6, 6)]),
                             Point((6, 0), [(3, 0), (6, 3), (5, 1)]),
                             Point((6, 3), [(6, 0), (5, 3), (6, 6)]),
                             Point((6, 6), [(6, 3), (5, 5), (3, 6)])
                             ]
        self._board = [[[], "_", "_", [], "_", "_", []],
                       ["_", [], "_", [], "_", [], "_"],
                       ["_", "_", [], [], [], "_", "_"],
                       [[], [], [], "_", [], [], []],
                       ["_", "_", [], [], [], "_", "_"],
                       ["_", [], "_", [], "_", [], "_"],
                       [[], "_", "_", [], "_", "_", []],
                       ]
        self._points_coord_dict = {
            point.coord(): point for point in self._points_list}

    def print_board(self):

        for point in self._points_list:
            self._board[point.coord()[0]][point.coord()
                                          [1]] = point.symbol()
        return tabulate(self._board, headers='0123456', tablefmt="fancy_grid",
                        showindex=True, numalign="center", stralign="center")

    def get_point(self, coord: tuple):
        if not type(coord) == tuple:
            raise IncorrectCoordsError("Coords must be a tuple")
        if not len(coord) == 2:
            raise IncorrectCoordsError("Coords must have 2 values x and y")
        if coord not in self._points_coord_dict:
            raise CoordsOfNotActivePoint("This point is not an active point")
        return self._points_coord_dict[coord]
