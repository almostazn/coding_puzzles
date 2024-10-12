from collections import deque

def in_bounds(state, grid):
    num_cols = len(grid[0])
    num_rows = len(grid)

    r, c = state

    return (0 <= r < num_rows) and (0 <= c < num_cols) and grid[r][c] != '#'

def get_adjacent_nodes(grid, state):
    r, c = state
    adjacent_nodes = [
            (r+1,c),
            (r-1,c),
            (r,c+1),
            (r,c-1),
        ]
    return [ node for node in adjacent_nodes if in_bounds(node, grid)]
    
def traverse_grid(grid, start):
    #bfs
    reachable = {}
    visited = {start}
    q = deque([(start[0], start[1], 0)])
    
    while q:
        r, c, steps = q.popleft()
        reachable[(r,c)] = steps
        for new_r, new_c in get_adjacent_nodes(grid, (r,c)):
            if (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                q.append((new_r, new_c, steps + 1))
    return reachable

def process_lines(lines):
    start = [(i, line.index('S')) for i, line in enumerate(lines) if 'S' in line][0]
    reachable = traverse_grid(lines, start)

    even_parity_corner = len([ step for step in reachable.values() if (step % 2 == 0 and step > len(lines) // 2)])
    odd_parity_corner = len([ step for step in reachable.values() if (step % 2 == 1 and step > len(lines) // 2)])
    even_parity = len([ step for step in reachable.values() if step % 2 == 0])
    odd_parity = len([ step for step in reachable.values() if step % 2 == 1])
    
    n = (26501365 - len(lines) // 2) // len(lines)
    p2 = ((n+1)*(n+1)) * odd_parity + (n*n) * even_parity - (n+1) * odd_parity_corner + n * even_parity_corner
    print(p2)

def main():
    with open("input/input_21.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
        process_lines(lines)

if __name__ == "__main__":
    main()
