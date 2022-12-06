import sys
import numpy as np


def main():
    dataFile = sys.argv[1]
    data = open(dataFile)
    line = data.readline()
    # find fourteen characters in a row in variable line that do not have a repeating character
    # if there are multiple, take the first one
    message = ['']*14
    for c in range(len(line)):
        message = line[c:c+14]
        # print(len(set(message)),len(message))
        if len(set(message)) == len(message):
            print(c+14)
            break

if __name__ == '__main__':
    main()