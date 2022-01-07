from classes import Mode, Player, Point, Board


class Game:
    def __init__(self, mode_number):
        modes = {1: (Mode(), Board(3, 3)),
                 2: (Mode(True), Board(6, 5)),
                 3: (Mode(True, True), Board(9, 7)),
                 4: (Mode(True, True), Board(12, 7))}
        self._mode = modes[mode_number][0]
        self._board = modes[mode_number][1]

    def board(self):
        return self._board

    def check_if_phase_moving(player1, player2, game_mode):
        if len(player1.occupied()) == game_mode and len(player2.occupied()) == game_mode:
            return True
        else:
            return False

    def check_if_win(self):
        pass

    def check_if_phase_flying(player1, player2, game_mode):
        if len(player2.occupied()) == 3 or len(player1.occupied()) == 3:
            return True
        else:
            return False

    def pick_board():
        """generate mode object from given"""

    def pick_player():
        """generate_player"""
        pass

    # phase:
    def make_move(player, phase):
        """enter coords
        check cords
        move - for phase
        print board
        check mills -- > remove
        check phase
        check win
        """
        pass

    def check_mills():
        pass

    def remove_opponent():
        """
        input
        check
        remove
        print board"""
        pass

    def check_phase():
        pass

    def check_win():
        pass

    """ reveal winner
    """
