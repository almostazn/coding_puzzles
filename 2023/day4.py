
CARD_MULTI = {}

def get_acutal_numbers(line):
    new_line = line.split('|')
    return [ int(s) for s in new_line[-1].split(' ') if s.isdigit()]

def get_winning_numbers(line):
    new_line = line.split('|')
    return [ int(s) for s in new_line[0].split(' ') if s.isdigit()]

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def get_score(winning_numbers):
    length = len(winning_numbers)
    if not length:
        return 0
    return 2**(len(winning_numbers)-1)

def process_lines(lines):
    total = 0
    for line in lines:
        parsed_line = line.strip('\n').split(':')[1:][0]
        winning_numbers = get_winning_numbers(parsed_line)
        actual_numbers = get_acutal_numbers(parsed_line)
        total += get_score(intersection(winning_numbers, actual_numbers))
    return total

def process_lines_2(lines):
    total = 0
    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        parsed_line = line.strip('\n').split(':')[1:][0]
        winning_numbers = get_winning_numbers(parsed_line)
        actual_numbers = get_acutal_numbers(parsed_line)
        length = len(intersection(winning_numbers, actual_numbers))
        for j in range(length):
            cards[i+j+1] += cards[i]
            print(cards)
    return sum(cards)

def main():
    with open("input/input_4_small.txt") as f:
        lines = f.readlines()
        total = process_lines_2(lines)
        print(total)

if __name__ == "__main__":
    main()
