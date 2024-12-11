import re
import numpy as np

with open('input.txt', 'r') as file:
    input = file.read().splitlines()

class PageOrder():
    def __init__(self, page):
        self._page = page
        self._precondition = []

    def get_precondition(self):
        return self._precondition
    
    def add_precondition(self, item):
        if item not in self._precondition:
            self._precondition.append(item)
        
regex_pageorders = r"^(\d+)\|(\d+)$"

page_order_list = []
for line in input:
    try:
        page_order_list.append(re.findall(regex_pageorders,line)[0])
    except:
        continue

pages = {}
for page_order_rule in page_order_list:
    if page_order_rule[0] not in pages:
        pages[page_order_rule[0]] = PageOrder(page_order_rule[0])
    pages[page_order_rule[0]].add_precondition(page_order_rule[1])

regex_updates = r"(\d*,\d+)+"
lines = [line for line in input if re.match(regex_updates, line)]
updates = [list(map(int, line.split(","))) for line in lines]

correct_order_updates = []
for update in updates:
    wrong_order = False
    for i in range(len(update)):
        current_number = str(update[i])
        numbers_to_check_against = update[i+1:]
        for number_to_check in numbers_to_check_against:
            try:
                preconditions = pages.get(str(number_to_check)).get_precondition()
            except:
                continue
            if preconditions:
                if current_number in preconditions:
                    wrong_order = True
                    break
        if wrong_order:
            break
    if wrong_order:
        continue
    else:
        correct_order_updates.append(update)

sum_mid_number = 0
for update in correct_order_updates:
    mid_position = round(np.ceil((len(update)/2)-1))
    sum_mid_number += update[mid_position]

print(sum_mid_number)

# part 2
incorrect_order_updates = []
for update in updates:
    wrong_order = True
    sorted_order = update[:]
    while wrong_order:
        wrong_order = False
        to_move = []  

        for i in range(len(sorted_order)):
            for j in range(i + 1, len(sorted_order)):
                current = sorted_order[i]
                to_check = sorted_order[j]
                preconditions = pages.get(str(to_check), PageOrder(to_check)).get_precondition()

                if str(current) in preconditions:
                    wrong_order = True
                    to_move.append((i, j))
                    break
            if wrong_order:
                break

        if to_move:
            for i, j in reversed(to_move):  
                element = sorted_order.pop(i)
                sorted_order.insert(j, element)

    if sorted_order != update: 
        incorrect_order_updates.append(sorted_order)

sum_mid_number = 0
for update in incorrect_order_updates:
    mid_position = (len(update) - 1) // 2
    sum_mid_number += update[mid_position]

print(sum_mid_number)
