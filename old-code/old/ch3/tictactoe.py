
x = "X"
o = "O"

# opponent win -> I lose
#


win = 1
draw = 2
lose = 3


class Board():
    empty = [[None for i in range(0,3)] for j in range(0,3)]

    def __init__(self, board=empty):
        self.board = board

    def __str__(self):
        def symbols(row): return [sym if sym else " " for sym in row]
        row_strings = [" | ".join(symbols(row)) for row in self.board]
        return "\n--+---+--\n".join(row_strings)

    def __repr__(self):
        return self.__str__()

    def move(self, symbol, position):
        new_i, new_j = position
        if self.board[new_i][new_j]:
            raise ValueError("Position (%d,%d) is already filled" % position)
        copy = [[cell for cell in row] for row in self.board]
        copy[new_i][new_j] = symbol
        return Board(copy)

    def winner(self):
        lines = [[(i,j) for j in range(0,3)] for i in range(0,3)] +\
                    [[(j,i) for j in range(0,3)] for i in range(0,3)] +\
                    [[(i,i) for i in range(0,3)]] +\
                    [[(i,2-i) for i in range(0,3)]]
        line_symbols = [{self.board[i][j] for i,j in line} for line in lines]
        if {x} in line_symbols:
            return x
        elif {o} in line_symbols:
            return o

    def outcome(self, symbol):
        if self.winner() == symbol:
            return win
        elif not self.winner():
            if self.open_positions():
                return None
            else:
                return draw
        else:
            return lose
            
    def open_positions(self):
        return [(i,j) for i in range(0,3) for j in range(0,3)
                    if not self.board[i][j]]

def opponent(symbol):
    return x if symbol == o else o

def opposite_outcome(outcome):
    return 4 - outcome

def worst_case(board, symbol, position):
    test = board.move(symbol, position)
    outcome = test.outcome(symbol)
    if outcome is None:
        opponent_move, opponent_outcome = next_move(test,opponent(symbol))
        return opposite_outcome(opponent_outcome)
    else:
        return outcome

def ranked_moves(board, symbol):
    options = [(p, worst_case(board,symbol,p)) for p in board.open_positions()]
    x = sorted(options, key=lambda x: x[1])
    return  x

def next_move(board,symbol):
    moves = ranked_moves(board, symbol)
    return (moves[0] if moves else (None, board.outcome(symbol)))


import unittest

class Test(unittest.TestCase):

    def test_tie(self):
        tie_board = Board([[x,o,x],[o,o,x],[x,x,o]])
        self.assertTrue(tie_board.winner() is None)
        self.assertEqual(tie_board.outcome(x), draw)
        self.assertEqual(tie_board.outcome(o), draw)
        pos, outcome = next_move(tie_board,x)
        self.assertTrue(pos is None)
        self.assertEqual(outcome, draw)

    def test_win_if_possible(self):
        winnable_both = Board([[x,None,None],[None,x,None],[o,o,None]])
        x_move, x_outcome = next_move(winnable_both, x)
        self.assertEqual(x_move, (2,2))
        self.assertEqual(x_outcome, win)
        o_move, o_outcome = next_move(winnable_both, o)
        self.assertEqual(o_move, (2,2))
        self.assertEqual(o_outcome, win)

    def test_worst_case_if_win(self):
        winnable_both = Board([[x,None,None],[None,x,None],[o,o,None]])
        worst_case_x = worst_case(winnable_both,x,(2,2))
        self.assertEqual(worst_case_x, win)
        # o_move, o_outcome = next_move(winnable_both, o)
        # self.assertEqual(o_move, (2,2))
        # self.assertEqual(o_outcome, win)

    def test_worst_case_fail_to_block(self):
        b = Board([[x,None,None],[None,x,None],[o,None,None]])
        worst_case_o = worst_case(b,o,(2,1))
        self.assertEqual(worst_case_o, lose)
        # o_move, o_outcome = next_move(winnable_both, o)
        # self.assertEqual(o_move, (2,2))
        # self.assertEqual(o_outcome, win)

    #
    # def test_bad_move_leads_to_expected_loss(self):
    #     winnable_both = Board([[x,None,None],[None,x,None],[o,o,None]])
    #     self.assertEqual(worst_case(winnable_both, x, (0,1)), lose)

    def test_worst_case_lose(self):
        winnable_both = Board([[x,None,None],[None,x,None],[o,o,None]])
        wc_x = worst_case(winnable_both, x, (0,2))
        self.assertEqual(wc_x, lose)
        wc_o = worst_case(winnable_both, o, (0,2))
        self.assertEqual(wc_o, lose)
    #
    # def test_moves(self):
    #     winnable_both = Board([[x,None,None],[None,x,None],[o,o,None]])
    #     ranked_moves(winnable_both, x)

    def test_worst_case_win(self):
        winnable_both = Board([[x,None,None],[None,x,None],[o,o,None]])
        wc_x = worst_case(winnable_both, x, (2,2))
        self.assertEqual(wc_x, win)
        wc_o = worst_case(winnable_both, o, (2,2))
        self.assertEqual(wc_o, win)

    def test_can_win(self):
        winnable_both = Board([[x,None,None],[None,x,None],[o,o,None]])
        x_move, x_outcome = next_move(winnable_both, x)
        self.assertEqual(x_move, (2,2))
        self.assertEqual(x_outcome, win)
        o_move, o_outcome = next_move(winnable_both, o)
        self.assertEqual(o_move, (2,2))
        self.assertEqual(o_outcome, win)

    def test_first_move(self):
        move, outcome = next_move(Board(),x)
        self.assertEqual(move,(0,0))
        self.assertEqual(outcome, 2)

    def test_counter_first_move(self):
        move, outcome = next_move(Board().move(x, (0,0)),o)
        self.assertEqual(move,(1,1))
        self.assertEqual(outcome, 2)

    def test_bad_counter_first_move(self):
        move, outcome = next_move(Board().move(x, (0,0)),o)
        self.assertEqual(move,(1,1))
        self.assertEqual(outcome, 2)

    def test_o_messes_up(self):
        b = Board.move(x, (0,0)).move(o,(2,0))
        move,outcome = next_move(b, x)
        self.assertEqual(move, (2,2))
        self.assertEqual(outcome, 1)

if __name__ == '__main__':
    unittest.main()







Board([[x,x,x],[x,None,o],[x,x,x]]).move(o,(1,1))

print(Board([[x,x,x],[x,None,o],[x,x,x]]))
