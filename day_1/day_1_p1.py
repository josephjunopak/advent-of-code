def most_left_right_sum(line):
    left_value = ""
    right_value = ""
    # two pointers: one from left, another from the right
    left_p = 0
    right_p = len(line) - 1
    
    for _ in range(len(line)):
        # find the numbers from the left and right side
        
        # if we find the first number on either side, stop looking on that side
        if not left_value:
            if (line[left_p].isdigit()):
                left_value += line[left_p]
            else:
                left_p += 1

        if not right_value:
            if (line[right_p].isdigit()):
                right_value += line[right_p]
            else:
                right_p -= 1
        
        if left_value and right_value:
            return(int(left_value + right_value))

if __name__ == "__main__":
    with open("day_1.in") as f:
        lines = f.read().splitlines()

    total = 0
    for line in lines:
        total += most_left_right_sum(line)


    print(total)





