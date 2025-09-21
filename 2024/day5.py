from collections import defaultdict
import functools

sample = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
RULES = None

def check_valid_order(rules, num, nums_before):
    return len([value for value in nums_before if value in  rules[num]]) == 0

def create_rules(rules):
    rules_dict = defaultdict(list)
    for r in rules:
        parsed = r.split('|')
        rules_dict[int(parsed[0])].append(int(parsed[1]))
    return rules_dict

def compare(x, y):
    cannot_before = RULES[x]
    if x == y:
        return 0
    elif y in cannot_before:
        return 1
    return -1

def process_2(lines):
    global RULES
    count = 0
    i = lines.index('\n')
    #i = lines.index("")
    updates = [l.strip() for l in lines[i+1:]]
    rules = create_rules([l.strip() for l in lines[:i]])
    RULES = rules
    for update in updates:
        parsed_update = [ int(u) for u in update.split(',') ]
        for i in range(1, len(parsed_update)):
            if (not check_valid_order(rules, parsed_update[i], parsed_update[:i])):
                new_order = sorted(parsed_update, key=functools.cmp_to_key(compare))
                count += new_order[len(new_order) // 2]
                break
    print(count)

def process_1(lines):
    count = 0
    i = lines.index('\n')
    #i = lines.index("")
    updates = [l.strip() for l in lines[i+1:]]
    rules = create_rules([l.strip() for l in lines[:i]])
    for update in updates:
        parsed_update = [ int(u) for u in update.split(',') ]
        for i in range(1, len(parsed_update)):
            if (not check_valid_order(rules, parsed_update[i], parsed_update[:i])):
                break
        else:
            count += parsed_update[len(parsed_update) // 2]
    
    print(count)

def main():
    with open('./inputs/2024/day5.txt') as f:
        lines = f.readlines()
        #process_1(lines)
        process_2(lines)
        #process_2(sample.split('\n')[1:-1])

if __name__ == '__main__':
    main()
