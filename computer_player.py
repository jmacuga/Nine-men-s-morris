from player import Player
from random import choice

class ComputerPlayer(Player):
    def __init__(self, id):
        super().__init__(id)

    def random_place_piece(self, board):
        posbl_points = [point for point in board.points_list()
                        if not point.owner()]
        point = choice(posbl_points)
        self.place_piece(point)

    def random_move(self, board, fly=False):
        if fly:
            point1, point2 = choice(self.possible_fly_moves(board))
            self.move_piece(point1, point2, True)
        else:
            point1, point2 = choice(self.possible_moves(board))
            self.move_piece(point1, point2)

    def random_remove(self, board):
        posbl_remove = [point for point in board.points_list()
                        if point.owner() and not point.owner() == self and not point.locked()]
        point = choice(posbl_remove)
        self.remove_opponents_piece(point)