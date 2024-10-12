#from heapq import heappush, heappop
import heapq

MIN = 4
MAX = 10

def in_bounds(state, grid):
    num_cols = len(grid[0])
    num_rows = len(grid)

    r, c, d = state

    return (0 <= r < num_rows) and (0 <= c < num_cols)

def get_nodes_straight(grid, state, min_steps, max_steps):
    new_states = []
    r, c, d = state

    for i in range(min_steps, max_steps+1):
        if d == 'n':
            new_states.append(( r - i, c, d))
        elif d == 'e':
            new_states.append(( r, c + i, d))
        elif d == 's':
            new_states.append(( r + i, c, d))
        else:
            new_states.append(( r, c - i, d))
    return [state for state in new_states if in_bounds(state, grid)]

def get_new_node_states(grid, current_v, nodes):
    new_states = []
    
    v = current_v
    for node in (nodes):
        r, c, d = node
        v += int(grid[r][c])
        new_states.append((v, r, c, d))

    return new_states

def get_min_v(grid, state):
    v, r, c, d = state
    new_v = v
    for i in range(1, MIN):
        if d == 'w':
            new_v += int(grid[r][c-i])
        elif d == 's':
            new_v += int(grid[r+i][c])
        elif d == 'e':
            new_v += int(grid[r][c+i])
        else:
            new_v += int(grid[r-i][c])
    return new_v

def get_adjacent_nodes(grid, state):
    new_states = []
    v, r, c, d = state

    # can only go left or right
    if d in 'ns':
        if in_bounds((r, c+MIN, d), grid):
            new_v = get_min_v(grid, (v, r, c, 'e'))
            nodes_straight = get_nodes_straight(grid, (r, c, 'e'), MIN, MAX)
            new_states += get_new_node_states(grid, new_v, nodes_straight)
        if in_bounds((r, c-MIN, d), grid):
            new_v = get_min_v(grid, (v, r, c, 'w'))
            nodes_straight_1 = get_nodes_straight(grid, (r, c, 'w'), MIN, MAX)
            new_states += get_new_node_states(grid, new_v, nodes_straight_1)
    elif d in 'ew':
        if in_bounds((r + MIN, c, d), grid):
            new_v = get_min_v(grid, (v, r, c, 's'))
            nodes_straight = get_nodes_straight(grid, (r, c, 's'), MIN, MAX)
            new_states += get_new_node_states(grid, new_v, nodes_straight)
        if in_bounds((r - MIN, c, d), grid):
            new_v = get_min_v(grid, (v, r, c, 'n'))
            nodes_straight_1 = get_nodes_straight(grid, (r, c, 'n'), MIN, MAX)
            new_states += get_new_node_states(grid, new_v, nodes_straight_1)

    return new_states
    
def traverse_grid(grid, start):
    #dijkstras
    visited = set()
    q = start

    while q:
        current = heapq.heappop(q)
        cv, cr, cc, cd = current

        for i in  get_nodes_straight(grid, (cr,cc,cd), 1, 4):
            visited.add(i)

        #reached end
        if (cr,cc) == (len(grid)-1, len(grid[0])-1):
            return cv

        for node in get_adjacent_nodes(grid, current):
            v,r,c,d = node
            if (r, c, d) not in visited:
                heapq.heappush(q, node)

def process_lines(lines):
    #v, r, c, d
    start = [(0, 0, 0, 's'), (0, 0, 0, 'e')]
    v = traverse_grid(lines, start)
    print(v)
    
def main():
    with open("input/input_17.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
        process_lines(lines)

if __name__ == "__main__":
    main()
