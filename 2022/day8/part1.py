
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
    visible = np.zeros((len(forest[0]), len(forest)))
    forest = np.array(forest)
    for x in range(len(forest[0])):
        for y in range(len(forest)):
            if x == 0 or y == 0 or x == len(forest[0])-1 or y == len(forest)-1:
                visible[y][x] = 1
                continue
            left = forest[y][0:x]
            right = forest[y][x+1:]
            up = forest[0:y, x]
            down = forest[y+1:,x]
            directions = [left, right, up, down]
            for dir in directions:
                if np.max(dir) < forest[y, x]:
                    visible[y][x] = 1
                    break
    print(np.sum(visible))

if __name__ == '__main__':
    main()
    