#Take an input character from the user and check whether the given input is vowel or consonant.
character = input("Enter a character: ")

character = character.lower()

if character.isalpha():
    if character in ['a', 'e', 'i', 'o', 'u']:
        print("The character " +character+ " is vowel.")
    else:
        print("The character " +character+ " is consonant.")
else:
    print("The character " +character+ " is invalid.")
