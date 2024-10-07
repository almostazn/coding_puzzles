def is_valid_pos(i, j, n, m):
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return False
    return True

def is_symbol(char):
    return not char.isdigit() and char != '.'

def create_grid(lines):
    grid = []
    for line in lines:
        row = []
        for char in line:
            if char != '\n':
                row.append(char)
        grid.append(row)
    return grid

def get_digit(row, i):
    digit_string = ''
    for char in reversed(row[:i]):
        if(not char.isdigit()):
            break
        digit_string = char + digit_string
    for char in row[i:]:
        if(not char.isdigit()):
            break
        digit_string += char
    if len(digit_string):
        return int(digit_string)
    return 0

def find_adjacent_nums(arr, cords):
    adjacent_nums = []
    n = len(arr)
    m = len(arr[0])
    i, j = cords

    if (is_valid_pos(i - 1, j - 1, n, m)):
        char = arr[i - 1][j - 1]
        if (char.isdigit()):
            adjacent_nums.append(get_digit(arr[i-1], j-1))
    if (is_valid_pos(i - 1, j, n, m)):
        char = arr[i - 1][j]
        if (char.isdigit()):
            adjacent_nums.append(get_digit(arr[i-1], j))
    if (is_valid_pos(i - 1, j + 1, n, m)):
        char = arr[i - 1][j+1]
        if (char.isdigit()):
            adjacent_nums.append(get_digit(arr[i-1], j+1))
    if (is_valid_pos(i, j - 1, n, m)):
        char = arr[i][j-1]
        if (char.isdigit()):
            adjacent_nums.append(get_digit(arr[i], j-1))
    if (is_valid_pos(i, j + 1, n, m)):
        char = arr[i][j+1]
        if (char.isdigit()):
            adjacent_nums.append(get_digit(arr[i], j+1))
    if (is_valid_pos(i + 1, j - 1, n, m)):
        char = arr[i + 1][j-1]
        if (char.isdigit()):
            adjacent_nums.append(get_digit(arr[i+1], j-1))
    if (is_valid_pos(i + 1, j, n, m)):
        char = arr[i+1][j]
        if (char.isdigit()):
            adjacent_nums.append(get_digit(arr[i+1], j))
    if (is_valid_pos(i + 1, j + 1, n, m)):
        char = arr[i+1][j+1]
        if (char.isdigit()):
            adjacent_nums.append(get_digit(arr[i+1], j+1))

    return set(adjacent_nums)

def get_adjacent_nums(grid):
    adjacent_nums = []
    for i,row in enumerate(grid):
        for j,char in enumerate(row):
            if is_symbol(char):
                nums = find_adjacent_nums(grid, (i,j))
                if char == '*' and len(nums) == 2:
                    nums = list(nums)
                    adjacent_nums.append(nums[0]*nums[1])
    return adjacent_nums

def process_lines(lines):
    grid = create_grid(lines)
    nums = get_adjacent_nums(grid)
    print(nums)
    return sum(nums)

def main():
    with open("input/input_3.txt") as f:
        lines = f.readlines()
        result = process_lines(lines)
        print(result)
if __name__ == "__main__":
    main()
