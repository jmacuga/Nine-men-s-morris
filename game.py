import os
from board import Board
from player import Player
from computer_player import ComputerPlayer
from exceptions import ComputerPlayer, FreePointError, ImpossibleMove
from exceptions import CoordsOfNotActivePoint, PointOwnerError, PointInMillError, PointOccupiedError


class Game:
    def clear(): return os.system('clear')
    clear()

    def __init__(self, mode_number):
        modes = {1: (False, Board(3, 3)),
                 2: (False, Board(6, 5)),
                 3: (True, Board(9, 7)),
                 4: (True, Board(12, 7))}
        self._fly = modes[mode_number][0]
        self._board = modes[mode_number][1]
        self.player1 = Player(1)
        self.player2 = Player(2)

        self._win = False
        self._phase = "placing_pieces"
        phases = ["placing_pieces", "moving", "flying"]

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
        def clear(): return os.system('clear')
        player.find_mills()
        if player.is_mill():
            clear()
            print(self.board().print_board())
            if self.board().pieces_num() == 3:
                return
            print("YOU HAVE A MILLL CONGRATTTS SISSS")
            removed = False
            if not self.opponent_removable(player):
                print("But you cannot remove any of opponnets pieces :((")
                input("Press Enter to continue")
            else:
                print("pick oponnents piece to remove:")
                while not removed:
                    try:
                        coords = self.coords_input()
                        point = self.board().get_point(coords)
                    except CoordsOfNotActivePoint as e:
                        print(e)
                        continue
                    try:
                        player.remove_opponents_piece(point)
                        removed = True
                    except PointOwnerError as e:
                        print(e)
                        continue
                    except PointInMillError as e:
                        print(e)
                        continue
                    except FreePointError as e:
                        print(e)
                        continue

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
        if self._phase == "placing_pieces":
            if self.check_if_phase_moving():
                self.set_phase("moving")
                # print("Scond phase: moving")
        if self._phase == "moving" and self._fly:
            if self.check_if_phase_flying():
                self.set_phase("flying")
                # print("Last phase: flying")s

    def check_win(self):
        if self.board().pieces_num() == 3:
            for player in self.players():
                if player.is_mill():
                    self._win = True
        for player in self.players():
            if not self._phase == "placing_pieces":
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

    def make_move(self, player):
        """eneter coords
        check coords
        make move
            move - depending on phase
            if phase 1:
                place piece
            if phase 2:
                move piece
            if phase 3:
                fly piece
        print boards
        if mill remov piece and print board

        """
        print(self.board().print_board())
        if self._phase == "placing_pieces":
            print(
                f'Player {player.id()} move\nEnter coordinates to place a piece:')
            self.place_piece(player)
        if self._phase == "moving":
            print(
                f'Player {player.id()} move\n')
            self.move_piece(player)
        if self._phase == "flying":
            print(
                f'Player {player.id()} move\n')
            self.move_piece(player, fly=True)

    def place_piece(self, player):
        coords = self.coords_input()
        try:
            point = self.board().get_point(coords)
            player.place_piece(point)
        except CoordsOfNotActivePoint as e:
            print(e)
            self.place_piece(player)
        except PointOccupiedError as e:
            print(e)
            self.place_piece(player)

    def move_piece(self, player, fly=False):
        moved = False
        while not moved:
            try:
                if fly:
                    print('Enter coordinates to pick a piece you want to fly:')
                else:
                    print('Enter coordinates to pick a piece you want to move:')
                coords1 = self.coords_input()
                point1 = self.board().get_point(coords1)
            except CoordsOfNotActivePoint as e:
                print(e)
                continue
            try:
                print("Enter coordinates of destination point:")
                coords2 = self.coords_input()
                point2 = self.board().get_point(coords2)
                player.move_piece(point1, point2, fly)
                moved = True
            except ImpossibleMove as e:
                print(e)
                continue
            except PointOccupiedError as e:
                print(e)
                continue
            except CoordsOfNotActivePoint as e:
                print(e)
                continue

    def coords_input(self):
        try:
            pointrow = input("row:")
            while not pointrow.isdigit():
                pointrow = input("row:")
            pointcol = input("col:")
            while not pointrow.isdigit():
                pointrow = input("row:")
            coords = (int(pointrow), int(pointcol))
        except ValueError:
            print("Try again")
            coords = self.coords_input()
        return coords


