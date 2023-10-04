# Write a program to find Fibonacci series up to n

num = input("Please enter the number :")
num = int(num)

def fibo(num):
    series = []
    if num<=0:
        return series
    elif num == 1:
        series.append(0)
        return series
    else:
        series = [0, 1]
        while series[-1] + series[-2] <= num:
            series.append(series[-1] + series[-2])
        return series

fib_series = fibo(num)
print(f"The Fibonacci series up to {num} is: {fib_series}")
   