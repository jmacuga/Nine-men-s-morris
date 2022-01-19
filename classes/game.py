from classes.board import Board
from classes.player import Player
from classes.computer_player import ComputerPlayer
from classes.point_generate import generate_points


class Game:
    """class representing state of game

    Attributes:
    ----------
    points_list
        list of active points passed to the board
    ai
        true if gameplay is in ai mode(default=False)
    sumbol
        symbol of human player on the board(default=None)
    win
        true if game is won
    phase
        current game phase [Placing pieces, Moving, Flying]

    Methods
    -------
    get_computer_player()
        generates computer player if game is in ai mode
    board()
    win()
    pahse()
    set_phase()
    players()
    check_if_phase_moving()
        returns true if hase is moving
    check_if_phase_flying()
        returns true if hase is flying
    check_mills(players)
        returns true if one of the players has a mill
        and is able to remove opponrnt's piece
    opponent_rmeovable(player)
        returns true if player is able ot remove opponent's piece
    check_phase()
        checks phase and sets game to next phase
    check_win()
        sets win to true if game if won
    reveal_winner()
        returns winner player, if there is a draw returns None
    """

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
        self._symbol = symbol
        if ai:
            self.get_computer_player()
        self._win = False
        self._phase = "Placing Pieces"
        phases = ["Placing Pieces", "Moving", "Flying"]

    def get_computer_player(self):
        if self._symbol == "o" or self._symbol == "0":
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
