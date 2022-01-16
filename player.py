from exceptions import ImpossibleMove, PointInMillError, PointOccupiedError, PointOwnerError


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
            raise ImpossibleMove("This piece doesn't belong to you.")
        elif point2.owner():
            raise PointOccupiedError()
        elif not point1.coord() in point2.posbl_mov() and not fly:
            raise ImpossibleMove("These points are not connected.")
        else:
            point1.remove_owner()
            self.place_piece(point2)

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

    def possible_moves(self, board):
        moves = []
        for point in self.occupied():
            for nextpoint in board.points_list():
                if nextpoint.coord() in point.posbl_mov() and not nextpoint.owner():
                    moves.append((point, nextpoint))
        return moves

    def possible_fly_moves(self, board):
        fly_moves = []
        for point in self.occupied():
            for nextpoint in board.points_list():
                if not nextpoint.owner():
                    fly_moves.append((point, nextpoint))
        return fly_moves
