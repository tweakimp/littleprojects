import os
from copy import deepcopy
from datetime import timedelta
from itertools import combinations, permutations
from math import sqrt
from timeit import default_timer

from tools import printmatrix, profiler, stopwatch, transpose

negative4 = [x for x in range(-8, 8)]
complex4 = [(complex(x, y))
            for x in range(1, 5)
            for y in range(1, 5)]
complex3 = [(complex(x, y))
            for x in range(1, 4)
            for y in range(1, 4)]
test4 = [x for x in range(1, 17)]
test3 = [x for x in range(1, 10)]
done4 = [16, 3, 2, 13, 5, 10, 11, 8, 9, 6, 7, 12, 4, 15, 14, 1]
odd3 = [2 * x + 1 for x in range(9)]


def possibilities(numbers, dim, magicnumber):
    combos = [
        list(x) for x in list(combinations(numbers, dim))
        if sum(x) == magicnumber]
    possibilities = [list(permutations(x)) for x in combos]
    possibilities = [
        [list(y) for y in x]
        for x in possibilities]
    possibilities = [item for sublist in possibilities for item in sublist]
    return possibilities


def remainding_possibilities(matrix, possibilities):
    entries = [item for sublist in matrix for item in sublist if item != ""]
    remainders = [x for x in possibilities
                  if set(entries).isdisjoint(x)]
    return remainders


# @stopwatch
def main(numbers):
    dim = int(sqrt(len(numbers)))
    magicnumber = sum(numbers) / dim
    emptyrow = ["" for _ in range(dim)]
    current = [emptyrow for _ in range(dim)]
    groups = possibilities(numbers, dim, magicnumber)
    written = 0

    def placeRow(matrix, groups, row=0):
        godeeper = False
        current = matrix
        for group in groups:
            current[row] = group
            remainders = remainding_possibilities(current, groups)
            if emptyrow in current:
                godeeper = placeRow(current, remainders, row=row + 1)
            else:
                if check(current):
                    # with open('solutions.txt', 'w') as the_file:
                    #     for solution in solutions:
                    #         for line in solution:
                    #             for entry in line:
                    #                 the_file.write(f"{entry: 2}" + " ")
                    #             the_file.write("\n")
                    #         the_file.write("\n")
                    solutions.append(deepcopy(current))
                    # report(solutions)
                    current[row] = emptyrow
                    return False
                else:
                    current[row] = emptyrow
            if godeeper is False:
                current[row] = emptyrow
        return False

    def check(matrix):
        # rows
        # for x in range(dim):
        #     if "" not in matrix[x]:
        #         if sum(matrix[x]) != magicnumber:
        #             return False

        # diagonals
        diag1 = [matrix[x][x] for x in range(dim)]
        if "" not in diag1:
            if sum(diag1) != magicnumber:
                return False

        diag2 = [matrix[x][dim - 1 - x] for x in range(dim)]
        if "" not in diag2:
            if sum(diag2) != magicnumber:
                return False

        # columns
        transposed = transpose(matrix)
        for x in range(dim):
            if "" not in transposed[x]:
                if sum(transposed[x]) != magicnumber:
                    return False

        return True

    solutions = []
    placeRow(current, groups, row=0)
    # report(solutions, finished=True)


def report(solutions, finished=True):
    os.system('cls')
    delta = timedelta(seconds=(default_timer() - start))
    count = len(solutions)
    print(f"Found {count} solutions",
          f"in {delta}.\n",
          f"{round(60*count/delta.total_seconds(),3)} solutions per minute")
    if finished:
        print("FINISHED")
        for solution in solutions:
            printmatrix(solution)
            print("")


if __name__ == "__main__":
    start = default_timer()

    @profiler
    def testor():
        for _ in range(300):
            main(test3)
            main(complex3)
            main(odd3)
    testor()
