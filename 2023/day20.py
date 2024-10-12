from collections import deque
import math

ADJ_dict = {}
MOD_dict = {}
P_dict = {}
CYCLE_dict = {}

#lo = false
#hi = true
class Module():
    def __init__(self, name, t, state):
        self.name = name
        self.t = t
        self.state = state

    def __str__(self):
        return f"name={self.name}, t={self.t}, state=({self.state})"

def parse_input(lines):
    parents_dict = {}
    adjacency_dict = {}
    module_dict = {}

    inverters = []
    for line in lines:
        module, neighbor = [l.strip() for l in line.split('->')]
        neighbor = [n.strip() for n in neighbor.split(',')]
        t = module
        name = module
        if module[0] in '%&':
            t = module[0]
            name = module[1:]
            state = False
            if t == '&':
                inverters.append(name)
        for child in neighbor:
            try:
                parents_dict[child].append(name)
            except KeyError:
                parents_dict[child] = [name]
        adjacency_dict[name] = neighbor
        module_dict[name] = Module(name, t, False)

    return adjacency_dict, module_dict, parents_dict

def get_next_states(name, pulse):
    try: 
        mod_type = MOD_dict[name].t
    except KeyError:
        return []
    next_states = []
    match mod_type:
        case 'broadcaster':
            MOD_dict[name].state = pulse
            for child in ADJ_dict[name]:
                next_states.append((child, pulse))
        case '%':
            if not pulse:
                MOD_dict[name].state = not MOD_dict[name].state
                for child in ADJ_dict[name]:
                    next_states.append((child, MOD_dict[name].state))
        case '&':
            if all( MOD_dict[p].state for p in P_dict[name] ):
                MOD_dict[name].state = False
            else:
                MOD_dict[name].state = True
            for child in ADJ_dict[name]:
                next_states.append((child, MOD_dict[name].state))
                
    return next_states

def press_button(i):
    high_count = 0
    low_count = 0
    q = deque()
    
    q.append(("broadcaster", False))
    while q:
        name, pulse = q.popleft()
        
        if name in CYCLE_dict.keys():
            if MOD_dict[name].state:
                CYCLE_dict[name] = i
        if pulse:
            high_count +=1
        else:
            low_count += 1

        next_states = get_next_states(name, pulse)
        for state in next_states:
            q.append(state)
    return high_count, low_count
        
def process_lines(lines):
    global ADJ_dict, MOD_dict, P_dict, CYCLE_dict
    ADJ_dict, MOD_dict, P_dict = parse_input(lines)
    rx_parent ='lg'
    #find cycle of receiving high pulse from all children of rx_parent
    CYCLE_dict = { c: None for c in P_dict[rx_parent]}
    #high_total = 0
    #low_total = 0
    i = 1
    while True:
        if all( v != None for v in CYCLE_dict.values()):
            break
        press_button(i)
        i+=1

    #    high_total += pulses[0]
    #    low_total += pulses[1]
    #print(high_total * low_total)
    print(math.lcm(*[v for v in CYCLE_dict.values()]))
    
def main():
    with open("input/input_20.txt") as f:
        lines = [line.strip('\n') for line in f.readlines()]
        process_lines(lines)

if __name__ == "__main__":
    main()
