import sys


def main():
    dataFile = sys.argv[1]
    data = open(dataFile)
    compartments = dict()
    index = 0
    total = 0
    for line in data:
        letters1 = []
        letters2 = []
        amount = int(len(line) / 2)
        for x in range(amount):
            letters1.append(line[x])
        for x in range(amount, len(line)):
            letters2.append(line[x])
        for letter in letters1:
            if letter in letters2:
                compartments[index] = letter
        index += 1
    vals = compartments.values()
    for v in vals:
        if ord(v) - 97 < 0:
            total += ord(v) - 65 + 27
        else:
            total += ord(v) - 96
    print(total)
            


if __name__ == '__main__':
    main()