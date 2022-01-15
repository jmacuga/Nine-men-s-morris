class IncorrectCoordsError(Exception):
    pass



class CoordsOfNotActivePoint(Exception):
    pass


class PointOccupiedError(Exception):
    def __init__(self):
        super().__init__('This point is already occupied. Pick another one.')


class ImpossibleMove(Exception):
    pass


class FreePointError(Exception):
    pass


class PointOwnerError(Exception):
    pass


class PointInMillError(Exception):
    pass
