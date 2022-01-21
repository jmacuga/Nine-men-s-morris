from classes.exceptions import ImpossibleMove, PointInMillError, PointOccupiedError, PointOwnerError


class Player:
    """
    class representing player

    Attributtes
    ----------
    id : int
    occupied : list
        list of players pieces as occupied points on board
    mills_list : list
        list of lists of points in one mill
    is_mill : bool
        true if recent move provided a mill
    placed_num : int
        number of placed pieces

    Methods
    -------
    id
    occupied
    mills_list
    is_mill
    placed_num
    place_piece(point)
        places piece on given point
    move_piece(point1, point2)
        moves piece from point1 to point2
    remove_oppponents_piece(point)
        removes piece from given point
    find_mills
        finds mills in occupied points and adds them to mills_list
    possible_moves(board)
        returns possible moves of the occupied points
    possible_fly_moves(board)
        returns possible moves of the occupied points in flying phase
    """

    def __init__(self, id: int):
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
        point.set_owner(self)
        self._occupied.append(point)
        self._placed_num += 1

    def move_piece(self, point1, point2, fly=False):
        # chceck if a point belongs to player,
        # if a move is possible
        # move point
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
        if point in self.occupied():
            raise PointOwnerError()
        if point.locked():
            raise PointInMillError()
        else:
            point.remove_owner()

    def find_mills(self):
        """finds all players mills, locks points and appends to mills_list."""
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
        moves = []
        for point in self.occupied():
            for nextpoint in board.points_list():
                if nextpoint.coord() in point.posbl_mov() and not nextpoint.owner():
                    moves.append((point, nextpoint))
        return moves

    def possible_fly_moves(self, board) -> list:
        fly_moves = []
        for point in self.occupied():
            for nextpoint in board.points_list():
                if not nextpoint.owner():
                    fly_moves.append((point, nextpoint))
        return fly_moves
