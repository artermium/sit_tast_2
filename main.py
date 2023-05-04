def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print("Hello, World!")
print(fib(10))