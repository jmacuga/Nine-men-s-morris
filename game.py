from classes import ComputerPlayer, FreePointError, Player, Board, ImpossibleMove, CoordsOfNotActivePoint
from classes import PointOwnerError, PointInMillError, PointOccupiedError
import os


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
            player.random_place_piece(self.board())
        if self._phase == "moving":
            player.random_move(self.board())
        if self._phase == "flying":
            player.random_fly(True, self.board())


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
