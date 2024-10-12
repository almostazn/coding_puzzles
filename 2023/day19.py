from collections import deque

def parse_workflow(lines):
    workflow = {}
    for line in lines:
        key, flow = line.strip('{}').replace('{',' ').split(' ')
        workflow[key] = flow.split(',')
    return workflow

def parse_part(line):
    part = {}
    for pair in [p.split('=') for p in line.strip('{}').split(',')]:
        part[pair[0]] = int(pair[1])
    return part

def parse_step(step):
    key = None
    op = None
    rest = None
    if '>' in step:
        key, rest = step.split('>')
        op = '>'
    if '<' in step:
        key, rest = step.split('<')
        op = '<'
    v, s = rest.split(':')
    return (key, op, int(v), s)
    
def check_step(part, step):
    if '<' in step:
        key, rest = step.split('<')
        rating, state = rest.split(':')
        return int(part[key]) < int(rating)
    else:
        key, rest = step.split('>')
        rating, state = rest.split(':')
        return int(part[key]) > int(rating)
        
def is_accepted(part, workflow):
    state = 'in'
    while True:
        if state == 'A' or state == 'R':
            break
        
        workflow_length = len(workflow[state])
        for i, step in enumerate(workflow[state]):
            if i == workflow_length - 1:
                state = step
                break
            if check_step(part, step):
                state = step.split(':')[-1]
                break
            
    return state == 'A'

def update_ranges(op, v, key, current):
    if op == '<':
        return (current[key][0], v-1), (v, current[key][1])
    else:
        return (v + 1, current[key][1]), (current[key][0], v)
    return p1, p2

#traverse through the paths (workflow)
#adjust ranges as steps are completed
#when accept state reached return product of ranges
def get_combinations(workflow, current):
    s, part = current
    match s:
        case 'R':
            return 0
        case 'A':
            product = 1
            for r in part.values():
                product *= r[1] - r[0] + 1
            return product
        case _:
            steps = workflow[s]
            total = 0
            for step in steps[:-1]:
                key, op, v, new_s = parse_step(step)
                p1, p2 = update_ranges(op, v, key, part)
                # go to true state
                if p1[0] and p1[1]:
                    #update range
                    new_part = dict(part)
                    new_part[key] = p1
                    total += get_combinations(workflow, (new_s, new_part))
                # go to false state
                if p2[0] and p2[1]:
                    part = dict(part)
                    part[key] = p2

            total += get_combinations(workflow, (steps[-1], part))
            return total

def process_lines(lines):
    blank_line = lines.index("")
    workflow = parse_workflow(lines[:blank_line])
    init_part= {}
    for c in 'xmas':
        init_part[c] = [1,4000]
    print(get_combinations(workflow, ('in', init_part)))

    parts = [parse_part(line) for line in lines[blank_line+1:]]
    total = 0
    for part in parts:
        if is_accepted(part, workflow):
            for k,v in part.items():
                total += int(v)
    #print(total)

def main():
    with open("input/input_19.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
        process_lines(lines)

if __name__ == "__main__":
    main()
