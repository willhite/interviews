
def fib3_rec(n):
    if n < 4:  # O(1)
        return 1
    return fib3_rec(n - 1) + fib3_rec(n - 2) + fib3_rec(n - 3)  # O(n)


def fib3_arr(n):
    if n < 4:
        return [1, 1, 1]
    res = fib3_arr(n - 1)
    return[sum(res), res[0], res[1]]


def fib3(n):
    if n < 4:
        return 1
    
    (v1, v2, v3) = (1, 1, 1)
    res = 0
    for i in range(4, n + 1):
        res = v1 + v2 + v3
        v1 = v2
        v2 = v3
        v3 = res
    return res


for n in range(1, 20):
    print("fib3_rec(", n, "):", fib3_rec(n))
    print("fib3_sim(", n, "):", fib3(n))
    print("fib3_arr(", n, "):", fib3_arr(n)[0])
