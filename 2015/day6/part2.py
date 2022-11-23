import numpy as np

N = 1000
lights = np.zeros((N,N))

def toggle(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] += 2

def on(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] += 1

def off(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            lights[x][y] -= 1
            if lights[x][y] < 0:
                lights[x][y] = 0

def main():
    data = open('data1')
    
    for line in data:
        line = line.split()
        if line[0] == 'toggle':
            one = line[1].split(',')
            two = line[3].split(',')
            x1 = int(one[0])
            y1 = int(one[1])
            x2 = int(two[0])
            y2 = int(two[1])
            toggle(x1, y1, x2, y2)
        else:
            one = line[2].split(',')
            two = line[4].split(',')
            x1 = int(one[0])
            y1 = int(one[1])
            x2 = int(two[0])
            y2 = int(two[1])
            if line[1] == 'on':
                on(x1, y1, x2, y2)
            else:
                off(x1, y1, x2, y2)

    print(np.sum(lights))

if __name__ == '__main__':
    main()