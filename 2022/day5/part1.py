import sys
import numpy as np

# stacks = [
#     ['Z', 'N'],
#     ['M', 'C', 'D'],
#     ['P']
# ]

stacks = [
    ['M', 'J', 'C', 'B', 'F', 'R', 'L', 'H'],
    ['Z', 'C', 'D'],
    ['H', 'J', 'F', 'C', 'N', 'G', 'W'],
    ['P', 'J', 'D', 'M', 'T', 'S', 'B'],
    ['N', 'C', 'D', 'R', 'J'],
    ['W', 'L', 'D', 'Q', 'P', 'J', 'G', 'Z'],
    ['P', 'Z', 'T', 'F', 'R', 'H'],
    ['L', 'V', 'M', 'G'],
    ['C', 'B', 'G', 'P', 'F', 'Q', 'R', 'J']
]

def main():
    dataFile = sys.argv[1]
    data = open(dataFile)
    totalStacks = 0
    gridMode = True
    for line in data:
        if line == '\n':
            gridMode = False
            continue
        line = line.strip()
        if gridMode:
            continue
        else:
            line = line.split()
            amount = int(line[1])
            source = int(line[3])
            target = int(line[5])
            for x in range(amount):
                elem = stacks[source-1].pop()
                stacks[target-1].append(elem)
    result = ""
    for stack in stacks:
        if len(stack) > 0:
            result += stack[-1]
    print(result)
if __name__ == '__main__':
    main()