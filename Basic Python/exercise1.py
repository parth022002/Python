#exercise 1: basis arithmetic operation
a = int(input("Enter the first value : "))
b = int(input("Enter the second value  : "))
c = input("Enter the  operator (+, - , * or /) : ")

if  c == "+":
    print(f"a",c,"b =",a+b)
elif c == "-":
    print(f"a",c,"b =",a-b)
elif c == "*":
    print(f"a",c,"b =",a*b)
elif c == "/":
    print(f"a",c,"b =",a/b)
else:
    print("Invalid Operator")
