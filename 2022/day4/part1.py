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
        if int(two[0]) >= int(one[0]) and int(two[1]) <= int(one[1]):
            total += 1
        elif int(one[0]) >= int(two[0]) and int(one[1]) <= int(two[1]):
            total += 1
    print(total)

if __name__ == '__main__':
    main()