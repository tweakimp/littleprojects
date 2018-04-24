import cProfile
import os
import sys
from contextlib import contextmanager
from copy import deepcopy
from datetime import timedelta
from timeit import default_timer

import numpy as np


def printmatrix(matrix):
    """Prints a matrix with leading spaces."""
    lengths = [[(len(str(y))) for y in x] for x in transpose(matrix)]
    longest = [max(x) for x in lengths]
    # print(longest)
    for line in matrix:
        for n, entry in enumerate(line):
            # print("\nlongeest", longest[n])
            print(f" " * (longest[n] - len(str(entry))
                          ) + f"{str(entry)}", end=" ")
        print()


def printlist(lst, columns, padding, separator):
    """Prints a list columnwise."""
    # UNDER CONSTRUCTION
    missingentries = columns - len(alist) % columns
    xlist = lst[:]  # copy list!
    for i in range(missingentries):
        xlist.append(":")
    columnwidths = [0 for _ in range(columns)]
    columnlength = len(xlist) // columns
    for i in range(len(xlist)):
        if columnwidths[i // columnlength] < len(xlist[i]) + padding:
            columnwidths[i // columnlength] = len(xlist[i]) + padding
    for i in range(len(xlist)):
        xlist[i] = f"{xlist[i]: <{columnwidths[i // columnlength]}}"
    columnlength = len(xlist) // columns
    for i in range(columnlength):
        for j in range(columns):
            print(xlist[i + (j * columnlength)], end="")
        print("")


def rotateLeft(matrix):
    """Rotate a matrix counterclockwise."""
    return (np.rot90(np.array(matrix))).tolist()


def rotate180(matrix):
    """Rotate a matrix 180 degrees."""
    return (np.rot90(np.array(matrix), k=2)).tolist()


def rotateRight(matrix):
    """Rotate a matrix clockwise."""
    return (np.rot90(np.array(matrix), k=3)).tolist()


def flipVert(matrix):
    """Flip a matrix vertically."""
    return (np.flip(np.array(matrix), 0)).tolist()


def flipHori(matrix):
    """Flip a matrix horizontally."""
    return (np.flip(np.array(matrix), 1)).tolist()


def transpose(matrix):
    """Transpose a matrix."""
    return list(map(list, zip(*matrix)))


def flatten(nested):
    """Flatten an arbitrarily nested list."""
    nested = deepcopy(nested)
    flat = []
    while nested:
        sublist = nested.pop(0)
        if isinstance(sublist, list):
            nested = sublist + nested
        else:
            flat.append(sublist)
    return flat


def profiler(func):
    """Create a run call profile of the decorated function."""
    def wrap(*args, **kwargs):
        profile = cProfile.Profile()
        result = profile.runcall(func, *args, **kwargs)
        profile.print_stats()
        return result

    return wrap


def stopwatch(func):
    """Print runtime of decorated function."""
    def wrap(*args, **kw):

        start = default_timer()
        result = func(*args, **kw)
        delta = timedelta(seconds=(default_timer() - start))
        print(f"Function {func.__name__} finished in {delta}")
        return result
    return wrap


@contextmanager
def noprint():
    """Prevent function from printing."""
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


def tracer(func):
    """Print a trace of the input and output of a function in one line."""
    def traced_func(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(args) is not 0:
            argslist = ", ".join(f"{x}" for x in args)
            if len(kwargs) is not 0:
                argslist = argslist + ", " if len(kwargs) is not 0 else ""
        else:
            argslist = ""
        if len(kwargs) is not 0:
            kwargslist = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
        else:
            kwargslist = ""
        print(
            f"{func.__name__}({argslist}{kwargslist}) = {result}")
        return result
    return traced_func


if __name__ == '__main__':
    from time import sleep

    @stopwatch
    def timetest():
        sleep(1.234)

    timetest()

    @tracer
    def tracetest(*args, **kwargs):
        even_or_odd = 1
        for _ in args:
            even_or_odd *= -1
        for _ in kwargs:
            even_or_odd *= -1
        return True if even_or_odd == 1 else False
    tracetest()
    tracetest(1)
    tracetest(1, "2")
    tracetest(test=3)
    tracetest(test=3, notest="4")
    tracetest(1, "2", test=3, notest="4")
    matrix = [[-1, 2, 3], [10, 3333, 3000], [10, -200, 3000]]
    printmatrix(matrix)
    print(transpose(matrix))
