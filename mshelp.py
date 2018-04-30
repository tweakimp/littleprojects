from copy import deepcopy
from itertools import combinations, permutations
from math import sqrt

# Some inputs for main().
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
    '''Returns a list of all theways to reach
    the magic number with the given numbers.'''
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
    '''Returns the remainding possibilities once the matrix has entries.'''
    entries =  {item for sublist in matrix for item in sublist if item != ""}
    remainders = [x for x in possibilities
                  if entries.isdisjoint(x)]
    return remainders


def placeRow(matrix, groups, row=0):
    '''Recursive function that fills the matrix row wise
    and puts magic squares into "solutions" list.'''
    godeeper = False
    # emptyrow = ["" for _ in range(dim)]
    current = matrix
    for group in groups:
        current[row] = group
        remainders = remainding_possibilities(current, groups)
        if emptyrow in current:
            godeeper = placeRow(current, remainders, row=row + 1)
        else:
            if check(current):
                solutions.append(deepcopy(current))
                current[row] = emptyrow
                return False
            else:
                current[row] = emptyrow
        if godeeper is False:
            current[row] = emptyrow
    return False


def check(matrix):
    '''Returns false if current matrix is not or cant be made
    into a magic square.'''
    # rows
    # not needed because we fill row wise
    # for x in range(dim):
    #     if "" not in matrix[x]:
    #         if sum(matrix[x]) != magicnumber:
    #             return False
    # only if we have positive numbers only
    #         else:
    #             if sum(transposed[x]) > magicnumber:
    #                 return False

    # diagonals
    diag1 = [matrix[x][x] for x in range(dim)]
    if "" not in diag1:
        if sum(diag1) != magicnumber:
            return False
    # only if we have positive numbers only
    else:
        if sum(diag1) > magicnumber:
            return False

    diag2 = [matrix[x][dim - 1 - x] for x in range(dim)]
    if "" not in diag2:
        if sum(diag2) != magicnumber:
            return False
    # only if we have positive numbers only
    else:
        if sum(diag2) > magicnumber:
            return False

    # columns
    transposed = transpose(matrix)
    for x in range(dim):
        if "" not in transposed[x]:
            if sum(transposed[x]) != magicnumber:
                return False
        # only if we have positive numbers only
        else:
            if sum(transposed[x]) > magicnumber:
                return False

    return True


def main(numbers):
    global dim, magicnumber, emptyrow, solutions
    dim = int(sqrt(len(numbers)))
    magicnumber = sum(numbers) / dim
    emptyrow = ["" for _ in range(dim)]
    current = [emptyrow for _ in range(dim)]
    groups = possibilities(numbers, dim, magicnumber)

    solutions = []
    placeRow(current, groups, row=0)
    for solution in solutions:
        for line in solution:
            print(line)
        print()


def transpose(matrix):
    """Transpose a matrix."""
    return list(map(list, zip(*matrix)))


if __name__ == "__main__":
    main(test3)
