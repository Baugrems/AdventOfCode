import sys
import numpy as np
import operator

def RPSresult(A, B):
    if A == 'A':
        if B == 'X':
            return 3
        if B == 'Y':
            return 6
        if B == 'Z':
            return 0
    if A == 'B':
        if B == 'X':
            return 0
        if B == 'Y':
            return 3
        if B == 'Z':
            return 6
    if A == 'C':
        if B == 'X':
            return 6
        if B == 'Y':
            return 0
        if B == 'Z':
            return 3

def main():
    dataFile = sys.argv[1]
    data = open(dataFile)
    choice_points = {'X': 1, 'Y': 2, 'Z': 3}
    result_points = [0, 3, 6]
    score = 0
    for line in data:
        enemy, choice = line.split()
        score += RPSresult(enemy, choice)
        score += choice_points[choice]
    print(score)
        

if __name__ == '__main__':
    main()