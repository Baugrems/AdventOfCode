
import sys
import numpy as np

MAX_SIZE = 100000


def main():
    currentDir = 'root'
    system = {'root': []}
    parents = {'root': None}
    values = {'root': 0}
    dataFile = sys.argv[1]
    data = open(dataFile)
    count = 0
    for line in data:
        count += 1
        # print(count)
        line = line.strip()
        # print(line)
        line = line.split()
        if line[0] == '$':
            if line[1] == 'ls':
                continue
            if line[2] == '/':
                currentDir = 'root'
                continue
            elif line[2] == '..':
                if parents[currentDir] is not None:
                    currentDir = parents[currentDir]
                else:
                    currentDir = 'root'
                continue
            else:
                # print(currentDir, parents[currentDir])
                newcurrentDir = None
                newcurrentDir = currentDir + '/' + line[2]
                if currentDir in system.keys() and newcurrentDir not in system[currentDir]:
                    system[currentDir].append(newcurrentDir)
                else:
                    system[currentDir] = [newcurrentDir]
                parents[newcurrentDir] = currentDir
                if newcurrentDir not in system.keys():
                    system[newcurrentDir] = []
                # print(currentDir, newcurrentDir)
                currentDir = newcurrentDir
                continue
        elif line[0].isdigit():
            if currentDir in values.keys():
                values[currentDir] += int(line[0])
            else:
                values[currentDir] = int(line[0])
        else:
            dir = currentDir + '/' + line[1]
            if dir not in system[currentDir]:
                system[currentDir].append(dir)
            if dir not in system.keys():
                system[dir] = []
            parents[dir] = currentDir
            if dir not in values.keys():
                values[dir] = 0
            # print(dir)
                
    # print(system)
    # print(values)
    # print(parents)

    systemSorted = sorted(system, key=len, reverse=True)
    for key in systemSorted:
        if key in values.keys() and parents[key] is not None:
            values[parents[key]] += values[key]

    total_space = 70000000
    used_space = values['root']
    needed_unused = 30000000
    current_unused = total_space - used_space
    delete_size = needed_unused - current_unused

    min = total_space
    dir = None

    for key in values.keys():
        val = values[key]
        if val < delete_size:
            continue
        if val < min:
            min = val
            dir = key
    print(min)


if __name__ == '__main__':
    main()
    