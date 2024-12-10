import re
import numpy as np

def get_diagonals(input):
    array = np.array([list(row) for row in input])
    diagonals = [''.join(array.diagonal(offset)) for offset in range(-array.shape[0] + 1, array.shape[1])]
    return diagonals

def rotate(input):
    array = np.array([list(row) for row in input])  
    rotated = np.fliplr(array.T) 
    return [''.join(row) for row in rotated]  


with open('input.txt', 'r') as file:
    input = file.read().splitlines()

input_transposed = [''.join(row) for row in zip(*input)]
input_diagnoals = get_diagonals(input)
input_rotated = rotate(input)
input_rotated_diagnoals = get_diagonals(input_rotated)

regex_XMAS = r"XMAS"
regex_SAMX = r"SAMX"

sum = 0
for line in input:
    matches_XMAS = re.findall(regex_XMAS,line)
    matches_SAMX = re.findall(regex_SAMX,line)
    sum += len(matches_XMAS)
    sum += len(matches_SAMX)
    
for line in input_transposed:
    matches_XMAS = re.findall(regex_XMAS,line)
    matches_SAMX = re.findall(regex_SAMX,line)
    sum += len(matches_XMAS)
    sum += len(matches_SAMX)

for line in input_diagnoals:
    matches_XMAS = re.findall(regex_XMAS,line)
    matches_SAMX = re.findall(regex_SAMX,line)
    sum += len(matches_XMAS)
    sum += len(matches_SAMX)

for line in input_rotated_diagnoals:
    matches_XMAS = re.findall(regex_XMAS,line)
    matches_SAMX = re.findall(regex_SAMX,line)
    sum += len(matches_XMAS)
    sum += len(matches_SAMX)
    
print(sum)

# task 2

def find_xmas_patterns(input):
    patterns = [
        np.array([["M", 0, "M"], [0, "A", 0], ["S", 0, "S"]]),
        np.array([["M", 0, "S"], [0, "A", 0], ["M", 0, "S"]]),
        np.array([["S", 0, "S"], [0, "A", 0], ["M", 0, "M"]]),
        np.array([["S", 0, "M"], [0, "A", 0], ["S", 0, "M"]]),
    ]
    array = np.array([list(row) for row in input])  
    rows, cols = array.shape
    matches = 0

    for i in range(rows - 2):  
        for j in range(cols - 2):  
            window = array[i:i+3, j:j+3]  
            for pattern in patterns:
                mask = (pattern != "0")
                if np.all(window[mask] == pattern[mask]):
                    matches += 1
    return matches

# Find matches
matches = find_xmas_patterns(input)

print(matches)
