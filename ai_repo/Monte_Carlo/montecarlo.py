import random
import math
import time
import os
import copy

ROWS = 6
COLS = 7
SIMULATION = 1
STILL_PLAYING = 0
WON = 1
DRAW = 2
PLAYER = 0
AI = 1

EMPTY_BOARD = [' ' * 7 for i in range(6)]

ai_vs_ai = "Monte_Carlo\\ai_vs_ai.txt"
man_vs_ai = "Monte_Carlo\\man_vs_ai.txt"

def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

class ConnectFourPos:

    def __init__(self, pos:list):
        self.pos = pos
        self.player = 'X'
        self.cols_filled = [0] * 7
        self.over_state = STILL_PLAYING
        self.move_statistics = ''
    
    def copy(self):
        return copy.deepcopy(self)

    def dump_pos(self):
        DisplayPos(self.pos)

    def dump_pos_file(self, PLAYER):
        file_path = man_vs_ai
        with open(file_path, 'a') as file:
            if PLAYER == AI:
                file.write(f"\t      AI moved '{self.player}' to {self.move}\n")
                file.write(self.move_statistics)
            else:
                file.write(f"\t      Player moved '{self.player}' to {self.move}")
            FileDisplayBoard(file, self.pos)
        self.move_statistics=''
        
    def parse_move(self):
        self.move = GetMove(self.player, self.cols_filled)
    
    def make_move(self):
        self.pos = MakeMove(self.pos, self.move, self.player, self.cols_filled)

    def change_player(self):
        if self.player == 'X':
            self.player = 'O'
        else: self.player = 'X'

    def valid_moves(self):
        valid_moves = []
        for col in range(COLS):  # Assuming 7 columns in your game
            if self.cols_filled[col] < ROWS:  # Check if the column is not full
                valid_moves.append(str(col + 1))  # Append the column as a valid move
        return valid_moves

    def monte_carlo(self, player, N):
        self.move = pure_mc(self, player, N)

    def is_over(self, flag = 0):
        self.over_state = IsOver(self.pos, self.player) 
        if self.over_state == STILL_PLAYING: return False
        elif self.over_state == DRAW: 
            if not flag: prGreen(f"\t      Draw!") 
            return True
        else: 
            if not flag: prGreen(f"\t      {self.player} Won!")
            return True
        
def FileDisplayBoard(file, pos):
    file.write('\n   1   2   3   4   5   6   7\n')
    file.write("   ___________________________ \n")
    for row in pos:
        file.write("  | "+" | ".join(row)+" |\n")
        file.write("  |---------------------------|\n")


def IsOver(pos:list, player):
    for row in pos:
        if 4 * player in ''.join(row):
            return WON
    
    for col in range(COLS):
        col_str = ''.join(pos[row][col] for row in range(6))
        if 4 * player in col_str:
            return WON
    
    for i in range(3):
        for j in range(4):
            diagonal = ''.join(pos[i + k][j + k] for k in range(4))
            if 4 * player in diagonal:
                return WON
    
    for i in range(3):
        for j in range(4):
            diagonal = ''.join(pos[i + k][6 - j - k] for k in range(4))
            if 4 * player in diagonal:
                return WON
    
    # Check for a draw
    if all(pos[row][col] != ' ' for row in range(ROWS) for col in range(COLS)):
        return DRAW
    
    return STILL_PLAYING

def GetMove(player:str, cols_filled:list):
    while True:
        try:
            move = int(input(f"{player}'s move (1-7): "))
            if 1 <= move <= 7:
                if cols_filled[move - 1] < 6:
                    return str(move)
                else:
                    print(f"{move} is full")
                    continue
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Please enter a valid integer.")

def MakeMove(pos:list, move:str, player:str,cols_filled:list):
    col = int(move) - 1
    for y, row in enumerate(reversed(pos)):
        if row[col] == ' ':
            cols_filled[col] += 1
            row_list = list(row)
            row_list[col] = player
            pos[len(pos) - 1 - y] = "".join(row_list)
            return pos
    return pos
    
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

def DisplayPos(pos):
    def colorize(char):
        if char == 'X':
            return "\033[91mX\033[00m"  # Red 'X'
        elif char == 'O':
            return "\033[94mO\033[00m"  # Blue 'O'
        else:
            return char

    prGreen("   1   2   3   4   5   6   7")
    print("   ___________________________ ")
    for i, row in enumerate(pos):
        colored_row = [colorize(char) for char in row]
        print("  | "+" | ".join(colored_row)+" |")
        print("  |---------------------------|")


def pure_mc(pos, player, N):
    # all moves from starting position
    initial_moves = pos.valid_moves()
    # win counters per move
    win_counts = dict((move, 0) for move in initial_moves)

    for move in initial_moves:
        for i in range(N):
            sim_pos = pos.copy()
            # make random moves until the game is over
            sim_pos.over_state = Simulate(sim_pos, move)
            if sim_pos.over_state == WON and sim_pos.player == player:
                win_counts[move] += 1
            elif sim_pos.over_state == DRAW:
                win_counts[move] += 0.5
    
    best_move = max(win_counts, key=win_counts.get)

    pos.move_statistics = GetAIDataString(N, initial_moves, win_counts)
    print(f"\nBest move for {player}: {best_move}") 
    print(pos.move_statistics)
    return best_move

def GetAIDataString(N, valid_moves, win_counts):
    moves = GetPossibleMovesString(valid_moves)
    wins = GetWinPercentageString(win_counts, N)
    return moves +'\n'+ wins

def GetPossibleMovesString(valid_moves):
    formatted_moves = ", ".join(str(move) for move in valid_moves)
    # print(f"All possible moves: {formatted_moves}")
    return f"All possible moves: {formatted_moves}"

def GetWinPercentageString(win_counts, N):
    win_percentage_dict = dict()
    formatted_string = []
    for move, count in win_counts.items():
        win_percentage_dict[move] = f"{((count / N) * 100):.2f} % |"
        formatted_string.append(f"{move} -> {win_percentage_dict[move]}")
    formatted_string = ' '.join(formatted_string)
    # print(formatted_string)
    return formatted_string

def Simulate(pos:ConnectFourPos, move):
    playing = True
    pos.move = move
    pos.make_move()
    pos.change_player()
    while playing:
        sim_moves = pos.valid_moves()
        random_move = random.choice(sim_moves)
        pos.move = random_move
        pos.make_move()
        # pos.dump_pos()

        if pos.is_over(SIMULATION) == True:
            # pos.dump_pos()
            pos.change_player()
            playing = False

        # print(move,pos.cols_filled)
        pos.change_player()
        
    return pos.over_state

def play_game(pos: ConnectFourPos, player_side = "X"):
    playing = True
    pos.dump_pos()
    while playing:
        if pos.player == player_side:
            # pos.parse_move()
            pos.move = pure_mc(pos, 'X', 1000)
            pos.make_move()
            # pos.dump_pos_file(PLAYER)
        else:
            pos.parse_move()
            # pos.move = pure_mc(pos, 'O', 1000)
            pos.make_move()
            # pos.dump_pos_file(AI)

        # ClearScreen()
        pos.dump_pos()
        

        if pos.is_over() == True:
            pos.dump_pos()
            pos.change_player()
            playing = False
        pos.change_player()
        

Pos = ConnectFourPos(EMPTY_BOARD)
play_game(Pos)
