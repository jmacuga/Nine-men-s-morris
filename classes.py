from tabulate import tabulate


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
        self._occupied= []

    def id(self):
        return self._id

    def occupied(self):
        return self._occupied

    def place_piece(self, point:"Point"):
        self._occupied.append(point)
        point._owner = self


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
        else:
            if self._owner.player_id() == 1:
                return "O"
            else:
                return "X"


class Board:
    """ atrruibutes:

        list of points

        methods :

        get point by coordinates
        print board
        generate
    """

    def __init__(self, points_list: list = None):
        self._points_list = points_list

    def points_list(self):
        return self._points_list

    def print_board(self):
        board = [[[], "_", "_", [], "_", "_", []],
                 ["_", [], "_", [], "_", [], "_"],
                 ["_", "_", [], [], [], "_", "_"],
                 [[], [], [], "_", [], [], []],
                 ["_", "_", [], [], [], "_", "_"],
                 ["_", [], "_", [], "_", [], "_"],
                 [[], "_", "_", [], "_", "_", []],
                 ]
        for point in self._points_list:
            board[point.coords()[0]][point.coords()
                                     [1]] = point.symbol()
        print(tabulate(board, headers='01234567', tablefmt="fancy_grid",
              showindex="True", numalign="center", stralign="center"))
