from board import Board
from player import Player
from computer_player import ComputerPlayer
from point_generate import generate_points

class Game:

    def __init__(self, mode_number, ai=False, symbol=None):
        points_list = generate_points(mode_number)
        modes = {1: (False, Board(3, 3, points_list)),
                 2: (False, Board(6, 5, points_list)),
                 3: (True, Board(9, 7, points_list)),
                 4: (True, Board(12, 7, points_list))}
        self._fly = modes[mode_number][0]
        self._board = modes[mode_number][1]
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.computer_player = None
        self.human_player = None
        if ai:
            self.set_human_symbol(symbol)
        self._win = False
        self._phase = "Placing Pieces"
        phases = ["Placing Pieces", "Moving", "Flying"]

    def set_human_symbol(self, symbol):
        if symbol == "o" or symbol == "0":
            self.player2 = ComputerPlayer(2)
        else:
            self.player1 = ComputerPlayer(1)

    def board(self):
        return self._board

    def win(self):
        return self._win

    def phase(self):
        return self._phase

    def set_phase(self, new_phase):
        self._phase = new_phase

    def players(self):
        return [self.player1, self.player2]

    def check_if_phase_moving(self):
        pieces_num = self.board().pieces_num()
        placed1 = self.player1.placed_num()
        placed2 = self.player2.placed_num()
        if placed1 == pieces_num and placed2 == pieces_num:
            return True
        else:
            return False

    def check_if_phase_flying(self):
        for player in self.players():
            if len(player.occupied()) == 3:
                return True
        else:
            return False

    def check_mills(self, player):
        """
        input
        check
        remove
        print board"""
        player.find_mills()
        if player.is_mill():
            if self.board().pieces_num() == 3:
                return False
            if not self.opponent_removable(player):
                return False
            else:
                return True

    def opponent_removable(self, player):
        if player == self.player1:
            other_player = self.player2
        else:
            other_player = self.player1
        for piece in other_player.occupied():
            if not piece.locked():
                return True
            else:
                continue
        return False

    def check_phase(self):
        """check if phase is still valid
        if not  -> change phase if possible in mode
        phase 1: until both players placed pieces pieces_num times
        phase 2: until 1 of players has 3 pieces left
        phase 3 : until one of plyers has 2 pieces left"""
        if self._phase == "Placing Pieces":
            if self.check_if_phase_moving():
                self.set_phase("Moving")
        if self._phase == "Moving" and self._fly:
            if self.check_if_phase_flying():
                self.set_phase("Flying")

    def check_win(self):
        if self.board().pieces_num() == 3:
            for player in self.players():
                if player.is_mill():
                    self._win = True
        for player in self.players():
            if not self._phase == "Placing Pieces":
                if len(player.occupied()) == 2:
                    self._win = True
            if not player.possible_moves(self.board()) and player.placed_num():
                self._win = True

    def reveal_winner(self):
        if len(self.player2.occupied()) == len(self.player1.occupied()):
            if self.board().pieces_num() == 3:
                for player in self.players():
                    if player.is_mill():
                        return player
            return None
        elif len(self.player2.occupied()) > len(self.player1.occupied()):
            return self.player2
        else:
            return self.player1
