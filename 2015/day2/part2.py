import numpy as np

def main():
    data = open('data1')
    total = 0
    for line in data:
        dims = list(map(int, line.split('x')))
        dims.sort()
        dims = dims[:2]
        total += 2*dims[0] + 2*dims[1]
        dims = list(map(int, line.split('x')))
        total += dims[0] * dims[1] * dims[2]
    print(total)

    
if __name__ == '__main__':
    main()