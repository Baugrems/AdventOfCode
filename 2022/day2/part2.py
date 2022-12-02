import sys
import numpy as np
import operator

def RPSresult(A, B):
    if A == 'A':
        if B == 'X':
            return 'Z'
        if B == 'Y':
            return 'X'
        if B == 'Z':
            return 'Y'
    if A == 'B':
        if B == 'X':
            return 'X'
        if B == 'Y':
            return 'Y'
        if B == 'Z':
            return 'Z'
    if A == 'C':
        if B == 'X':
            return 'Y'
        if B == 'Y':
            return 'Z'
        if B == 'Z':
            return 'X'

def main():
    dataFile = sys.argv[1]
    data = open(dataFile)
    choice_points = {'X': 1, 'Y': 2, 'Z': 3}
    result_points = {'X':0, 'Y': 3, 'Z': 6}
    score = 0
    for line in data:
        enemy, choice = line.split()
        score += result_points[choice]
        choice = RPSresult(enemy, choice)
        score += choice_points[choice]
    print(score)
        

if __name__ == '__main__':
    main()