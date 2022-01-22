from classes.point import Point
from tabulate import tabulate
from classes.exceptions import CoordsOfNotActivePoint, IncorrectCoordsError


class Board:
    """
    A class to represent board.

    Atrruibutes
    -----------
    pieces_num : int
        Number of pieces per player in game mode.
    board_size : int
        Size of the board in the game mode.
    points_list : list
        List of active points on the board.
    points_coord_dict : dict
        Dictionary where keys are coordinates, values are points.
    """

    def __init__(self,  pieces_num, board_size, points_list):
        """
        Parameters
        ----------
        pieces_num : int
            Number of pieces per player in game mode.
        board_size : int
            Size of the board in the game mode.
        points_list : list
            List of active points on the board.
        """
        self._pieces_num = pieces_num
        self._board_size = board_size
        self._points_list = points_list
        self._points_coord_dict = {
            point.coord(): point for point in self._points_list}

    def pieces_num(self):
        return self._pieces_num

    def points_list(self) -> list:
        return self._points_list

    def board_size(self):
        return self._board_size

    def __str__(self):
        """Print board."""
        headers = ""
        for i in range(self._board_size):
            headers += str(i)
        return tabulate(self.board(), headers=headers, tablefmt="fancy_grid",
                        showindex=True, numalign="center", stralign="center")

    def get_point(self, coord: tuple) -> Point:
        """
        Return point of given coordinates.

        Parameters
        ----------
        coord: tuple
            The coordinates of the point.
        """
        if not type(coord) == tuple:
            raise TypeError()
        if not len(coord) == 2:
            raise IncorrectCoordsError("Coords must have 2 values x and y.")
        if coord not in self._points_coord_dict:
            raise CoordsOfNotActivePoint()
        return self._points_coord_dict[coord]

    def board(self) -> list:
        """Generate list of symbols for each point on the board."""
        board = [[" " for i in range(self._board_size)]
                 for i in range(self._board_size)]
        for point in self._points_list:
            board[point.coord()[0]][point.coord()
                                    [1]] = point.symbol()
        self._board = board
        return board
