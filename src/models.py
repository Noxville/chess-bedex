class GameState:
    def __init__(self, half_move_num, players_turn, prev_move_uci, board_fen):
        self.half_move_num = half_move_num
        self.players_turn = players_turn
        self.prev_move_uci = prev_move_uci
        self.board_fen = board_fen

    def to_dict(self):
        return {
            'msg_type': 'GAMESTATE',
            'current_move_number': 1 + self.half_move_num,
            'player_to_move': self.players_turn,
            'previous_move': self.prev_move_uci,
            'board_state': self.board_fen
        }

    def __repr__(self):
        return "[{} - {}] previous_move: {}, board: {}".format(1 + self.half_move_num, self.players_turn, self.prev_move_uci,
                                                               self.board_fen)


class ResultEvent:
    def __init__(self, outcome):
        self.outcome = outcome

    def __repr__(self):
        return "{}".format(self.outcome)

    def to_dict(self):
        return {
            'msg_type': 'GAME_END',
            'winner': {
                '1-0': 'WHITE',
                '0-1': 'BLACK',
                '1/2-1/2': 'DRAW'
            }[self.outcome]
        }
