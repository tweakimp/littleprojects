size = 4
n = range(size)
candidates = list(reversed([x for x in range(1, size * size + 1)]))
magicnumber = int((size ** 3 + size) / 2)
zeromatrix = [[0 for x in n] for y in n]


def printmatrix(current):
    for i in n:
        for j in n:
            if current[i][j] < 10 and size > 3:
                print("0", end="")
                print(current[i][j], end=" ")
            else:
                print(current[i][j], end=" ")
        print("")


def checkstatus(current):
    valid = True
    if not valid:
        return valid
    else:
        for i in n:
            row = 0
            for j in n:
                row += current[i][j]
            if row > magicnumber:
                valid = False
    if not valid:
        return valid
    else:
        for i in n:
            column = 0
            for j in n:
                column += current[j][i]
            if column > magicnumber:
                valid = False
    if not valid:
        return valid
    else:
        diagonalTL = 0
        for i in n:
            diagonalTL += current[i][i]
        if diagonalTL > magicnumber:
            valid = False
    if not valid:
        return valid
    else:
        diagonalBL = 0
        for i in n:
            diagonalBL += current[size - i - 1][i]
        if diagonalBL > magicnumber:
            valid = False
    return valid


def checksuccess(current):
    valid = True
    if not valid:
        return valid
    else:
        for i in n:
            row = 0
            for j in n:
                row += current[i][j]
            if row != magicnumber:
                valid = False
    if not valid:
        return valid
    else:
        for i in n:
            column = 0
            for j in n:
                column += current[j][i]
            if column != magicnumber:
                valid = False
    if not valid:
        return valid
    else:
        diagonalTL = 0
        for i in n:
            diagonalTL += current[i][i]
        if diagonalTL != magicnumber:
            valid = False
    if not valid:
        return valid
    else:
        diagonalBL = 0
        for i in n:
            diagonalBL += current[size - i - 1][i]
        if diagonalBL != magicnumber:
            valid = False
    return valid


def zerolist(current):
    zerolist = []
    for i in n:
        for j in n:
            if current[i][j] == 0:
                zerolist.append((i, j))
    return zerolist


def placeEntry(number=0, matrix=zeromatrix):
    entry = candidates[number % (size ** 2)]
    current = matrix
    godeeper = False
    placeEntry.counter += 1
    for (i, j) in zerolist(matrix):
        current[i][j] = entry
        if checkstatus(current):
            if checksuccess(current):
                placeEntry.SUCCESS += 1
                print("SUCCESS!")
                printmatrix(current)
                print(placeEntry.counter, "function calls")
                print(placeEntry.SUCCESS, "squares found")
                print("========")
                # raise SystemExit  # get only one matrix
                return False
            godeeper = placeEntry(number + 1, current)
        else:
            current[i][j] = 0
        if godeeper is False:
            current[i][j] = 0
    return False


placeEntry.SUCCESS = 0
placeEntry.counter = 0

placeEntry()
print(placeEntry.counter, "function calls")
print(placeEntry.SUCCESS, "squares found")
