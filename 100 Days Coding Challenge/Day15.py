# Write a program to identify if the number is Strong number or not
number = int(input("Enter a number: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_strong_number(number):
    original_number = number
    sum_of_factorials = 0
    while number > 0:
        digit = number % 10
        sum_of_factorials += factorial(digit)
        number //= 10
    return sum_of_factorials == original_number

if is_strong_number(number):
    print(number+ "is a strong number.")
else:
    print(number+ "is not a strong number.")
