import sys

def main():
    dataFile = sys.argv[1]
    data = open(dataFile)
    total = 0
    for line in data:
        line = line.strip()
        one, two = line.split(',')
        one = one.split('-')
        two = two.split('-')
        one = [int(x) for x in one]
        two = [int(x) for x in two]
        if one[1] < two[0]:
            continue
        if two[1] < one[0]:
            continue
        total += 1
    print(total)

if __name__ == '__main__':
    main()