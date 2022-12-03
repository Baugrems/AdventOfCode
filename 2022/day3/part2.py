import sys


def main():
    dataFile = sys.argv[1]
    data = open(dataFile)
    compartments = dict()
    index = 0
    count = 1
    total = 0
    letters = dict()
    amount = 0
    for line in data:
        line = line.strip()
        if count < 4:
            letters[count] = []
            amount = len(line)
            for x in range(amount):
                letters[count].append(line[x]) 
            count += 1
        else:
            count = 1
            for c in letters[1]:
                if c in letters[2] and c in letters[3]:
                    compartments[index] = c
            letters = {}
            index += 1
            letters[count] = []
            amount = len(line)
            for x in range(amount):
                letters[count].append(line[x]) 
            count += 1
    for c in letters[1]:
                if c in letters[2] and c in letters[3]:
                    compartments[index] = c
    vals = compartments.values()
    for v in vals:
        if ord(v) - 97 < 0:
            total += ord(v) - 65 + 27
        else:
            total += ord(v) - 96
    print(total)
            


if __name__ == '__main__':
    main()