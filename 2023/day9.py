def get_diff(nums):
    diff = []
    current = nums[0]
    for num in nums[1:]:
        diff.append(num - current)
        current = num
    return diff

def get_diff_history(seq):
    history = [seq]
    current = get_diff(seq)
    history.append(current)
    while(not all([n == 0 for n in current])):
        current = get_diff(current)
        history.append(current)
    return history

def extrapolate(seq):
    diff_history = get_diff_history(seq)
    n = 0
    for history in diff_history[::-1]:
        n += history[-1]
    return n

def process(sequences):
    values = []
    for seq in sequences:
        values.append(extrapolate(seq))
    print(sum(values))

def main():
    with open("input/input_9.txt") as f:
        sequences = [ [int(n) for n in line.strip('\n').split() ][::-1] for line in f.readlines()]
        process(sequences)

if __name__ == "__main__":
    main()
