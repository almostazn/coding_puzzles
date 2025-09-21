import re
REGEX_PATTERN_1 = r"mul\((\d{1,3}),(\d{1,3})\)"
REGEX_PATTERN_2 = r"(don't\(\))|(do\(\))|(mul\((\d{1,3}),(\d{1,3})\))"

def process_2(lines):
    count = 0
    do_count = True
    for line in lines:
        for match in re.findall(REGEX_PATTERN_2, line):
            if match[0] != '':
                do_count = False
            elif match[1] != '': 
                do_count = True
            elif match[2] != '':
                if do_count:
                    count += int(match[3]) * int(match[4])
    print(count)

def process_1(lines):
    count = 0
    for line in lines:
        count += sum([int(x[1]) * int(x[0]) for x in re.findall(REGEX_PATTERN_1, line)])
    print(count)

def main():
    with open('./inputs/2024/day3.txt') as f:
        lines = f.readlines()
        process_2(lines)

if __name__ == '__main__':
    main()
