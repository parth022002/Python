n = int(input("Enter the Number of row : "))

# increasing triangle
print("1)Increasing Triangle: ")
for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()


# deceasing triangle
print("2)Decreasing Triangle: ")
for i in range(n):
    for j in range(i,n):
        print('*', end='')
    print()

# Right Sided Triangle
print("3)Right Sided Triangle:")
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for j in range (i + 1):
        print ('*',end='')
    print()

# Right Sided decreasing Triangle
print("4)Right Sided decreasing Triangle:")
for i in range(n):
    for j in range(i+1):
        print(' ', end='')
    for j in range(i,n):
        print('*', end='')
    print()

# Hill Pattern
print("5)Hill Pattern:")
for i in range(n):
    for j in range(i,n):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    for j in range(i+1):
        print('*', end='')
    print()

# Reverse Hill Patter
print("6)Reverse Hill Pattern:")
for i in range(n):
    for j in range(i+1):
        print(' ', end='')
    for j in range(i,n):
        print('*', end='')
    for j in range(i,n-1):
        print('*', end='')
    print()

# Diamond Pattern
print("7)Diamond Pattern:")
for i in range(n-1):
    for j in range(i,n):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    for j in range(i+1):
        print('*', end='')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ', end='')
    for j in range(i,n):
        print('*', end='')
    for j in range(i,n-1):
        print('*', end='')
    print()

#Sandglass
print("8)Sandglass Pattern:")
for i in range(n -1):
    for j in range(i+1):
        print(' ', end='')
    for j in range(i,n):
        print('*', end='')
    for j in range(i,n-1):
        print('*', end='')
    print()
for i in range(n):
    for j in range(i,n):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    for j in range(i+1):
        print('*', end='')
    print()
