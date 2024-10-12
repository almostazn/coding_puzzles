
def get_galaxy_coords(grid):
    galaxy = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '#':
                galaxy.append((r,c))
    return galaxy

def print_grid(grid):
    for r in grid:
        print(r)
        
def expand_galaxy(grid):
    SCALE = 2
    new_grid = []
    empty_rows = [ i for i, r in enumerate(grid) if '#' not in r]
    empty_cols = [i for i in range(len(grid[0])) if '#' not in [row[i] for row in grid]]

    for i, r in enumerate(grid):
        new_grid.append(r)
        if i in empty_rows:
            new_grid.append('.' * len(r))

    new_grid_1 = []
    for i, r in enumerate(new_grid):
        new_row = ''
        for j, y in enumerate(r):
            if j in empty_cols:
                new_row+= '.' * SCALE
            else:
                new_row+= y
        new_grid_1.append(new_row)

    return new_grid_1

def get_manhattan_dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def process_lines(grid):
    #grid = expand_galaxy(lines)
    galaxy_coords = get_galaxy_coords(grid)
    empty_rows = [ i for i, r in enumerate(grid) if '#' not in r]
    empty_cols = [i for i in range(len(grid[0])) if '#' not in [row[i] for row in grid]]
    total = 0
    for i in range(len(galaxy_coords)):
        for j in range(i+1, len(galaxy_coords)):
            c1 = galaxy_coords[i]
            c2 = galaxy_coords[j]
            for r in range(min(c1[0], c2[0]), max(c1[0], c2[0])):
                if r in empty_rows:
                    total += 1000000
                else:
                    total += 1
            for c in range(min(c1[1], c2[1]), max(c1[1], c2[1])):
                if c in empty_cols:
                    total += 1000000
                else:
                    total += 1
    print(total)

def main():
    with open("input/input_11.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
        process_lines(lines)

if __name__ == "__main__":
    main()
