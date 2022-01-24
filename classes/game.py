from classes.board import Board
from classes.player import Player
from classes.computer_player import ComputerPlayer
from classes.point_generate import generate_points


class Game:
    """
    Class representing state of the game.

    Attributes:
    ----------
    points_list : list
        List of active points passed to the board.
    sumbol : str
        Symbol of human player on the board (default is None).
    fly : bool
        True if current game mode fly phase is permited.
    board : Board
        Board of current game.
    player1 : Player
        Player with symbol 'o'.
    player2 : Player
        Player with symbol 'x'.
    win : bool
        True if game is won.
    phase : str
        Current game phase [Placing pieces, Moving, Flying].
    """

    def __init__(self, mode_number, ai=False, symbol=None):
        """
        Parameters
        ----------
        mode_number : int
            Game mode depending on board size.
        ai : bool, optional
            True if gameplay is in ai mode (default is False).
        sumbol : str, optional
            Symbol of human player on the board (default is None).
        """
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
        """Check if current phase is moving."""
        pieces_num = self.board().pieces_num()
        placed1 = self.player1.placed_num()
        placed2 = self.player2.placed_num()
        if placed1 == pieces_num and placed2 == pieces_num:
            return True
        else:
            return False

    def check_if_phase_flying(self):
        """Check if current phase is moving."""
        for player in self.players():
            if len(player.occupied()) == 3:
                return True
        else:
            return False

    def check_mills(self, player):
        """
        Check if player can remove opponents piece as a result of creating mill.

        Parameters
        ----------
        player : Player
            Player whose pieces are being checked.
        """
        player.find_mills()
        if player.is_mill():
            if self.board().pieces_num() == 3:
                return False
            if not self.opponent_removable(player):
                return False
            else:
                return True

    def opponent_removable(self, player):
        """
        Check if the player can remove any of opponent's pieces.

        Parameters
        ----------
            player : Player
        Player whose opponent's pieces are being checked.
        """
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
        """Check if phase has changed and set a new one."""
        if self._phase == "Placing Pieces":
            if self.check_if_phase_moving():
                self.set_phase("Moving")
        if self._phase == "Moving" and self._fly:
            if self.check_if_phase_flying():
                self.set_phase("Flying")

    def check_win(self):
        """
        Check if game is won.

        Set self._win to True if one of the players has 2 pieces left.
        In mode 1 if one of the payers made a mill. In mode 4 if board
        is full. In phase moving game is won if one of the players
        doesn't have possible moves.
        """
        if self.board().pieces_num() == 3:
            for player in self.players():
                if player.is_mill():
                    self._win = True
        if self.board().pieces_num() == 12:
            full = True
            for point in self.board().points_list():
                if not point.owner():
                    full = False
                    break
            if full:
                self._win == True
        for player in self.players():
            if not self._phase == "Placing Pieces":
                if len(player.occupied()) == 2:
                    self._win = True
                if not player.possible_moves(self.board()):
                    self._win = True

    def reveal_winner(self):
        """
        Return player who won.

        If game ended as a result of blocking one of the players,
        the player who has more pieces on the board is the winner.
        If there is a draw return None.
        """
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
