
def rotate_grid(grid):
    grid = [list(row) for row in zip(*grid)]
    return ["".join(row[::-1]) for row in grid]

def can_move_up(grid, i, j):
    if i <= 0:
        return False
    return grid[i-1][j] == '.'

def move_up(grid, i, j):
    grid[i-1] = grid[i-1][:j] + grid[i][j] + grid[i-1][j+1:]
    grid[i] = grid[i][:j] + '.' + grid[i][j+1:]

def tilt_grid(grid):
    new_grid = []
    for i, row in enumerate(grid):
        new_grid.append(row)
        for j, c in enumerate(row):
            if c == 'O':
                pos = i
                while can_move_up(new_grid, pos, j):
                    move_up(new_grid, pos, j)
                    pos-=1

    return new_grid

def get_load(grid):
    total = 0
    num_rows = len(grid)
    for i in range(num_rows):
        count = 0
        for c in grid[i]:
            if c == 'O':
                count += 1
        total += (num_rows - i) * count
    return total

def print_grid(grid):
    for row in grid:
        print(row)
    print()

def cycle_grid(grid):
    new_grid = grid
    for r in range(4):
        new_grid = tilt_grid(new_grid)
        new_grid = rotate_grid(new_grid)
    return new_grid

def process_lines(lines):
    NUM_CYCLES = 1000000000
    #NUM_CYCLES = 3
    prev_results = {}

    current = lines
    for i in range(1, NUM_CYCLES+1):
        current = cycle_grid(current)
        grid_state = "".join(current)

        if grid_state in prev_results:
            break
        prev_results[grid_state] = i

    cycle_start = "".join(current)
    cycle_length = i - prev_results[cycle_start]
    cycles_remaining = (NUM_CYCLES - i) % cycle_length 
    print(cycles_remaining)
    
    for j in range(cycles_remaining):
        current = cycle_grid(current)

    print(get_load(current))
    
def main():
    with open("input/input_14.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
        process_lines(lines)

if __name__ == "__main__":
    main()
