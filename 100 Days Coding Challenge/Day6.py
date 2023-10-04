#Write a program to find the Quadrants in which coordinates lie
x = input("Enter value of x = ")
x = float(x)
y = input("Enter value of y = ")
y = float(y)

if x>0:
    if y>0:
        print("This points lies in first quadrant.")
    else:
        print("This points lies in four quadrant.") 
elif x<0:
    if y>0:
        print("This points lies in second quadrant.")
    else:
        print("This points lies in third quadrant.") 
else:
    print("The points lie in origin.")