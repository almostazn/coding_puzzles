
NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

PIPES = {
    '|' : [NORTH, SOUTH],
    '-': [EAST, WEST],
    'L': [NORTH, EAST],
    'J': [NORTH, WEST],
    '7': [SOUTH, WEST],
    'F': [SOUTH, EAST],
    }
    
def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return i,j

def add_pos(pos1, pos2):
    return pos1[0] + pos2[0], pos1[1] + pos2[1]

def get_connections(grid):
    connections = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            tile = grid[i][j]
            if tile in PIPES.keys():
                for direction in PIPES[tile]:
                    connection = add_pos((i,j), direction)
                    try:
                        connections[(i,j)].append(connection)
                    except KeyError:
                        connections[(i,j)] = [connection]
    return connections

def get_dist(connections, start):
    dist = 0
    visited = {start}
    queue = [start]

    while len(queue):
        current = queue.pop()
        
        for neighbor in connections[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        dist += 1
    return visited
   
def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return i,j
        
def get_area(grid, edges):
    count = 0
    for i in range(len(grid)):
        intersect = 0
        for j in range(len(grid[0])):
            tile = grid[i][j]
            if ((i,j) in edges) and (tile in '|JL'):
                intersect += 1
            elif intersect % 2 == 1:
                count += 1
    print(count)

def process(lines):
    grid = [ line.strip('\n') for line in lines ]
    #print(find_start(grid))
    start = (1,1)#(60, 75)
    connections = get_connections(grid)
    edges = get_dist(connections, start)
    get_area(grid, edges)

def main():
    with open("input/input_10_small.txt") as f:
        lines = f.readlines()
        process(lines)

if __name__ == "__main__":
    main()
