from copy import deepcopy
from itertools import combinations, permutations
from math import sqrt

from tools import flatten, printmatrix, stopwatch, transpose

inputs = {"negative4": [x for x in range(-8, 8)],
          "complex4": [(complex(x, y))
                       for x in range(1, 5)
                       for y in range(1, 5)],
          "test4": [x for x in range(1, 17)],
          "test3": [x for x in range(1, 10)],
          }


# def getCombinations(numbers):
#     dim = int(sqrt(len(numbers)))
#     magicnumber = sum(numbers) / dim
#     combos = list(combinations(numbers, dim))
#     combos = [x for x in combos if sum(x) == magicnumber]
#     print(dim, magicnumber)
#     return list(combos)


# test = getCombinations(inputs["complex4"])
# for combo in test:
#     print(combo)


# magic square rules
# 2x2 subsquares also sum to magic number
# dist n/2 on a diagonal sum to half of magic number

@stopwatch
def getSquares(numbers):
    # prepare
    dim = int(sqrt(len(numbers)))
    nullmatrix = [["" for x in range(dim)] for y in range(dim)]
    magicnumber = sum(numbers) / dim
    combos = [
        x for x in list(combinations(numbers, dim))
        if sum(x) == magicnumber]
    possibilities = [list(permutations(x)) for x in combos]
    for x in combos:
        print(*x)
    solutions = []
    # for each combo start recursive

    def placeEntry(count=0, matrix=nullmatrix):
        entry = numbers[count]
        current = matrix
        zerolist = [(i, j) for i in range(dim)
                    for j in range(dim) if current[i][j] == ""]
        godeeper = False
        for (i, j) in zerolist:
            current[i][j] = entry
            if "" in flatten(current):
                if check(current):
                    godeeper = placeEntry(count + 1, current)
                else:
                    current[i][j] = ""
            else:
                if check(current):
                    print("FOUND ONE")
                    # for line in current:
                    #     print(*line, sep="\t")
                    # print("\t")
                    # raise SystemExit
                    solutions.append(deepcopy(current))
                    return False
                else:
                    current[i][j] = ""
            if godeeper is False:
                current[i][j] = ""
        return False

    def check(matrix, notifications=False):
        # rows
        for x in range(dim):
            if "" not in matrix[x]:
                if sum(matrix[x]) != magicnumber:
                    print(f"false in row {x}") if notifications else 1
                    return False

        # diagonals
        diag1 = [matrix[x][x] for x in range(dim)]
        if "" not in diag1:
            if sum(diag1) != magicnumber:
                print(f"false in diag1") if notifications else 1
                return False

        diag2 = [matrix[x][dim - 1 - x] for x in range(dim)]
        if "" not in diag2:
            if sum(diag2) != magicnumber:
                print(f"false in diag2") if notifications else 1
                return False

        # columns
        transposed = transpose(matrix)
        for x in range(dim):
            if "" not in transposed[x]:
                print(transposed)
                if sum(transposed[x]) != magicnumber:
                    print(f"false in col {x}") if notifications else 1
                    return False

        return True

    placeEntry()
    for sol in solutions:
        printmatrix(sol)
        print()


getSquares(inputs["test3"])
