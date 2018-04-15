from math import sqrt

import numpy as np

inputs = {"negative5": [x for x in range(-12, 13)],
          "complex5": [(complex(x, y)) for x in range(-2, 3) for y in range(-2, 3)],
          # "complex3": [(complex(x, y)) for x in range(-1, 2) for y in range(-1, 2)],
          "complex3": [(complex(x, y)) for x in range(-1, 2) for y in reversed(range(-1, 2))],
          "test7": [x for x in range(1, 50)],
          "test3": [x for x in range(1, 10)],
          "done3": [4, 9, 2, 3, 5, 7, 8, 1, 6],
          "done4": [16, 3, 2, 13, 5, 10, 11, 8, 9, 6, 7, 12, 4, 15, 14, 1],
          }


def createMS(numbers, notifications=False):
    numbers = list(numbers)
    # print(f"numbers ({len(numbers)})\n", numbers)
    # raise SystemExit
    dim = int(sqrt(len(numbers)))
    magicnumber = sum([np.real(x) for x in numbers]) // dim

    matrix = np.matrix([[0 + 0j for x in range(dim)] for y in range(dim)]) if isinstance(
        numbers[0], complex) else np.matrix([[0 for x in range(dim)]for y in range(dim)])

    # fill
    filler = 0
    for x in range(dim):
        for y in range(dim):

            matrix[x, y] = numbers[filler]
            filler += 1

    if notifications:
        print(f"numbers ({len(numbers)})\n", numbers)
        print("dim\n", dim)
        print("magicnumber\n", magicnumber)
        print("matrix\n", matrix)
    for x in range(dim):
        if np.sum(matrix[x:x + 1]) == magicnumber:
            # row good
            print(f"row {x} good")
            pass
        else:
            # row bad
            print(f"row {x} bad")
            pass
        if np.sum((matrix.transpose())[x:x + 1]) == magicnumber:
            # column good
            print(f"column {x} good")
            pass
        else:
            # column bad
            print(f"column {x} bad")
            pass


createMS(inputs["complex3"], notifications=True)
