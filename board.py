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

    def __init__(self,  pieces_num, board_size, points_list):
        self._pieces_num = pieces_num
        self._board_size = board_size

        self._points_list = points_list
        self._points_coord_dict = {
            point.coord(): point for point in self._points_list}

    def points_list(self):
        return self._points_list

    def __str__(self):
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