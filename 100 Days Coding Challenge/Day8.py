#Write a program to find roots of a quadratic equation
import math

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

d = b**2 - 4*a*c #d=discriminant

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("The equation has two distinct real roots:")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif d == 0:
    root = -b / (2*a)
    print("The equation has one real root:")
    print("Root:", root)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(d)) / (2*a)
    print("The equation has complex roots:")
    print("Root 1:", real_part, "+", imaginary_part, "i")
    print("Root 2:", real_part, "-", imaginary_part, "i")
