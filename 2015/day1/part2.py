import numpy as np

def main():
    data = open('data1')
    floor = 0
    position = 0
    for line in data:
        for c in line:
            if c == '(':
                floor += 1
            else:
                floor -= 1
            position += 1
            if floor == -1:
                print(position)
                return

    
if __name__ == '__main__':
    main()