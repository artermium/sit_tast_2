def fib(n):
    first, second = 0, 1
    print(first)
    n -= 1
    while n:
        print(second)
        second += first
        first = second - first
        n -= 1


print("Hello, World!")
fib(10)