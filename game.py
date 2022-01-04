from classes import Player, Point, Board



class Game:

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
