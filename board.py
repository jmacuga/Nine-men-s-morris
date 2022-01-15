from point import Point
from tabulate import tabulate
from exceptions import CoordsOfNotActivePoint, IncorrectCoordsError

class Board:
    """ atrruibutes:

        list of points

        methods :

        get point by coordinates
        print board
        generate
    """

    def __init__(self,  pieces_num, board_size):
        points12 = [Point((0, 0), [(0, 3), (1, 1), (3, 0)]),
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

        points9 = [Point((0, 0), [(0, 3), (3, 0)]),
                   Point((0, 3), [(1, 3), (0, 0), (0, 6)]),
                   Point((0, 6), [(0, 3), (3, 6)]),
                   Point((1, 1), [(1, 3), (3, 1)]),
                   Point((1, 3), [(0, 3), (1, 1), (1, 5), (2, 3)]),
                   Point((1, 5), [(1, 3), (3, 5)]),
                   Point((2, 2), [(2, 3), (3, 2)]),
                   Point((2, 3), [(2, 2), (1, 3), (2, 4)]),
                   Point((2, 4), [(2, 3), (3, 4)]),
                   Point((3, 0), [(0, 0), (6, 0), (3, 1)]),
                   Point((3, 1), [(3, 0), (1, 1), (5, 1), (3, 2)]),
                   Point((3, 2), [(2, 2), (3, 1), (4, 2)]),
                   Point((3, 4), [(2, 4), (3, 5), (4, 4)]),
                   Point((3, 5), [(3, 4), (3, 6), (1, 5), (5, 5)]),
                   Point((3, 6), [(3, 5), (0, 6), (6, 6)]),
                   Point((4, 2), [(3, 2), (4, 3)]),
                   Point((4, 3), [(4, 2), (5, 3), (4, 4)]),
                   Point((4, 4), [(4, 3), (3, 4)]),
                   Point((5, 1), [(3, 1), (5, 3)]),
                   Point((5, 3), [(5, 1), (4, 3), (5, 5), (6, 3)]),
                   Point((5, 5), [(5, 3), (3, 5)]),
                   Point((6, 0), [(3, 0), (6, 3)]),
                   Point((6, 3), [(6, 0), (5, 3), (6, 6)]),
                   Point((6, 6), [(6, 3), (3, 6)])
                   ]
        points6 = [Point((0, 0), [(2, 0), (0, 2)]),
                   Point((0, 2), [(0, 0), (0, 4), (1, 2)]),
                   Point((0, 4), [(0, 2), (2, 4)]),
                   Point((1, 1), [(1, 2), (2, 1)]),
                   Point((1, 2), [(1, 1), (1, 3), (0, 2)]),
                   Point((1, 3), [(1, 2), (2, 3)]),
                   Point((2, 0), [(0, 0), (4, 0), (2, 1)]),
                   Point((2, 1), [(2, 0), (1, 1), (3, 1)]),
                   Point((2, 3), [(1, 3), (2, 4), (3, 3)]),
                   Point((2, 4), [(2, 3), (0, 4), (4, 4)]),
                   Point((3, 1), [(3, 2), (2, 1)]),
                   Point((3, 2), [(3, 1), (3, 3), (4, 2)]),
                   Point((3, 3), [(3, 2), (2, 3)]),
                   Point((4, 0), [(4, 2), (2, 0)]),
                   Point((4, 2), [(4, 0), (3, 2), (4, 4)]),
                   Point((4, 4), [(4, 2), (2, 4)])
                   ]

        points3 = [Point((0, 0), [(0, 1), (1, 0), (1, 1)]),
                   Point((0, 1), [(0, 0), (1, 1), (0, 2)]),
                   Point((0, 2), [(0, 1), (1, 2), (1, 1)]),
                   Point((1, 0), [(0, 0), (2, 0), (1, 1)]),
                   Point((1, 1), [(0, 0), (1, 0), (2, 0), (0, 1),
                                  (2, 1), (0, 2), (1, 2), (2, 2)]),
                   Point((1, 2), [(0, 2), (2, 2), (1, 1)]),
                   Point((2, 0), [(2, 1), (1, 0), (1, 1)]),
                   Point((2, 1), [(2, 2), (2, 0), (1, 1)]),
                   Point((2, 2), [(2, 1), (1, 2), (1, 1)])]
        self._pieces_num = pieces_num
        self._board_size = board_size
        points_dict = {12: points12,
                       9: points9,
                       6: points6,
                       3: points3}
        self._points_list = points_dict[self._pieces_num]
        self._points_coord_dict = {
            point.coord(): point for point in self._points_list}

    def points_list(self):
        return self._points_list

    def print_board(self):
        headers = ""
        for i in range(self._board_size):
            headers += str(i)
        return tabulate(self.board(), headers=headers, tablefmt="fancy_grid",
                        showindex=True, numalign="center", stralign="center")

    def get_point(self, coord: tuple):
        if not type(coord) == tuple:
            raise IncorrectCoordsError("Coords must be a tuple.")
        if not len(coord) == 2:
            raise IncorrectCoordsError("Coords must have 2 values x and y.")
        if coord not in self._points_coord_dict:
            raise CoordsOfNotActivePoint("This point is not an active point.")
        return self._points_coord_dict[coord]

    def pieces_num(self):
        return self._pieces_num

    def board_size(self):
        return self._board_size

    def board(self):
        board = [[" " for i in range(self._board_size)]
                 for i in range(self._board_size)]
        for point in self._points_list:
            board[point.coord()[0]][point.coord()
                                    [1]] = point.symbol()
        self._board = board
        return board