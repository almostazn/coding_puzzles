CONSTRAINT = (12, 13, 14)

def is_possible(counts):
    print(counts)
    red_count = 0
    blue_count = 0
    green_count = 0
    for count in counts:
        r,g,b = count
        red_count = max(red_count, r)
        green_count = max(green_count, g)
        blue_count = max(blue_count, b)
    cr, cg, cb = CONSTRAINT
    print(red_count, blue_count, green_count)
    return red_count <= cr and green_count <= cg and blue_count <= cb

def power_set(counts):
    red_count = 0
    blue_count = 0
    green_count = 0
    for count in counts:
        r,g,b = count
        red_count = max(red_count, r)
        green_count = max(green_count, g)
        blue_count = max(blue_count, b)
    return red_count * blue_count * green_count

def get_ball_counts(line):
    hands = line.split(':')[1:][0].split(';')
    counts = []
    for hand in hands:
        cubes = hand.split(',')
        rgb = [0,0,0]
        for cube in cubes:
            parsed_cube = cube.split(' ')[1:]
            count, color = parsed_cube
            count = int(count)
            if color == 'red':
                rgb[0] = count
            elif color == 'green':
                rgb[1] = count
            else:
                rgb[2] = count
        counts.append(rgb)
    return counts
    
def process_lines(lines):
    possible = []
    for i, line in enumerate(lines):
        game_number = i + 1
        ball_counts = get_ball_counts(line.strip('\n'))
        possible.append(power_set(ball_counts))
    return sum(possible)

def main():
    with open("input/input_2_small.txt") as f:
        lines = f.readlines()
        game_sum = process_lines(lines)
        print(game_sum)

if __name__ == "__main__":
    main()
