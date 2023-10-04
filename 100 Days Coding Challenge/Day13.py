# Write a program to find Sum of N natural numbers

num = input("Enter a positive integer: ")
num = int(num)

def sum_number(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

result = sum_number(num)
print("The sum of the first",num,"natural numbers is:",result)


