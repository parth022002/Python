#Write a program to identify of the a number is positive or negative
character = input("Enter a number: ")
character = float(character)

if character > 0:
    print ("Number is positive")
elif character < 0:
    print ("Number is negative")
else:
    print ("Number is Zero")
