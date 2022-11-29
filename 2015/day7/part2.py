import sys
import numpy as np

data_file = sys.argv[1]
target = sys.argv[2]
target2 = sys.argv[3]

data = open(data_file)
num_commands = len(data.readlines())
data.close()

wires = dict()
max_val = 65535

operators = ['AND', 'OR', 'LSHIFT', 'RSHIFT']

def ensure_max(index):
    if wires[index] > max_val:
        wires[index] = max_val

def handle_not(line):
    if line[1] not in wires:
            return False
    if line[3] in wires:
        wires[line[3]] += max_val - wires[line[1]]
    else:
        wires[line[3]] = max_val - wires[line[1]]
    ensure_max(line[3])
    return True

def handle_bitwise(line):
    op = line[1]
    target = line[4]
    if op == 'AND' and not line[0].isdigit():
        if line[0] not in wires or line[2] not in wires:
            return False
        a = wires[line[0]]
        b = wires[line[2]]
        if target in wires:
            wires[target] += a & b
        else:
            wires[target] = a & b
    elif op == 'AND' and line[0].isdigit():
        if line[2] not in wires:
            return False
        a = int(line[0])
        b = wires[line[2]]
        if target in wires:
            wires[target] += a & b
        else:
            wires[target] = a & b
    elif op == 'OR':
        if line[0] not in wires or line[2] not in wires:
            return False
        a = wires[line[0]]
        b = wires[line[2]]
        if target in wires:
            wires[target] += a | b
        else:
            wires[target] = a | b
    elif op == 'RSHIFT':
        if line[0] not in wires:
            return False
        if target in wires:
            wires[target] += wires[line[0]] >> int(line[2])
        else:
            wires[target] =  wires[line[0]] >> int(line[2])
    elif op == 'LSHIFT':
        if line[0] not in wires:
            return False
        if target in wires:
            wires[target] += wires[line[0]] << int(line[2])
        else:
            wires[target] =  wires[line[0]] << int(line[2])
    return True

def handle_signal(line):
    if line[2] in wires:
        wires[line[2]] += int(line[0])
    else:
        wires[line[2]] = int(line[0])
    ensure_max(line[2])
    return True

def handle_signal_source(line):
    if line[0] not in wires:
        return False
    if line[2] in wires:
        wires[line[2]] += wires[line[0]]
    else:
        wires[line[2]] = wires[line[0]]
    ensure_max(line[2])
    return True

    

def part1():
    commands_run = []
    while len(commands_run) < num_commands:
        index = 0
        data = open(data_file)
        for line in data:
            if index in commands_run:
                index += 1
                continue
            line = line.split()
            if line[0] == 'NOT':
                if handle_not(line):
                    commands_run.append(index)
            elif line[1] in operators:
                if handle_bitwise(line):
                    commands_run.append(index)
            elif line[1] == '->' and line[0].isdigit():
                if handle_signal(line):
                    commands_run.append(index)
            elif line[1] == '->':
                if handle_signal_source(line):
                    commands_run.append(index)
            index += 1
        data.close()
        print(len(commands_run))
    return wires[target]

def main():
    solution = part1()
    global wires
    wires = {}
    wires[target2] = solution
    commands_run = []
    while len(commands_run) < num_commands:
        index = 0
        data = open(data_file)
        for line in data:
            if index in commands_run:
                index += 1
                continue
            line = line.split()
            if line[0] == 'NOT':
                if handle_not(line):
                    commands_run.append(index)
            elif line[1] in operators:
                if handle_bitwise(line):
                    commands_run.append(index)
            elif line[1] == '->' and line[0].isdigit():
                if handle_signal(line):
                    commands_run.append(index)
            elif line[1] == '->':
                if handle_signal_source(line):
                    commands_run.append(index)
            index += 1
        data.close()
        print(len(commands_run))
    print(wires[target])
        
    

if __name__ == '__main__':
    main()