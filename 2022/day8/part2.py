
import sys
import numpy as np

def main():
    dataFile = sys.argv[1]
    data = open(dataFile)
    forest = []
    for line in data:
        line = line.strip()
        row = [int(x) for x in line]
        forest.append(row)
    distances = {}
    forest = np.array(forest)
    for x in range(len(forest[0])):
        for y in range(len(forest)):
            left = forest[y][0:x]
            left = np.flip(left)
            right = forest[y][x+1:]
            up = forest[0:y, x]
            up = np.flip(up)
            down = forest[y+1:,x]
            directions = [left, right, up, down]
            if x == 0:
                continue
            if y == 0:
                continue
            if x == len(forest[0]) - 1:
                continue
            if y == len(forest) - 1:
                continue
            distances[(y, x)] = []
            # print(up)
            for dir in directions:
                for s in range(len(dir)):
                    if dir[s] >= forest[y][x]:
                        distances[(y,x)].append(s+1)
                        break
                    if s == len(dir) - 1:
                        distances[(y,x)].append(s+1)
    max = 0
    for dist in distances.values():
        total = 0
        for d in dist:
            if total == 0:
                total += d
                continue
            total *= d
        if total > max:
            max = total
    print(max)

if __name__ == '__main__':
    main()
    