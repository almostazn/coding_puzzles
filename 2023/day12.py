
prev_results = {}

def can_fit(spring, size):
    #print("CAN_FIT", spring, size)
    if len(spring) < size:
        return False
    if '.' in spring[:size]:
        return False
    if len(spring) > size and spring[size] == '#':
        return False

    return True

def get_arrangements(springs, groups):
    if not len(groups):
        if "#" in springs:
            return 0
        else:
            return 1
    if springs == "":
        if len(groups):
            return 0
        else:
            return 1
    results_key = springs + ' ' +  ','.join([str(n) for n in groups])
    if results_key in prev_results:
        return prev_results[results_key]
        
    count = 0
    char = springs[0]
    if char == '.':
        count += get_arrangements(springs[1:], groups)
    if char == '#':
        if can_fit(springs, groups[0]):
            end = groups[0] + 1
            count += get_arrangements(springs[end:], groups[1:])
    if char == '?':
        #check both cases
        count += get_arrangements(springs[1:], groups)
        if can_fit(springs, groups[0]):
            end = groups[0] + 1
            count += get_arrangements(springs[end:], groups[1:])

    prev_results[results_key] = count
    return count

def process_lines(lines):
    total = 0
    for line in lines:
        spring, group = line.split(' ')
        group = [int(num) for num in group.split(',')]
        new_spring = "?".join([ spring for i in range(5)])
        total += get_arrangements(new_spring, group*5)
    print("total:", total)

def main():
    with open("input/input_12.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
        process_lines(lines)

if __name__ == "__main__":
    main()

