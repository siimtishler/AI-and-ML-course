import queue
import time

CAVE_FILE_NAME = "cave300x300" # Change CAVE_FILE_NAME to load ASCII map into map_data
# CAVE_FILE_NAME = "cave600x600"
# CAVE_FILE_NAME = "cave900x900"

with open(f"ai_repo\Pathfinding\{CAVE_FILE_NAME}") as f:
    map_data = [l.strip() for l in f.readlines() if len(l)>1]

START_CHAR = 's'
GOAL_CHAR = 'D'

lava_map1 = [
    "      **    *******    **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "** *********        ***********",
    "******************       ***** ",
    "                      *****    ",
    "** *********        ***********",
    "**                       ***** ",
    "***************       *****    ",
    "** *********        ***********",
    "** *********        ***********",
    "**                       ***** ",
    "***************       *****    ",
    "**                       ***** ",
    "                               ",
    "                s              ",
]

lava_map2 = [
    "      **                       ",
    "     ***              ***  D   ",
    "     ***                ***** *",
    "                         **** *",
    "                s              ",
]

test_map2 = [
    "              D",
    "               ",
    "               ",
    "               ",
    "               ",
    "*              ",
    "               ",
    "               ",
    "               ",
    "s              ",
]

test_map = [
    "   s",
    "    ",
    " *  ",
    " D  ",
]

# FUNCTION DEFINES

def printMaze(maze):
    print("\nMaze:")
    for i in range(len(maze)):
        print("|"+maze[i]+"|")

def getCharOnMaze(maze, char):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (maze[i][j] == char):
                startCoord = (i,j)
                #print(f"'{char}' on maze at: {startCoord}")
                return startCoord
    print("Starting character not found!")
    return 0

def validMove(maze, y, x):
    x_bounds = len(maze[0])
    y_bounds = len(maze)
    if 0 <= x < x_bounds and 0 <= y < y_bounds and maze[y][x] != '*':
        return True
    else:
        return False
    
def printSolution(start_coor, end_coor, came_from:dict, maze, algo:str):
    path = []
    path_cost = 0
    current = end_coor
    while current != start_coor:
        path_cost += 1
        path.append(current)
        current = came_from[current]
    print(f"Path cost {algo}: {path_cost}")
    path.append(start_coor)
    path.reverse() # optional

    # Print the path
    for y, x in path:
        if (y,x) == end_coor or (y, x) == start_coor:
            continue
        maze[y] = maze[y][:x] + '.' + maze[y][x+1:]

    with open(f"ai_repo\Pathfinding\{algo}_solution_{CAVE_FILE_NAME}.txt", "w") as f:
        for row in maze:
            # print("|"+str(row)+"|")
            f.write("|"+row+"|"+'\n')

def heuristic(a:tuple, b:tuple):
   # Manhattan distance on a square grid
   return abs(a[0] - b[0]) + abs(a[1] - b[1])

def bfs(maze_data):
    maze = maze_data

    start_coor = getCharOnMaze(maze,START_CHAR) # row, col
    end_coor = getCharOnMaze(maze, GOAL_CHAR) # row, col

    frontier = queue.Queue() 
    frontier.put((start_coor))
    came_from = dict()
    came_from[start_coor] = None

    time_start = time.time() # Search time start
    iterations = 0
    while(not frontier.empty()):
        iterations += 1
        current = frontier.get() 
        if current == end_coor:
            break
        y, x = current

        for move_y, move_x in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_x = x + move_x
            next_y = y + move_y
            if validMove(maze, next_y, next_x) and (next_y, next_x) not in came_from:
                frontier.put((next_y, next_x)) 
                came_from[(next_y, next_x)] = current

    time_stop = time.time() # Search time end
    printSolution(start_coor, end_coor, came_from, maze, "bfs")
    print(f"Time spent BFS: {1000*(time_stop - time_start):.3f} ms, Iterations:{iterations}\n")


def greedy(maze_data):
    maze = maze_data

    start_coor = getCharOnMaze(maze,START_CHAR) # row, col
    end_coor = getCharOnMaze(maze, GOAL_CHAR) # row, col

    frontier = queue.PriorityQueue() # PRIO PriorityQueue()
    frontier.put((start_coor, 0))
    came_from = dict()
    came_from[start_coor] = None

    time_start = time.time() # Search time start
    iterations = 0
    while(not frontier.empty()):
        iterations += 1
        current = frontier.get()[0] # PRIO [1]
        if current == end_coor:
            break
        y, x = current

        for move_y, move_x in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_x = x + move_x
            next_y = y + move_y
            if validMove(maze, next_y, next_x) and (next_y, next_x) not in came_from:
                priority = heuristic(end_coor, (next_y, next_x))
                frontier.put(((next_y, next_x),priority)) # PRIO ((priority,(next_y, next_x)))
                came_from[(next_y, next_x)] = current

    time_stop = time.time() # Search time end
    printSolution(start_coor, end_coor, came_from, maze, "greedy")
    print(f"Time spent Greedy: {1000*(time_stop - time_start):.3f} ms, Iterations:{iterations}\n")

def astar(maze_data):
    maze = maze_data

    start_coor = getCharOnMaze(maze,START_CHAR) # row, col
    end_coor = getCharOnMaze(maze, GOAL_CHAR) # row, col

    frontier = queue.PriorityQueue() # PRIO PriorityQueue()
    frontier.put((start_coor, 0))
    came_from = dict()
    came_from[start_coor] = None
    cost_so_far = dict()
    cost_so_far[start_coor] = 0

    time_start = time.time() # Search time start

    
    iterations = 0
    while not frontier.empty():
        iterations += 1
        current, current_cost = frontier.get() # PRIO [1]
        if current == end_coor:
            break
        y, x = current

        for move_y, move_x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = x + move_x
            new_y = y + move_y
            new_cost = cost_so_far[current] + 1
            
            if validMove(maze, new_y, new_x) and ((new_y, new_x) not in cost_so_far or new_cost < cost_so_far[(new_y, new_x)]):
                cost_so_far[(new_y, new_x)] = new_cost
                priority = heuristic(end_coor, (new_y, new_x)) + new_cost
                frontier.put(((new_y, new_x), priority)) # PRIO ((priority, (new_y, new_x)))
                came_from[(new_y, new_x)] = current

    time_stop = time.time() # Search time end
    printSolution(start_coor, end_coor, came_from, maze, "astar")
    print(f"Time spent A*: {1000*(time_stop - time_start):.3f} ms, Iterations:{iterations}\n")
# -------------------------------------------------------------

# MAIN 

def main():
    print(CAVE_FILE_NAME)
    # print("LAVA_MAP")
    bfs(test_map2)       # Change algo map parameter 
    greedy(test_map2)    # map_data for big maps in files, eg. "cave300x300" etc
    astar(test_map2)     # lava_map1, test_map used for testing
    exit()

if __name__ == "__main__":
    main()

