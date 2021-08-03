def Fibonacci(amount):
    fibonacci = [0, 1]

    i = 0
    while i < amount:
        sum = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(sum)
        i += 1

    return fibonacci
