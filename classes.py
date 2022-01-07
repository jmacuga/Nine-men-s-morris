from tabulate import tabulate


class IncorrectCoordsError(Exception):
    pass


class CoordsOfNotActivePoint(Exception):
    pass


class PointOccupiedError(Exception):
    pass


class ImpossibleMove(Exception):
    pass


class FreePointError(Exception):
    pass


class PointOwnerError(Exception):
    pass


class PointInMillError(Exception):
    pass


class Player:
    """ attributes:

        id
        points

        methods:

        place a piece
        # occupied intersections
        move a piece
        # remove an opponent's piece
        fly a piece

        """

    def __init__(self, id):
        self._id = id
        self._occupied = []
        self._mills_list = []
        self._is_mill = False
# points may be redundant - winner is player who removes
# opponents pieces to two or opponent cannot make legal move

    def id(self):
        return self._id

    def occupied(self):
        return self._occupied

    def mills_list(self):
        return self._mills_list

    def is_mill(self):
        return self._is_mill

    def place_piece(self, point: "Point"):
        self._occupied.append(point)
        point.set_owner(self)

    def move_piece(self, point1: "Point", point2: "Point", fly=False):
        # chceck if a point belongs to player,
        # if a move is possible
        # move point
        if point1.owner() == self:
            if point1.coord() in point2.posbl_mov() or fly:
                point1.remove_owner()
                self.place_piece(point2)
            else:
                raise ImpossibleMove("These points are not connected.")
        else:
            raise ImpossibleMove("This piece doesn't belong to this player.")

    def remove_opponents_piece(self, piece):
        if piece in self.occupied():
            raise PointOwnerError("You can only remove an oponent's piece")
        if piece.locked():
            raise PointInMillError("This point is in mill")
        else:
            piece.remove_owner()

    def find_mills(self):
        """find all mills
        check
        -if at least 3 points in player's points are connected
        -if connected points are in the same line

        if list of mills changed and tehre is new mill-- > set  is mill true

        returns list of mills
        """
        mills = []
        for point1 in self.occupied():
            connect_list = [point2 for point2 in self.occupied(
            ) if point1.coord() in point2.posbl_mov()]
            if len(connect_list) >= 2:
                for i in range(2):
                    coords_match = [point for point in connect_list if point.coord()[
                        i] == point1.coord()[i]]
                    if len(coords_match) == 2:
                        coords_match.append(point1)
                        mills.append(coords_match)
                        for point in coords_match:
                            point._locked = True
        if (not mills == self._mills_list) and (len(mills) >= len(self._mills_list)):
            self._is_mill = True
        else:
            self._is_mill = False
        self._mills_list = mills


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

    def __init__(self, coordinates: tuple, posbl_mov: list, taken: bool = False, owner: 'Player' = None, locked=False):
        self._coords = coordinates
        self._posbl_mov = posbl_mov
        self._taken = taken
        self._owner = owner if owner else None
        self._locked = locked

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

    def locked(self):
        return self._locked

    def unlock(self):
        self.owner().find_mills()
        mills = self.owner().mills_list()
        for mill in mills:
            if self in mill:
                for point in mill:
                    point._locked = False

    def taken(self):
        return self._taken

    def set_owner(self, player: "Player" = None):
        if not self._taken:
            self._owner = player
            self._taken = True
        else:
            raise PointOccupiedError("This point is already occupied.")

    def remove_owner(self):
        if self._owner:
            if self._locked:
                self.unlock()
            self._owner._occupied.remove(self)
            self._owner = None
            self._taken = False
        else:
            raise FreePointError("Cannot remove a piece from this point")


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
                   Point((4, 0), [(4, 2), (2, 0), (4, 4)]),
                   Point((4, 2), [(4, 0), (3, 2), (4, 4)]),
                   Point((4, 4), [(4, 2), (2, 4)])
                   ]

        points3 = [Point((0, 0), [(0, 1), (1, 0), (1, 1)]),
                   Point((0, 1), [(0, 0), (1, 1), (0, 2)]),
                   Point((0, 2), [(0, 1), (1, 2), (1, 1)]),
                   Point((1, 0), [(0, 0), (2, 0), (1, 1)]),
                   Point((1, 1), [(0, 0), (1, 0), (2, 0), (0, 1),
                                  (2, 1), (0, 2), (1, 2), (2, 2)]),
                   Point((1, 2), [(0, 2), (1, 2), (1, 1)]),
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

    def print_board(self):
        headers = ""
        for i in range(self._board_size):
            headers+= str(i)
        return tabulate(self.board(), headers= headers, tablefmt="fancy_grid",
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
        board = [["-" for i in range(self._board_size)]
                 for i in range(self._board_size)]
        for point in self._points_list:
            board[point.coord()[0]][point.coord()
                                    [1]] = point.symbol()
        self._board = board
        return board

    def points6(self):
        pass

    def points3(self):
        pass


class Mode:
    def __init__(self, moving=False, flyig=False):
        self._moving = moving
        self._flying = flyig

    def moving(self):
        return self._moving

    def flying(self):
        return self._flying
