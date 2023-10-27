#! /usr/bin/python3

import os

with open(f'{os.path.dirname(os.path.realpath(__file__))}/input', 'r') as f:
    text = f.read()

calories = text.split('\n')
elvies = []
count = 0
for calory in calories:
    if len(calory) != 0:
        count += int(calory)
    else:
        elvies.append(count)
        count = 0

print(max(elvies))

elvies.sort(reverse = True)
print(sum(elvies[:3]))