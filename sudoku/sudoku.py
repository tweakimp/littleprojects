import test

zeromatrix = [[0 for j in range(1, 10)] for i in range(1, 10)]

startcandidates = [[[x for x in range(1, 10)] for j in range(1, 10)]
                   for i in range(1, 10)]


def printmatrix(matrix, start=zeromatrix):
    for i in range(9):
        for j in range(9):
            if (j == 2 or j == 5):
                if (matrix[i][j] == 0):  # TODO ternary experiment
                    print("\x1b[1;90m.\x1b[0m", end=" \x1b[1;90m|\x1b[0m ")
                else:
                    if (start[i][j] == 0):
                        print(
                            f"\x1b[1;91m{matrix[i][j]}\x1b[m",
                            end=" \x1b[1;90m|\x1b[0m ")
                    else:
                        print(matrix[i][j], end=" \x1b[1;90m|\x1b[0m ")
            else:
                if (matrix[i][j] == 0):
                    print("\x1b[1;90m.\x1b[0m", end=" ")
                else:
                    if (start[i][j] == 0):
                        print(f"\x1b[1;91m{matrix[i][j]}\x1b[m", end=" ")
                    else:
                        print(matrix[i][j], end=" ")
        print("")
        if (i == 2 or i == 5):
            print("\x1b[1;90m- - - + - - - + - - -\x1b[0m")


def matrixfromcandidates(candidates):
    matrix = zeromatrix
    for i in range(9):
        for j in range(9):
            if len(candidates[i][j]) == 1:
                matrix[i][j] = candidates[i][j][0]
    return matrix


def zerocounter(current):
    count = 0
    for row in current:
        count += row.count(0)
    return count


def nonzerocounter(current):
    count = 81 - zerocounter(current)
    return count


def solve(start):
    # initialize
    global current, candidates, zerocounter, iterationcount
    current = zeromatrix
    candidates = startcandidates
    for i in range(9):
        for j in range(9):
            if start[i][j] != 0:
                current[i][j] = start[i][j]
                deleteCandidates(i, j)
    print(f"========START========")
    print(f"{nonzerocounter(start)} clues")
    printmatrix(current)
    while (zerocounter(current) > 0):
        zeroesbefore = zerocounter(current)
        iteration(candidates)
        checkCandidates()
        zeroesafter = zerocounter(current)
        if (zeroesbefore == zeroesafter):
            print("=========END=========")
            s = ("" if iteration.count == 1 else "s")
            print(
                f"Couldn't solve! {nonzerocounter(current)-nonzerocounter(start)} found in {iteration.count} iteration{s}"
            )
            printmatrix(current, start)
            raise SystemExit

    else:
        print("=========END=========")
        s = ("" if iteration.count == 1 else "s")
        print(f"Solved in {iteration.count} iteration{s}")
        printmatrix(current, start)


def deleteCandidates(i, j):
    deleteHorizontal(i, j)
    deleteVertical(i, j)
    deleteSubgrid(i, j)


def deleteHorizontal(i, j):
    disqualified = current[i][j]
    for x in range(9):
        if x == j:
            candidates[i][x] = [disqualified]
        else:
            if disqualified in candidates[i][x]:
                candidates[i][x].remove(disqualified)


def deleteVertical(i, j):
    disqualified = current[i][j]
    for x in range(9):
        if x == i:
            candidates[x][j] = [disqualified]
        else:
            if disqualified in candidates[x][j]:
                candidates[x][j].remove(disqualified)


def deleteSubgrid(i, j):
    disqualified = current[i][j]
    # get top left cell
    a = i - (i % 3)
    b = j - (j % 3)
    for x in range(3):
        for y in range(3):
            if a + x == i and b + y == j:
                candidates[i][j] = [disqualified]
            else:
                if disqualified in candidates[a + x][b + y]:
                    candidates[a + x][b + y].remove(disqualified)


def checkCandidates():
    checkRows()
    checkColumns()
    checkSubgrids()


def checkRows():
    for x in range(1, 10):
        for i in range(9):
            count = 0
            for j in range(9):
                if x in candidates[i][j]:
                    count += 1
                    position = [i, j]
            if count == 1:
                candidates[position[0]][position[1]] = [x]
                iteration(candidates)


def checkColumns():
    for x in range(1, 10):
        for j in range(9):
            count = 0
            for i in range(9):
                if x in candidates[i][j]:
                    count += 1
                    position = [i, j]
            if count == 1:
                candidates[position[0]][position[1]] = [x]
                iteration(candidates)


def checkSubgrids():
    for x in range(1, 10):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                count = 0
                for a in range(3):
                    for b in range(3):
                        if x in candidates[i + a][j + b]:
                            count += 1
                            position = [i + a, j + b]
                if count == 1:
                    candidates[position[0]][position[1]] = [x]
                    iteration(candidates)


def iteration(candidates):
    iteration.count += 1
    current = matrixfromcandidates(candidates)
    for i in range(9):
        for j in range(9):
            if current[i][j] != 0:
                deleteCandidates(i, j)


if __name__ == "__main__":
    iteration.count = 0
    # solve(test.sudoku1)  # 32 clues - Solved in 238 iterations
    # solve(test.sudoku2)  # 28 clues - Solved in 153 iterations
    # solve(test.sudoku3)  # 28 clues - Solved in 153 iterations
    # solve(test.sudoku4)  # 26 clues - Solved in 185 iterations
    # solve(test.sudoku5)  # 26 clues - Couldn't solve! 3 found in 175 iterations
    # solve(test.sudoku6)  # 21 clues - Couldn't solve! 0 found in 64 iterations
    # solve(test.sudoku7)  # 17 clues - Couldn't solve! 4 found in 183 iterations
    solve(test.sudoku5)  # 17 clues - Solved in 349 iterations
    pass
