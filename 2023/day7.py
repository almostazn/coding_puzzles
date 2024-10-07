card_to_char = {
    'A': 'Z',
    'K': 'Y',
    'Q': 'X',
    'T': 'W',
    'J': '0',
    }

def get_hand_value(hand):
    cards = ''.join([card_to_char.get(char, char) for char in hand[0]])

    char_count = {}
    for char in cards:
        try:
            char_count[char] += 1
        except KeyError:
            char_count[char] = 1
    count = [(k,v) for k,v in char_count.items() if k != '0']
    count.sort(key = lambda x: x[1])

    cards1 = cards
    if (len(count)):
        print(count)
        cards1 = cards.replace('0', count[-1][0])
    hand_count = [cards1.count(char) for char in cards1]

    hand_string = ''
    
    if 5 in hand_count:
        hand_string += '6'
    elif 4 in hand_count:
        hand_string += '5'
    elif 3 in hand_count and 2 in hand_count:
        hand_string += '4'
    elif 3 in hand_count:
        hand_string += '3'
    elif hand_count.count(2) == 4:
        hand_string += '2'
    elif 2 in hand_count:
        hand_string += '1'
    else:
        hand_string += '0'
    print(hand_string+cards, cards1, hand[0])
    return hand_string + cards

def parse_line(line):
    parsed_line = line.split(' ')
    return parsed_line[0], int(parsed_line[1])
    
def process_lines(lines):
    tuple_list = [parse_line(line) for line in lines]
    tuple_list.sort(key = get_hand_value)
    total = 0
    print(tuple_list)
    for i, value in enumerate(tuple_list):
        total += ((i+1) * value[1])
    return total
    
def main():
    with open("input/input_7.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
        result = process_lines(lines)
        print(result)

if __name__ == "__main__":
    main()
