from collections import defaultdict

def process_2(lines):
    count_left = defaultdict(int)
    count_right = defaultdict(int)
    similarity = 0
    for line in lines:
        split_line = line.split(' ')
        count_left[split_line[0]] += 1
        count_right[split_line[len(split_line) - 1].strip()] += 1

    for key in count_left.keys():
        if key in count_right:
            similarity += int(key) * count_right[key]
        
    print(similarity)

def process_1(lines):
    left_list = []
    right_list = []
    distance = 0
    for line in lines:
        split_line = line.split(' ')
        left_list.append(int(split_line[0]))
        right_list.append(int(split_line[len(split_line) - 1].strip()))
    left_list.sort()
    right_list.sort()

    for n1, n2 in zip(left_list, right_list):
        distance += abs(n1 - n2)
    print(distance)

def main():
    with open('./inputs/2024/day1.txt') as f:
        lines = f.readlines()
        process_2(lines)

if __name__ == '__main__':
    main()
