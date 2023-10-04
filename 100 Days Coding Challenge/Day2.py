#Write a program to identify if the character is an alphabet or not

character = input("Enter a character: ")

character = character.lower()

if character.isalpha():
        print("The character " +character+ " is alphabet.")
else:
    print("The character " +character+ " is not alphabet.")
