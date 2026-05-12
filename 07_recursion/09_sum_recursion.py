def sum(n):

    if n == 0:
        return 1
    return n + sum(n - 1)

res = sum(4)
print(res)


sum(4)
# = 4 * factorial(3)
#
# = 4 * (3 * factorial(2))
#
# = 4 * (3 * (2 * factorial(1)))
#
# = 4 * (3 * (2 * (1 * factorial(0))))
#
# = 4 + (3 + (2 + (1 + 1)))
