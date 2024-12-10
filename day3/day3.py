import re
input = []
with open('input.txt', 'r') as file:
    for line in file:
        input.append(line)

def mul(x,y):
    return x*y

regex = r"mul\((\d*),(\d*)\)"

sum = 0
for line in input:
    matches = re.findall(regex,line)
    for numbers in matches:
        sum += mul(int(numbers[0]), int(numbers[1]))

print(sum)

regex = r"(do(n't)?\(\))|mul\((\d*),(\d*)\)"
sum = 0
do_calc = True

for line in input:
    matches = re.findall(regex,line)
    for numbers in matches:
        if numbers[0] == "do()":
            do_calc = True
        elif numbers[0] == "don't()":
            do_calc = False

        if do_calc:
            try:
                sum += mul(int(numbers[2]), int(numbers[3]))
            except:
                lol = True

print(sum)