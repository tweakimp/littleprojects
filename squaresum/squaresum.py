import timeit


def choose_one(so_far, nums, squares):
    if not nums:
        return so_far
    else:
        for n in nums:
            if not so_far or so_far[-1] + n in squares:
                n2 = nums[::]
                n2.remove(n)
                ans = choose_one(so_far + [n], n2, squares)
                if ans:
                    return ans


def square_sum(rmin=1, rmax=40):
    squares, i = set(), 1
    while i * i < rmax**2:
        squares.add(i * i)
        i += 1
    return choose_one([], list(range(rmin, rmax + 1)), squares)


if __name__ == '__main__':
    level = 50
    for x in range(15, level + 1):
        print("sum squares up to", x)
        start = timeit.default_timer()
        print(square_sum(1, x))
        stop = timeit.default_timer()
        print(round(stop - start, 4), "seconds", "\n")
