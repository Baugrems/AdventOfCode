import sys
import os


parent_dir = 'C:/Users/copen/AdventOfCode/2022'

def main():
    folder = "day" + sys.argv[1]
    path = os.path.join(parent_dir, folder)
    os.mkdir(path)

    f = open(path + "/part1.py", "w")
    f.write('''
import sys
import numpy as np

def main():
    dataFile = sys.argv[1]
    data = open(dataFile)
    for line in data:
        pass

if __name__ == '__main__':
    main()
    ''')
    f.close()
    f = open(path + "/part2.py", "w")
    f.write('''
import sys
import numpy as np

def main():
    dataFile = sys.argv[1]
    data = open(dataFile)
    for line in data:
        pass

if __name__ == '__main__':
    main()
    ''')
    f.close()

    f = open(path + "/data-ex", 'w')
    f.write("")
    f.close()

    f = open(path + "/data", 'w')
    f.write("")
    f.close()

if __name__ == '__main__':
    main()