INPUT_SMALL = [
    [71530],
    [940200]
    ]

INPUT = [
    [53717880],
    [275118112151524]
    ]

def main(races):
    product = 1
    for i in range(len(races[0])):
        time = races[0][i]
        distance = races[1][i]
        finish = 0
        for speed in range(1, time+1):
            time_left = time - speed
            dist_traveled = time_left * speed
            if (dist_traveled > distance):
                finish = finish + 1
        if (finish > 0):
            product = product * finish
    print(product)

if __name__ == "__main__":
    races = INPUT
    main(races)
