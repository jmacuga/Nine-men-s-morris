from classes import Mode, Player, Point, Board, ImpossibleMove, CoordsOfNotActivePoint
from classes import PointOwnerError, PointInMillError, PointOccupiedError
import os


class Game:
    clear = lambda: os.system('clear')
    clear()
    def __init__(self, mode_number):
        modes = {1: (Mode(), Board(3, 3)),
                 2: (Mode(True), Board(6, 5)),
                 3: (Mode(True, True), Board(9, 7)),
                 4: (Mode(True, True), Board(12, 7))}
        self._mode = modes[mode_number][0]
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

    def set_phase(self, new_phase):
        self._phase = new_phase

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

    def check_mills(self, player):

        """
        input
        check
        remove
        print board"""
        clear = lambda: os.system('clear')
        player.find_mills()
        if player.is_mill():
            clear()
            print(self.board().print_board())
            print("YOU HAVE A MILLL CONGRATTTS SISSS")
            removed = False
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






    def check_phase(self):
        """check if phase is still valid
        if not  -> change phase if possible in mode
        phase 1: until num of pieces == num of pl for mode
        phase 2: until 1 of players has 3 players left
        phase 3 : until one of plyers has 2 pieces left"""
        if self._phase == "placing_pieces":
            pieces_num = self.board().pieces_num()
            if len(self.player1.occupied()) == pieces_num and len(self.player2.occupied()) == pieces_num:
                self.set_phase("moving")
                print("Scond phase: moving")
        if self._phase == "moving" and self._mode.flying():
            if len(self.player1.occupied() == 3):
                self.set_phase("flying")
                print("Last phase: flying")

    def check_win():
        pass

    """ reveal winner
    """

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
                f'Player {player.id()} move\nEnter coordinates to pick a piece you want to move:')
            self.move_piece(player)
        if self._phase == "flying":
            print(
                f'Player {player.id()} move\nEnter coordinates to pick a piece you want to fly:')
            self.move_piece(player, fly=True)
        # if game.check_mills:
        #     print("Pick players piece to remove:")
        #     coords = coords_input()
        #     game.remove(player, coords)
        #     print(game.board().print_board())


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
            coords1 = self.coords_input()
            try:
                point1 = self.board().get_point(coords1)
            except CoordsOfNotActivePoint as e:
                print(e)
                continue
            print("Enter coordinates of destination point:")
            coords2 = self.coords_input()
            try:
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
        pointrow = input("row:")
        while not pointrow.isdigit():
            pointrow = input("row:")
        pointcol = input("col:")
        while not pointrow.isdigit():
            pointrow = input("row:")
        coords = (int(pointrow), int(pointcol))
        return coords
