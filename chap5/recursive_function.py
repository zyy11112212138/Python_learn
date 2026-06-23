def fac(n):
    if n == 1:
        return 1
    else :
        return n * fac(n - 1)

print(fac(5))       #120

#斐波那契数列
def fib(n):
    if n == 1 or n == 2:
        return 1
    else :
        return fib(n - 1) + fib(n - 2)

print(fib(5))

