import numpy as np

def main():
    data = open('data1')
    total = 0
    for line in data:
        l, w, h = list(map(int, line.split('x')))
        total += 2*l*w + 2*w*h + 2*h*l
        total += np.min([l*w,w*h, h*l])
    print(total)


if __name__ == '__main__':
    main()