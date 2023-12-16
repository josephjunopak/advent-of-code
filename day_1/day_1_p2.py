from day_1_p1 import most_left_right_sum

mapping = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

if __name__ == '__main__':
    with open('day_1.in') as f:
        data = f.read()

        for name, value in mapping.items():
            data = data.replace(name, value)
        
        lines = data.splitlines()

    total = 0
    
    for line in lines:
        total += most_left_right_sum(line)


    print(total)