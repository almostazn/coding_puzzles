from collections import deque

def in_bounds(state, grid):
    num_cols = len(grid[0])
    num_rows = len(grid)

    r, c, d = state

    return (0 <= r < num_rows) and (0 <= c < num_cols)

def get_adjacent_nodes(grid, state):
    new_states = []
    r, c, d = state
    tile = grid[r][c]
    if tile == "|":
        if d in 'we':
            new_states.append(( r+1, c, 's'))
            new_states.append(( r-1, c, 'n'))
        else:
            if d == 'n':
                new_states.append(( r-1, c, d))
            else:
                new_states.append(( r+1, c, d))
    elif tile == "-":
        if d in 'sn':
            new_states.append(( r, c+1, 'e'))
            new_states.append(( r, c-1, 'w'))
        else:
            if d == 'e':
                new_states.append(( r, c+1, d))
            else:
                new_states.append(( r, c-1, d))
    elif tile == '/':
        if d == 'n':
            new_states.append(( r, c+1, 'e'))
        elif d == 's':
            new_states.append(( r, c-1, 'w'))
        elif d == 'e':
            new_states.append(( r-1, c, 'n'))
        else:
            new_states.append(( r+1, c, 's'))
    elif tile == '\\':
        if d == 's':
            new_states.append(( r, c+1, 'e'))
        elif d == 'n':
            new_states.append(( r, c-1, 'w'))
        elif d == 'w':
            new_states.append(( r-1, c, 'n'))
        else:
            new_states.append(( r+1, c, 's'))
    else:
        if d == 'n':
            new_states.append(( r-1, c, d))
        elif d == 's':
            new_states.append(( r+1, c, d))
        elif d == 'e':
            new_states.append(( r, c+1, d))
        else:
            new_states.append(( r, c-1, d))

    return [ state for state in new_states if in_bounds(state, grid) ]
    

def get_grid_edges(num_rows, num_cols):
    grid_edges = []
    for i in range(num_rows):
        grid_edges.append((i, 0, 'e'))
        grid_edges.append((i, num_cols - 1, 'w'))

    for j in range(num_cols):
        grid_edges.append((0, j, 's'))
        grid_edges.append((num_rows - 1, j, 'n'))

    return grid_edges
def traverse_grid(grid, start):
    #bfs
    visited = set()
    q = deque()
    
    #directions clockwise
    # n e s w
    q.append(start)
    visited.add(start)
    while q:
        current = q.popleft()
        for node in get_adjacent_nodes(grid, current):
            if node not in visited:
                visited.add(node)
                q.append(node)
    return visited

def process_lines(lines):
    max_visited = 0
    start_list = get_grid_edges(len(lines), len(lines[0]))
    for start in start_list:
        visited = traverse_grid(lines, start)
        nodes = set()
        for val in visited:
           r, c, d = val
           nodes.add((r,c))
        max_visited = max(max_visited, len(nodes))
    print(max_visited)
    
def main():
    with open("input/input_16.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
        process_lines(lines)

if __name__ == "__main__":
    main()
