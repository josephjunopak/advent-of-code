with open("day_3.in") as f:
    lines = f.read().splitlines()
    line_length = len(lines[0])


def is_adj_to_symbol(line_num, start, end):
    ret = False

    prev_line = line_num - 1
    next_line = line_num + 1

    if start > 0:
        start = start - 1

    if end < line_length - 1:
        end = end + 1

    # Check prev line
    for c in lines[prev_line][start : end + 1]:
        if c.isdigit() or c == ".":
            continue
        ret = True

    # Check next line
    for c in lines[next_line][start : end + 1]:
        if c.isdigit() or c == ".":
            continue

        ret = True

    # Check current line
    char_before = lines[line_num][start]
    char_after = lines[line_num][end]

    if not char_before.isdigit() and char_before != ".":
        ret = True

    if not char_after.isdigit() and char_after != ".":
        ret = True

    return ret


total_sum = 0
# Check if a number is adjacent to a symbol
for line_num, line  in enumerate(lines):
    num_locations = []
    num_value = ""
    for char_index in range(len(lines[line_num])):
        c = lines[line_num][char_index]

        if c.isdigit():
            num_locations.append(char_index)
            num_value += c
        else:
            # check if index_list is not empty, check if symbol is adjacent
            if num_locations and is_adj_to_symbol(
                line_num, num_locations[0], num_locations[-1]
            ):
                total_sum += int(num_value)

            num_locations = []
            num_value = ""

        # to account for numbers are the end of grid
        if (
            (char_index == line_length - 1)
            and num_locations
            and is_adj_to_symbol(line_num, num_locations[0], num_locations[-1])
        ):
            total_sum += int(num_value)

print(total_sum)
