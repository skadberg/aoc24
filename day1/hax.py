# ho ho ho
import re
import numpy as np

# Task 1
left_numbers = []
right_numbers = []

with open('input.txt', 'r') as file:
    for line in file:
        match = re.match(r'(\d+)\s+(\d+)', line)
        if match:
            left_numbers.append(int(match.group(1))) 
            right_numbers.append(int(match.group(2))) 

left_numbers_sorted = sorted(left_numbers)
right_numbers_sorted = sorted(right_numbers)

diffs = abs(np.subtract(left_numbers_sorted, right_numbers_sorted))

diffs_sum = sum(diffs)

# Answer 1
print(diffs_sum)

# Task 2
num_count_list = []
for left_number in left_numbers:
    num_count = 0
    for right_number in right_numbers:
        if left_number == right_number:
            num_count += 1
    num_count_list.append(num_count)

similarity_list = np.multiply(left_numbers, num_count_list)

similarity_sum = sum(similarity_list)

# Answer 2
print(similarity_sum)