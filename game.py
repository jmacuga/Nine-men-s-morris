from classes import Mode, Player, Point, Board, ImpossibleMove, CoordsOfNotActivePoint, PointOccupiedError



class Game:
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

    def board(self):
        return self._board

    def win(self):
        return self._win

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
        """check if phase is still valid
        if not  -> change phase if possible in mode
        phase 1: until num of pieces == num of pl for mode
        phase 2: until 1 of players has 3 players left
        phase 3 : until one of plyers has 2 pieces left"""
        pass

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
        if self._phase == "placing_pieces":
            print(
                f'Player {player.id()} move\nEnter coordinates to place a piece:')
            self.place_piece(player)
        if self._phase == "moving":
            print(
                f'Player {player.id()} move\nEnter coordinates to pick a piece you want to move:')
            coords1 = self.coords_input()
            point1 = self.board().get_point(coords1)
            print("Enter coordinates of destination point:")
            coords2 = self.coords_input()
            point2 = self.board().get_point(coords2)
            player.move_piece(point1, point2)
        if self._phase == "flying":
            print(
                f'Player {player.id()} move\nEnter coordinates to pick a piece you want to fly:')
            coords1 = self.coords_input()
            point1 = self.board().get_point(coords1)
            print("Enter coordinates of destination point:")
            coords2 = self.coords_input()
            point2 = self.board().get_point(coords2)
            player.move_piece(point1, point2, True)
        # if game.check_mills:
        #     print("Pick players piece to remove:")
        #     coords = coords_input()
        #     game.remove(player, coords)
        #     print(game.board().print_board())
        # if game.check_next_phase():
        #     print('Next phase')
        print(self.board().print_board())

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



    def coords_input(self):
        pointrow = input("row:")
        while not pointrow.isdigit():
            pointrow = input("row:")
        pointcol = input("col:")
        while not pointrow.isdigit():
            pointrow = input("row:")
        coords = (int(pointrow), int(pointcol))
        return coords
