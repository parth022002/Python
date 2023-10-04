# Write a program to reverse a given number
num=int(input("Please enter the number: "))

def reverse(num):
    rev=0
    while num>0:
        digit=num%10
        rev=(rev*10)+digit
        num=num//10
    return rev

result =reverse(num)
print("The reverse of",num,"is:",result)
