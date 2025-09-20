INPUT = '''
noop
addx 12
addx -5
addx -1
noop
addx 4
noop
addx 1
addx 4
noop
addx 13
addx -8
noop
addx -19
addx 24
addx 1
noop
addx 4
noop
addx 1
addx 5
addx -1
addx -37
addx 16
addx -13
addx 18
addx -11
addx 2
addx 23
noop
addx -18
addx 9
addx -8
addx 2
addx 5
addx 2
addx -21
addx 26
noop
addx -15
addx 20
noop
addx 3
noop
addx -38
addx 3
noop
addx 26
addx -4
addx -19
addx 3
addx 1
addx 5
addx 3
noop
addx 2
addx 3
noop
addx 2
noop
noop
noop
noop
addx 5
noop
noop
noop
addx 3
noop
addx -30
addx -4
addx 1
addx 18
addx -8
addx -4
addx 2
noop
addx 7
noop
noop
noop
noop
addx 5
noop
noop
addx 5
addx -2
addx -20
addx 27
addx -20
addx 25
addx -2
addx -35
noop
noop
addx 4
addx 3
addx -2
addx 5
addx 2
addx -11
addx 1
addx 13
addx 2
addx 5
addx 6
addx -1
addx -2
noop
addx 7
addx -2
addx 6
addx 1
addx -21
addx 22
addx -38
addx 5
addx 3
addx -1
noop
noop
addx 5
addx 1
addx 4
addx 3
addx -2
addx 2
noop
addx 7
addx -1
addx 2
addx 4
addx -10
addx -19
addx 35
addx -1
noop
noop
noop
'''

INPUT_1 = '''
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
'''

INPUT_1: '''
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
'''
def draw_sprite():
    pass

def get_signal_strength(cycle, value):
    return cycle * value

if __name__ == '__main__':
    parsed_input = INPUT.split('\n')[1:][:-1]

    signal_strength_list = []
    X_register = 1
    cycle_limit = 240
    cycle = 1
    completed_cycle = None
    num_pixels = 40
    row = ['#']

    for command in parsed_input:
        if cycle > cycle_limit:
            break
        if command == 'noop':
            increment = 1
        else:
            value = int(command.split(" ")[-1])
            increment = 2
            completed_cycle = cycle + 2

        for i in range(increment):
            current_pixel = cycle % 40
            if ((cycle) % 40) == 0:
                signal_strength_list.append(get_signal_strength(cycle, X_register))
                print(''.join(row))
                row = []
            cycle += 1
            if completed_cycle == cycle:
                X_register += value
            if abs(current_pixel - X_register) <= 1:
                row.append('#')
            else:
                row.append('.')

    print(X_register)
    print(signal_strength_list)  
    print(sum(signal_strength_list))            
        
    
        
    
