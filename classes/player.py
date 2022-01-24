from classes.exceptions import ImpossibleMove, PointInMillError, PointOccupiedError, PointOwnerError


class Player:
    """
    Class representing player.

    Attributtes
    ----------
    id : int
        Players id.
    occupied : list
        List of players pieces as occupied points on board.
    mills_list : list
        List of lists of points in one mill.
    is_mill : bool
        Rrue if recent move provided a mill.
    placed_num : int
        Number of placed pieces.
    """

    def __init__(self, id: int):
        """
        Parameters
        ----------
        id : int
            Players id.
        """
        self._id = id
        self._occupied = []
        self._mills_list = []
        self._is_mill = False
        self._placed_num = 0

    def id(self):
        return self._id

    def occupied(self):
        return self._occupied

    def mills_list(self):
        return self._mills_list

    def is_mill(self):
        return self._is_mill

    def placed_num(self):
        return self._placed_num

    def place_piece(self, point):
        """
        Place piece on given point.

        Parameters
        ----------
        point : Point
            Point to place a piece.
        """
        point.set_owner(self)
        self._occupied.append(point)
        self._placed_num += 1

    def move_piece(self, point1, point2, fly=False):
        """
        Move players piece.

        Parameters
        ----------
        point1 : Point
            Moving piece.
        point2 : Point
            Destinatinon point.
        fly : bool, optional
            True if move is in flying phase (default is False).
        """
        if point1.owner() != self:
            raise ImpossibleMove()
        elif point2.owner():
            raise PointOccupiedError()
        elif not point1.coord() in point2.posbl_mov() and not fly:
            raise ImpossibleMove()
        else:
            point1.remove_owner()
            self.place_piece(point2)

    def remove_opponents_piece(self, point):
        """
        Remove opponent's piece from given point.

        Parameters
        ----------
        point : Point
            Piece to remove.
        """
        if point in self.occupied():
            raise PointOwnerError()
        if point.locked():
            raise PointInMillError()
        else:
            point.remove_owner()

    def find_mills(self):
        """Finds all players mills, locks points and appends to mills_list."""
        mills = []
        for point1 in self.occupied():
            connect_list = [point2 for point2 in self.occupied()
                            if point1.coord() in point2.posbl_mov()]
            if len(connect_list) >= 2:
                for i in range(2):
                    coords_match = [point for point in connect_list
                                    if point.coord()[i] == point1.coord()[i]]
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

    def possible_moves(self, board) -> list:
        """
        Get players possible moves.

        Parameters
        ----------
        board : Board
            Board of current game.
        """
        moves = []
        for point in self.occupied():
            for nextpoint in board.points_list():
                if nextpoint.coord() in point.posbl_mov() and not nextpoint.owner():
                    moves.append((point, nextpoint))
        return moves

    def possible_fly_moves(self, board) -> list:
        """
        Get players possible fly moves.

        Parameters
        ----------
        board : Board
            Board of current game.
        """
        fly_moves = []
        for point in self.occupied():
            for nextpoint in board.points_list():
                if not nextpoint.owner():
                    fly_moves.append((point, nextpoint))
        return fly_moves
