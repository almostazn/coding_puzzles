

def has_one_diff(l1, l2):
    diff = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            diff +=1

    return diff == 1

def is_reflect(pattern, start):
    i =  start
    j = start + 1
    repairs = 0

    while i >= 0 and j < len(pattern):
        if pattern[i] != pattern[j]:
            if repairs == 0 and has_one_diff(pattern[i], pattern[j]):
                repairs +=1
            else:
                return False
        i-=1
        j+=1

    return repairs == 1        
    
def get_reflect_line(pattern):
    for start in range(len(pattern) - 1):
        if is_reflect(pattern, start):
            return start + 1

    return 0

def transpose(l1, l2):
    # iterate over list l1 to the length of an item 
    for i in range(len(l1[0])):
        # print(i)
        row =[]
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2

def process_lines(lines):
    patterns = []
    current = [];
    for line in lines:
        if line == '':
            patterns.append(current)
            current = []
        else:
            current.append(line)
    patterns.append(current)
        
    total = 0
    for pattern in patterns:
        pattern_t = []
        transpose(pattern, pattern_t)
        vertical_line = get_reflect_line(pattern_t)
        horizontal_line = get_reflect_line(pattern)

        total += (100 * horizontal_line)
        total += (vertical_line)
        #break
    print('total: ', total)

def main():
    with open("input/input_13.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
        process_lines(lines)

if __name__ == "__main__":
    main()
