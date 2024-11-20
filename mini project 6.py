def fibonacci(limit):
    fibo_series = [0,1]

    while fibo_series[-1] + fibo_series[-2]<=limit:
        nextfibo = fibo_series[-1] + fibo_series[-2]
        fibo_series.append(nextfibo)

    return fibo_series

fibonacci_reasult = fibonacci(50)
print("fibonacci series up to 50.")
print(fibonacci_reasult)
