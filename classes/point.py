from classes.exceptions import PointOccupiedError, FreePointError
from classes.player import Player


class Point:
    """
    A class representing an active point on the board.

    Atributes
    ---------

    coordinates: tuple
        coordinates on the board
    posbl_mov: list
        list of coordinates of connected points
    owner: Player, optional
        player whose piece is in that point (default is None)
    locked: bool, optional
        true if point is in mill

    Methods
    -------
    symbol()
        symbol of the owner printed on the board
    unlock()
        unlocks point and points in common mill
    set_owner(player=None)
        sets new owner of point
    remove_owner()
        removes current owner
    is_blocked(board)
        returns true if all connected points are occupied
    """

    def __init__(self, coordinates: tuple, posbl_mov: list, owner: Player=None, locked: bool=False):
        self._coords = coordinates
        self._posbl_mov = posbl_mov
        self._owner = owner
        self._locked = locked

    def coord(self):
        return self._coords

    def posbl_mov(self):
        return self._posbl_mov

    def owner(self):
        return self._owner

    def locked(self):
        return self._locked

    def symbol(self) -> str:
        if not self.owner():
            return "•"
        elif self._owner.id() == 1:
            return "O"
        else:
            return "X"

    def unlock(self):
        """unlocks itself and points in common mill"""
        self.owner().find_mills()
        mills = self.owner().mills_list()
        for mill in mills:
            if self in mill:
                for point in mill:
                    point._locked = False

    def set_owner(self, player: Player = None):
        """sets new owner of point

        Raises
        ------
        PointOcupiedError
            if a point already has an owner
        """
        if not self._owner:
            self._owner = player
        else:
            raise PointOccupiedError()

    def remove_owner(self):
        """removes current owner

        sets owner to None, unlocks point
        and removes it from players occupied list

        Raises
        ------
        FreePOintError
            if point doesn't have an owner
        """
        if self._owner:
            if self._locked:
                self.unlock()
            self._owner._occupied.remove(self)
            self._owner = None
        else:
            raise FreePointError()

    def is_blocked(self, board) -> bool:
        """returns true if all connected points are occupied

        Parameters
        ----------
        board : Board
            board of current game
        """
        for point in self.posbl_mov():
            point = board.get_point(point)
            if not point.owner():
                return False
        return True
