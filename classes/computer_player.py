from classes.player import Player
from random import choice


class ComputerPlayer(Player):
    """
    Class representing computer player.

    Methods
    -------
    get_remove_point(board)
        Return random point to remove.
    score(game, human)
        Return score passed to minimax algorithm.
    best_move(game, board, human)
        Return best move based on minimax algorithm with alpha-beta pruning.
    minimax(game, human,  depth, alpha, beta, maximizing, fly=False)
        Pick minimax algorithm based on current game phase.
    minimax_phase1(self, game, human, depth, alpha, beta, maximizing)
        Search for best move during placing pieces game phase.
    minimax_phase2(self, game, human, depth, alpha, beta, maximizing, fly=False)
        Search for best move during moving and flying game phase.
    """
    def __init__(self, id):
        super().__init__(id)

    def get_remove_point(self, board):
        posbl_remove = [point for point in board.points_list()
                        if point.owner() and not point.owner() == self and not point.locked()]
        piece = choice(posbl_remove)
        return piece

    def score(self, game, human):
        if self.is_mill():
            return +10
        if human.is_mill():
            return -10
        if game.win():
            if game.reveal_winner() == self:
                return +10
            if game.reveal_winner() == human:
                return -10
            else:
                return 5
        else:
            return 0

    def best_move(self, game, board, human):
        best_score = -1000
        alpha = -1000
        beta = 1000
        depth = 4
        if game.phase() == "Placing Pieces":
            posbl_points = [point for point in board.points_list()
                            if not point.owner()]
            for point in posbl_points:
                self.place_piece(point)
                self.find_mills()
                game.check_phase()
                score = self.minimax_phase1(game, human, depth, alpha, beta, False)
                point.remove_owner()
                self._placed_num -= 1
                self.find_mills()
                game.set_phase("Placing Pieces")
                game._win = False
                alpha = max(score, alpha)
                if score > best_score:
                    best_score = score
                    best_point = point
            self.place_piece(best_point)
        else:
            fly = True if game._phase == "Flying" else False
            for point1, point2 in self.possible_moves(game.board()):
                self.move_piece(point1, point2, fly)
                self.find_mills()
                score = self.minimax_phase2(
                    game, human, depth, alpha, beta, True, fly)
                self.move_piece(point2, point1, fly)
                self.find_mills()
                self._placed_num -= 2
                game._win = False
                alpha = max(score, alpha)
                if score > best_score:
                    best_score = score
                    best_point1 = point1
                    best_point2 = point2
            self.move_piece(best_point1, best_point2)

    def minimax(self, game, human,  depth, alpha, beta, maximizing, fly=False):
        if game._phase == "Placing Pieces":
            return self.minimax_phase1(game, human, depth, alpha, beta, maximizing)
        else:
            return self.minimax_phase2(game, human, depth, alpha, beta, maximizing, fly)

    def minimax_phase1(self, game, human, depth, alpha, beta, maximizing):
        game.check_win()
        if game.win() or human.is_mill() or self.is_mill() or not depth:
            return self.score(game, human)
        if maximizing:
            player = self
        else:
            player = human
        posbl_points = [point for point in game.board().points_list()
                        if not point.owner()]
        for point in posbl_points:
            player.place_piece(point)
            player.find_mills()
            game.check_phase()
            score = self.minimax(game, human, depth - 1,
                                 alpha, beta, not maximizing)
            player._placed_num -= 1
            point.remove_owner()
            player.find_mills()
            game.set_phase("Placing Pieces")
            game._win = False
            if maximizing:
                alpha = max(alpha, score)
            else:
                beta = min(beta, score)
            if beta <= alpha:
                break
        return alpha if maximizing else beta

    def minimax_phase2(self, game, human, depth, alpha, beta, maximizing, fly=False):
        game.check_win()
        if game.win() or human.is_mill() or self.is_mill() or not depth:
            return self.score(game, human)
        if maximizing:
            player = self
        else:
            player = human
        if fly:
            posbl_moves = player.possible_fly_moves(game.board())
        else:
            posbl_moves = player.possible_moves(game.board())
        for point1, point2 in posbl_moves:
            player.move_piece(point1, point2, fly)
            player.find_mills()
            score = self.minimax(game, human, depth - 1,
                                 alpha, beta, not maximizing)
            player.move_piece(point2, point1, fly)
            player.find_mills()
            player._placed_num -= 2
            game._win = False
            if maximizing:
                alpha = max(alpha, score)
            else:
                beta = min(beta, score)
            if beta <= alpha:
                break
        return alpha if maximizing else beta