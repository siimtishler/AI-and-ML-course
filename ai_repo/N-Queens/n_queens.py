import random
import time
import math

# For a NxN chessboard, the number of queens is always N

class NQPosition:

    def __init__(self, N):
        self.N = N
        self.board = FillBoard(N)
        self.board, self.vector = AddQueens(self.board)
    
    def value(self):
        value = CalculateConflicts(self.vector, self.N)
        return value

    def make_move(self, move):
        ColSwap(self.vector, move)
        
    def best_move(self):
        test_vector = self.vector[:]
        move = RandomCols(self.N)
        test_vector = ColSwap(test_vector, move)
        value_after = CalculateConflicts(test_vector, self.N)

        return move, value_after
    
    def print_board(self):
        PrintBoard(self.board)

def FillBoard(N):
    board=[]
    for i in range(N):
        row = []
        for j in range(N):
            row.append(' ')
        board.append(row)
    return board

def PrintBoard(board):
    print('\nBOARD:')
    for i in range(N):
        print(board[i])
    print('')

def AddQueens(board):
    vec = []
    random_integers = random.sample(range(N), N)
    for i in range(N):
        random_int = random_integers[i]
        board[random_integers[i]][i] = 'Q'
        # Add to vector
        vec.append(random_int)             
    return board, vec

def CalculateConflicts(vector:list, N):
    conflict_count = 0
    for i in range(N):
        for j in range(i + 1, N):
            # Check if queens share the same diagonal or row
            if abs(vector[i] - vector[j]) == abs(i - j):
                conflict_count += 1
    return conflict_count

def ColSwap(vector:list, move:tuple):
    temp = vector[move[0]]
    vector[move[0]] = vector[move[1]]
    vector[move[1]] = temp
    return vector

def RandomCols(N): 
    return tuple(random.sample(range(N), 2))
    
def VectorToBoard(vector:list, N):
    chessboard = [[' ' for _ in range(N)] for _ in range(N)]

    for row, col in enumerate(vector):
        chessboard[col][row] = 'Q'

    return chessboard


def hill_climbing(pos):
    curr_value = pos.value()
    if curr_value == 0:
        print("early return", pos.vector)
        return pos, curr_value
    while True:
        move, new_value = pos.best_move()
        if new_value >= curr_value:
            # no improvement, give up
            return pos, curr_value
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)


# Main algo

N = 8
RESTART_VALUE = N * N
I = 3

time_spent_sum = 0

for i in range(I):
    pos = NQPosition(N)
    print(f"{i}) Initial pos conflicts:", pos.value())
    # pos.print_board()
    # print(f"VECTOR before: {pos.vector}")

    time_start = time.time()
    iterations = 0
    while True:
        _, best_value = hill_climbing(pos)
        iterations += 1
        if best_value == 0: 
            break
        if iterations % RESTART_VALUE == 1:
            print("Restart\n")
            pos = NQPosition(N)

    time_spent = time.time() - time_start
    time_spent_sum += time_spent
    print(f"Found in {iterations} iterations, {time_spent:.2f} seconds\n")

    pos.board = VectorToBoard(pos.vector, pos.N)
    # pos.print_board()
    # print(f"VECTOR after: {pos.vector}")
print(f"\nN: {N}\nAvg time:{time_spent_sum/I:.2f}s\nRestart val: {RESTART_VALUE}")



# It's cheaper to jump into a hole, than jump out of it [Video: Advenced local search timestamp: 11:11]
# Damn... Did not expect that get hit with some hard life advice