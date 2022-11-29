import sys
import numpy as np

data_file = sys.argv[1]



def main():
    total_chars = 0
    good_chars = 0
    data = open(data_file)
    for line in data:
        line = line.strip()
        total_chars += len(line)
        c = 0
        while c != len(line):
            if line[c] == '"':
                c += 1
                continue
            if line[c] == '\\':
                if line[c+1] == '\\' or line[c+1] == '"':
                    good_chars += 1
                    c += 2
                    continue
                elif line[c+1] == 'x':
                    good_chars += 1
                    c += 4
                    continue
            good_chars += 1
            c += 1
    print(total_chars - good_chars)


if __name__ == '__main__':
    main()