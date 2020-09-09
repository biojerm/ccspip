def fib5(n):
    if n == 0: 
        return n
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


if __name__ == "__main__":
    print(fib5(5))
    print(fib5(50))