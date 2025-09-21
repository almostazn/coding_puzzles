sample = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''

def report_is_safe(processed_report):
    diff = processed_report[1] - processed_report[0]

    if (abs(diff) > 3 or diff == 0):
        return False
    #decreasing
    elif (diff < 0):
        for i in range(1, len(processed_report) - 1):
            dec_diff = processed_report[i+1] - processed_report[i]
            if (dec_diff < -3 or dec_diff >= 0):
                return False
        else:
            return True
    #increasing
    elif (diff > 0):
        for i in range(1, len(processed_report) - 1):
            inc_diff = processed_report[i+1] - processed_report[i]
            if (inc_diff <= 0 or inc_diff > 3):
                return False
        else:
            return True
    return False

def process_2(reports):
    safe = 0
    for report in reports:
        processed_report = [int(level.strip()) for level in report.split(' ') ]
        if (report_is_safe(processed_report) == -1):
            safe += 1
        else:
            for i in range(len(processed_report)):
                copy = processed_report.copy()
                copy.pop(i)
                if (report_is_safe(copy)):
                    safe += 1
                    break
    print(safe)


def process_1(reports):
    safe = 0
    for report in reports:
        processed_report = [int(level.strip()) for level in report.split(' ') ]
        if (report_is_safe(processed_report)):
            safe += 1
    print(safe)


def main():
    with open('./inputs/2024/day2.txt') as f:
        lines = f.readlines()
        process_2(lines)
        #process_2(sample.split('\n')[1:-1])

if __name__ == '__main__':
    main()
