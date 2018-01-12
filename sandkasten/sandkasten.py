size = 9
limit = 5
box = [[0 for i in range(size)] for j in range(size)]


def clear():
    # time.sleep(0.01)
    # os.system("cls")
    pass


def printSandbox():
    for row in range(size):
        for column in range(size):
            if box[row][column] >= 0:
                positive = " "
            else:
                positive = ""
            if box[row][column] == 0:
                color = "\033[90m"
            elif box[row][column] == 1:
                color = "\033[92m"
            elif box[row][column] == 2:
                color = "\033[93m"
            elif box[row][column] == 3:
                color = "\033[91m"
            elif box[row][column] == 4:
                color = "\033[94m"
            elif box[row][column] < 0:
                color = "\033[30m"
            else:
                color = "\033[97m"
            print(f"{color}{positive}{box[row][column]}\033[0m", end=" ")
        print("")
    print("")


def dropSand(i, j):
    box[i][j] += 1


def digHole(i, j):
    box[i][j] -= 1


def spread():
    spread.counter += 1
    for i in range(size):
        for j in range(size):
            if box[i][j] >= limit:
                value = box[i][j]
                if i + 1 in range(size):
                    box[i + 1][j] += value // 4
                    box[i][j] -= value // 4
                if i - 1 in range(size):
                    box[i - 1][j] += value // 4
                    box[i][j] -= value // 4
                if j + 1 in range(size):
                    box[i][j + 1] += value // 4
                    box[i][j] -= value // 4
                if j - 1 in range(size):
                    box[i][j - 1] += value // 4
                    box[i][j] -= value // 4
    for i in range(size):
        for j in range(size):
            if box[i][j] >= limit:
                spread()


def deepen():
    deepen.counter += 1
    for i in range(size):
        for j in range(size):
            if box[i][j] <= -limit:
                value = -box[i][j]
                if i + 1 in range(size):
                    box[i + 1][j] -= value // 4
                    box[i][j] += value // 4
                if i - 1 in range(size):
                    box[i - 1][j] -= value // 4
                    box[i][j] += value // 4
                if j + 1 in range(size):
                    box[i][j + 1] -= value // 4
                    box[i][j] += value // 4
                if j - 1 in range(size):
                    box[i][j - 1] -= value // 4
                    box[i][j] += value // 4
    for i in range(size):
        for j in range(size):
            if box[i][j] <= -limit:
                deepen()


def amountofsand():
    amount = 0
    for i in range(size):
        for j in range(size):
            amount += box[i][j]
    return amount


def start(s, x1, y1, x2, y2, z1, z2):
    iterations = 0
    noholes = False
    while (noholes is False):
        dropSand(x1, y1)
        dropSand(x2, y2)
        digHole(z1, z2)
        spread()
        deepen()
        noholes = True
        for i in range(size):
            for j in range(size):
                if box[i][j] < 0:
                    noholes = False
                    break
        iterations += 1
        printSandbox()
    print("sandcount", amountofsand(), ", ", iterations)
    print("spread.counter", spread.counter)
    print("deepen.counter", deepen.counter)
    print("iterations", iterations)


if __name__ == "__main__":
    deepen.counter = 0
    spread.counter = 0
    start(size, 0, 0, 1, 0, size - 1, size - 1)
