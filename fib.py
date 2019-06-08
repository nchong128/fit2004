def fib(n, list):
    if n == 1 or n == 0:
        list[0] = 0
        list[1] = 1
        return list[n]
    else:
        fib(n-1, list)
        list[n] = list[n-1] + list[n-2]
        return list[n]

print(fib(8, [0]*9))