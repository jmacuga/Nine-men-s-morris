from exceptions import PointOccupiedError, FreePointError
from player import Player


class Point:
    """ attributes:

        coordinates
        possible movement points
        owner: optional


        methods:
        symbol: "_"/"O","X"
        take by player
        remove

        """

    def __init__(self, coordinates: tuple, posbl_mov: list, owner: 'Player' = None, locked=False):
        self._coords = coordinates
        self._posbl_mov = posbl_mov
        self._owner = owner if owner else None
        self._locked = locked

    def coord(self):
        return self._coords

    def posbl_mov(self):
        return self._posbl_mov

    def symbol(self):
        if not self.owner():
            return "•"
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

    def set_owner(self, player: "Player" = None):
        if not self._owner:
            self._owner = player
        else:
            raise PointOccupiedError()

    def remove_owner(self):
        if self._owner:
            if self._locked:
                self.unlock()
            self._owner._occupied.remove(self)
            self._owner = None
        else:
            raise FreePointError("There is no piece to remove from this point")
