from classes.exceptions import PointOccupiedError, FreePointError
from classes.player import Player


class Point:
    """
    A class representing an active point on the board.

    Atributes
    ---------
    coordinates: tuple
        Coordinates on the board.
    posbl_mov: list
        List of coordinates of connected points.
    owner: Player, optional
        Player whose piece is in that point (default is None).
    locked: bool, optional
        True if point is in mill (default is False).
    """

    def __init__(self, coordinates: tuple, posbl_mov: list, owner: Player = None, locked: bool = False):
        """
        Parameters
        ----------
        coordinates: tuple
            Coordinates on the board.
        posbl_mov: list
            List of coordinates of connected points.
        owner: Player, optional
            Player whose piece is in that point (default is None).
        locked: bool, optional
            True if point is in mill (default is False).
        """
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
        """
        Unlock itself and points in common mill.
        """
        self.owner().find_mills()
        mills = self.owner().mills_list()
        for mill in mills:
            if self in mill:
                for point in mill:
                    point._locked = False

    def set_owner(self, player: Player = None):
        """
        Set new owner of point."""
        if not self._owner:
            self._owner = player
        else:
            raise PointOccupiedError()

    def remove_owner(self):
        """
        Remove current owner.

        Set owner to None, unlock point
        and remove it from players occupied list.
        """
        if self._owner:
            if self._locked:
                self.unlock()
            self._owner._occupied.remove(self)
            self._owner = None
        else:
            raise FreePointError()

    def is_blocked(self, board) -> bool:
        """
        Return true if all connected points are occupied.

        Parameters
        ----------
        board : Board
            Board of current game.
        """
        for point in self.posbl_mov():
            point = board.get_point(point)
            if not point.owner():
                return False
        return True
