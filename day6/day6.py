import copy

with open('input.txt', 'r') as file:
    input = [list(line) for line in file.read().splitlines()]

def find_guard(input_matrix):
    for row_index, row in enumerate(input_matrix):
        for col_index, char in enumerate(row):
            if char in "^>v<":
                return row_index, col_index
    return None

def move_up(position, input_matrix):
    if position:
        row, col = position
    else:
        return False
    if row == 0:
        input_matrix[row][col] = "X"
        return False
    if input_matrix[row-1][col] != "#":
        input_matrix[row][col] = "X"
        input_matrix[row-1][col] = "^"
        return True
    else:
        return False

def move_right(position, input_matrix):
    if position:
        row, col = position
    else:
        return False
    if col == len(input_matrix[row])-1:
        input_matrix[row][col] = "X"
        return False
    if input_matrix[row][col+1] != "#":
        input_matrix[row][col] = "X"
        input_matrix[row][col+1] = ">"
        return True
    else:
        return False

def move_down(position, input_matrix):
    if position:
        row, col = position
    else:
        return False
    if row == len(input_matrix)-1:
        input_matrix[row][col] = "X"
        return False
    if input_matrix[row+1][col] != "#":
        input_matrix[row][col] = "X"
        input_matrix[row+1][col] = "v"
        return True
    else:
        return False

def move_left(position, input_matrix):
    if position:
        row, col = position
    else:
        return False
    if col == 0:
        input_matrix[row][col] = "X"
        return False
    if input_matrix[row][col-1] != "#":
        input_matrix[row][col] = "X"
        input_matrix[row][col-1] = "<"
        return True
    else:
        return False

while find_guard(input):
    while move_up(find_guard(input), input):
        continue
    while move_right(find_guard(input), input):
        continue
    while move_down(find_guard(input), input):
        continue
    while move_left(find_guard(input), input):
        continue

num_X = 1
for row in input:
    for column in row:
        if column == "X":
            num_X += 1
        
print(num_X)


# part 2

with open('input.txt', 'r') as file:
    input = [list(line) for line in file.read().splitlines()]

def add_new_X(input_matrix, row, col):
    input_matrix[col][row] = "#"
    return input_matrix

possible_loops = 0
for row in range(len(input)):
    for column in range(len(input[row])):
        input_copy = copy.deepcopy(input)
        add_new_X(input_copy, row, column)

        loop_count = 0
        while loop_count < 1000 and find_guard(input_copy):
            while move_up(find_guard(input_copy), input_copy):
                continue
            while move_right(find_guard(input_copy), input_copy):
                continue
            while move_down(find_guard(input_copy), input_copy):
                continue
            while move_left(find_guard(input_copy), input_copy):
                continue
            loop_count += 1
            if loop_count >= 1000:
                possible_loops += 1
                break
        print("row ", row, " col ", column, " done")

print(possible_loops)

