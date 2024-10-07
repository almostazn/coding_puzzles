
def create_node_map(nodes):
    node_map = {}
    for node in nodes:
        parse = node.split('=')
        key = parse[0].strip(' ')
        values = parse[-1].strip(' ()').split(',')
        node_map[key] = (values[0].strip(' '), values[1].strip(' '))
    return node_map

def process_lines(lines):
    instructions = lines[0]
    node_map = create_node_map(lines[2:])
    print(node_map)
    current_nodes = [key for key in node_map.keys() if key[-1] == 'A']
    steps = 0
    while (not all([node[-1] == 'Z' for node in current_nodes])):
        direction = 0 if ( instructions[steps % len(instructions)] == 'L') else 1
        current_nodes = [node_map[node][direction] for node in current_nodes]
        steps += 1
    print(steps)

def main():
    with open("input/input_8.txt") as f:
        lines = f.readlines()
        process_lines([line.strip('\n') for line in lines])

if __name__ == "__main__":
    main()
