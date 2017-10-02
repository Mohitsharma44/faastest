def fib(n):
    if n <= 1: return n
    else: return fib(n-1) + fib(n-2)

def handle(st):
    n = int(st)

    output = []
    for i in range(n):
        output.append(str(fib(i)))
    print(', '.join(output))
