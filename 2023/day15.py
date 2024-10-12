

def hash_string(string):
    value = 0
    for c in string:
        value += ord(c)
        value *= 17
        value = value % 256
    return value

def get_operation(step):
    char = '-' if '-' in step else '='
    focal = None
    if char == '=':
        focal = step.split(char)[-1]
    return step.split(char)[0] , char, focal

def get_focusing_power_box(n, box):
    lenses = [v for v in box.values()]
    
    total = 0
    for i, v in enumerate(lenses):
        total += (n + 1) * (i + 1) * int(v)
    return total

def arrange_lenses(lines):
    boxes = [ {} for i in range(256) ]

    for line in lines:
        for step in line.split(','):
            label, operation, focal = get_operation(step)
            box = hash_string(label)

            if operation == '=':
                if label in boxes[box]:
                    boxes[box][label] = focal
                else:
                    boxes[box][label] = focal
            else:
                if label in boxes[box]:
                    del boxes[box][label]

    total = 0
    for i, box in enumerate(boxes):
        total += get_focusing_power_box(i, box)
    return total
        
def process_lines(lines):
    total = arrange_lenses(lines)
    print('total: ', total)
    
def main():
    with open("input/input_15.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
        process_lines(lines)

if __name__ == "__main__":
    main()
