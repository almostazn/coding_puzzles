# A = b/2 + i -1
# I = sum(xi * (yi+1 - yi+2))

def parse_hex(h):
    h = h.strip('()')
    dir_dict = {
        '0': 'R',
        '1': 'D',
        '2': 'L',
        '3': 'U',
    }
    return dir_dict[h[-1]], int(h[1:-1], base=16)
    
def process_lines(lines):
    points = [(0,0)]
    total_steps = 0
    for line in lines:
        d, steps, h = line.split(' ')
        steps = int(steps)
        total_steps += steps
        #d, steps = parse_hex(h)
        match d:
            case 'U':
                offset = (0,-1 * steps)
            case 'D':
                offset = (0,1 * steps)
            case 'L':
                offset = (-1 * steps,0)
            case _ :
                offset = (1 * steps,0)
        prev_point = points[-1]
        points.append((prev_point[0] + offset[0], prev_point[1] + offset[1]))
    int_A = 0  
    for i in range(len(points)):
        if (i + 1) == len(points):
            y_1 = points[0][1]
        else:
            y_1 = points[i+1][1]
        int_A += points[i][0] * ( y_1 - points[i-1][1])
    int_A = abs(int_A // 2)
    adjusted_int_A = int_A - total_steps // 2 + 1
    return adjusted_int_A + total_steps
        
def main():
    with open("input/input_18_small.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
        print('total: ', process_lines(lines))
        

if __name__ == "__main__":
    main()