class ComputerGame(Game):
    def __init__(self, mode_number, human_symbol):
        super().__init__(mode_number)
        self.computer_player = None
        if human_symbol == "o":
            self.player2 = ComputerPlayer(2)
            self.computer_player = self.player2
            self.human_player = self.player1
        else:
            self.player1 = ComputerPlayer(1)
            self.computer_player = self.player1
            self.human_player = self.player2

    def check_computer_mills(self, player):
        def clear(): return os.system('clear')
        player.find_mills()
        if player.is_mill():
            clear()
            print(self.board().print_board())
            if self.board().pieces_num() == 3:
                return
            if not self.opponent_removable(player):
                return
            else:
                player.random_remove(self.board())

    def score(self):
        if self.computer_player.is_mill():
            return +10
        if self.human_player.is_mill():
            return -10
        if self.reveal_winner() == self.computer_player:
            return +10
        if self.reveal_winner() == self.human_player:
            return -10
        else:
            return 0

    def best_move(self):
        best_score = -2000
        alpha = -1000
        beta = 1000
        player = self.computer_player
        if self._phase == "placing_pieces":
            posbl_points = [point for point in self.board().points_list()
                            if not point.owner()]
            for point in posbl_points:
                player.place_piece(point)
                player.find_mills()
                self.check_phase()
                score = self.minimax_phase1(5, alpha, beta, False)
                point.remove_owner()
                player._placed_num -= 1
                player.find_mills()
                self.set_phase("placing_pieces")
                self._win = False
                alpha = max(score, alpha)
                if score > best_score:
                    best_score = score
                    best_point = point
            player.place_piece(best_point)
        else:
            fly = True if self._phase == "flying" else False
            for point1, point2 in player.possible_moves(self.board()):
                player.move_piece(point1, point2, fly)
                player.find_mills()
                score = self.minimax_phase2(4, alpha, beta, True, fly)
                player.move_piece(point2, point1, fly)
                player.find_mills()
                player._placed_num -= 2
                self._win = False
                alpha = max(score, alpha)
                if score > best_score:
                    best_score = score
                    best_point1 = point1
                    best_point2 = point2
            self.computer_player.move_piece(best_point1, best_point2)

    def minimax(self, depth, alpha, beta, maximizing, fly=False):
        if self._phase == "placing_pieces":
            return self.minimax_phase1(depth, alpha, beta, maximizing)
        else:
            return self.minimax_phase2(depth, alpha, beta, maximizing, fly)

    def minimax_phase1(self, depth, alpha, beta, maximizing):
        self.check_win()
        if self.win() or self.human_player.is_mill() or self.computer_player.is_mill() or not depth:
            return self.score()
        if maximizing:
            best_score = -2000
            player = self.computer_player
        else:
            best_score = 2000
            player = self.human_player

        posbl_points = [point for point in self.board().points_list()
                        if not point.owner()]
        for point in posbl_points:
            player.place_piece(point)
            player.find_mills()
            self.check_phase()
            score = self.minimax(depth - 1, alpha, beta, not maximizing)
            player._placed_num -= 1
            point.remove_owner()
            player.find_mills()
            self.set_phase("placing_pieces")
            self._win = False
            if maximizing:
                best_score = max(score, best_score)
                alpha = max(alpha, score)
            else:
                best_score = min(score, best_score)
                beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

    def minimax_phase2(self, depth, alpha, beta, maximizing, fly=False):
        self.check_win()
        if self.win() or self.human_player.is_mill() or self.computer_player.is_mill() or not depth:
            return self.score()
        if maximizing:
            best_score = -2000
            player = self.computer_player
        else:
            best_score = 2000
            player = self.human_player
        if fly:
            posbl_moves = player.possible_fly_moves(self.board())
        else:
            posbl_moves = player.possible_moves(self.board())
        for point1, point2 in posbl_moves:
            player.move_piece(point1, point2, fly)
            player.find_mills()
            score = self.minimax(depth - 1, alpha, beta, not maximizing)
            player.move_piece(point2, point1, fly)
            player.find_mills()
            player._placed_num -= 2
            self._win = False
            if maximizing:
                best_score = max(score, best_score)
                alpha = max(alpha, score)
            else:
                best_score = min(score, best_score)
                beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score
