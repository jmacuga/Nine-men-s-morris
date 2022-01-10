from classes import ComputerPlayer, FreePointError, Player, Board, ImpossibleMove, CoordsOfNotActivePoint
from classes import PointOwnerError, PointInMillError, PointOccupiedError
import os
import copy
import math


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
        self.computer_player = None
        self.human_player = None
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
                print("Scond phase: moving")
        if self._phase == "moving" and self._fly:
            if self.check_if_phase_flying():
                self.set_phase("flying")
                print("Last phase: flying")

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

    def computer_move(self, player):
        print(self.board().print_board())
        if self._phase == "placing_pieces":
            player.best_place_piece(self.board())
        if self._phase == "moving":
            player.best_move(self.board())
        if self._phase == "flying":
            player.best_move(self.board(), fly=True)

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
        if self.human_player.is_mill():
            return -10
        if self.computer_player.is_mill():
            return +10
        if self.reveal_winner() == self.computer_player:
            return +20
        if self.reveal_winner() == self.human_player:
            return -20
        else:
            return 0

    def best_move(self):
        best_score = -1000
        if self._phase == "placing_pieces":
            posbl_points = [point for point in self.board().points_list()
                            if not point.owner()]
            for point in posbl_points:
                new_game = copy.deepcopy(self)
                new_point = new_game.board().get_point(point.coord())
                new_game.computer_player.place_piece(new_point)
                score = new_game.minimax(4, -1000, +1000, False)
                if score > best_score:
                    best_score = score
                    best_point = point
            self.computer_player.place_piece(best_point)
        if self._phase == "moving":
            for point1, point2 in self.computer_player.possible_moves(self.board()):
                new_game = copy.deepcopy(self)
                new_point1 = new_game.board().get_point(point1.coord())
                new_point2 = new_game.board().get_point(point2.coord())
                new_game.computer_player.move_piece(new_point1, new_point2)
                score = new_game.minimax(4, -1000, +1000, False)
                if score > best_score:
                    best_score = score
                    best_point1 = point1
                    best_point2 = point2
            self.computer_player.move_piece(best_point1, best_point2)
        if self._phase == "flying":
            for point1, point2 in self.computer_player.possible_fly_moves(self.board()):
                new_game = copy.deepcopy(self)
                new_point1 = new_game.board().get_point(point1.coord())
                new_point2 = new_game.board().get_point(point2.coord())
                new_game.computer_player.move_piece(new_point1, new_point2, fly=True)
                score = new_game.minimax(10, -2000, +2000, False)
                if score > best_score:
                    best_score = score
                    best_point1 = point1
                    best_point2 = point2
            self.computer_player.move_piece(best_point1, best_point2, fly=True)

    def minimax(self, depth, alpha, beta, maximizing):
        if maximizing:
            player = self.computer_player
        else:
            player = self.human_player
        player.find_mills()
        self.check_win()
        if self.win() or player.is_mill() or not depth:
            return self.score()
        if maximizing:
            if self._phase == "placing_pieces":
                return self.minimax_phase1(depth, alpha, beta, True)
            if self._phase == "moving":
                return self.minimax_phase2(depth, alpha, beta, True)
            if self._phase == "flying":
                return self.minimax_phase2(depth, alpha, beta, True, fly=True)
        else:
            if self._phase == "placing_pieces":
                return self.minimax_phase1(depth, alpha, beta, False)
            if self._phase == "moving":
                return self.minimax_phase2(depth, alpha, beta, False)
            if self._phase == "flying":
                return self.minimax_phase2(depth, alpha, beta, False, fly=True)


    def minimax_phase1(self, depth, alpha, beta, maximizing):
        if maximizing:
            best_score = -2000
            posbl_points = [point for point in self.board().points_list()
                                    if not point.owner()]
            for point in posbl_points:
                new_game = copy.deepcopy(self)
                new_point = new_game.board().get_point(point.coord())
                new_game.computer_player.place_piece(new_point)
                score = new_game.minimax(depth - 1, alpha, beta, False)
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = 2000
            posbl_points = [point for point in self.board().points_list()
                                if not point.owner()]
            for point in posbl_points:
                new_game = copy.deepcopy(self)
                new_point = new_game.board().get_point(point.coord())
                new_game.human_player.place_piece(new_point)
                score = new_game.minimax(depth - 1, alpha, beta, True)
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return best_score


    def minimax_phase2(self, depth, alpha, beta, maximizing, fly=False):
        if maximizing:
            best_score = -2000
            if fly:
                posbl_moves =  self.computer_player.possible_fly_moves(self.board())
            else:
                posbl_moves =  self.computer_player.possible_moves(self.board())
            for point1, point2 in posbl_moves:
                new_game = copy.deepcopy(self)
                new_point1 = new_game.board().get_point(point1.coord())
                new_point2 = new_game.board().get_point(point2.coord())
                new_game.computer_player.move_piece(new_point1, new_point2, fly)
                score = new_game.minimax(depth - 1, alpha, beta, False)
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = 2000
            if fly:
                posbl_moves =  self.human_player.possible_fly_moves(self.board())
            else:
                posbl_moves =  self.human_player.possible_moves(self.board())
            for point1, point2 in posbl_moves:
                new_game = copy.deepcopy(self)
                new_point1 = new_game.board().get_point(point1.coord())
                new_point2 = new_game.board().get_point(point2.coord())
                new_game.human_player.move_piece(new_point1, new_point2)
                score = new_game.minimax(depth - 1, alpha, beta, True)
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return best_score
