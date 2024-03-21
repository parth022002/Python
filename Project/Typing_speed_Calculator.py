import time
import random

def count_errors(actual, typed):
    """
    Count the number of errors between the actual text and the typed text.
    """
    errors = 0
    for i in range(min(len(actual), len(typed))):
        if actual[i] != typed[i]:
            errors += 1
    errors += abs(len(actual) - len(typed))
    return errors

def calculate_typing_speed():
    """
    Calculate typing speed based on user input.
    """
    sample = [
        "In the heart of a bustling city, an old bookstore stood, its sign weathered and barely visible amidst the neon glow. Inside, the scent of aging paper mingled with the aroma of coffee. Rows of shelves filled with books lined the walls, each containing a world waiting to be explored.",
        "A cozy reading nook beckoned visitors with soft cushions and warm lamplight. From classic literature to contemporary fiction, the store held treasures for every taste. Customers browsed the shelves, fingers tracing spines, feeling a sense of wonder. Outside, the city pulsed with life, but within, time stood still.",
        "Here, amidst a thousand stories, people found solace, inspiration, and joy. As they left, bags filled with adventures, they knew they would return to this haven of words and imagination."
    ]
    paragraph = random.choice(sample)
    print(paragraph)
    print()
    print("Type the paragraph shown above.")
    print("Press Enter when you're done.")
    print()

    start_time = time.time()
    typed_text = input("Paragraph: ").strip()
    end_time = time.time()

    # Calculate the elapsed time in seconds
    elapsed_time = end_time - start_time

    # Calculate the number of words in the text
    num_words = len(typed_text.split())

    # Calculate the typing speed in words per minute
    typing_speed = round(num_words / elapsed_time * 60, 2)

    num_errors = count_errors(paragraph, typed_text)

    print("Your typing speed is", typing_speed, "words per minute.")
    print("Number of typing errors:", num_errors)

if __name__ == "__main__":
    while True:
        print("***Typing Speed Calculator***")
        choice = input("Ready for the test? (y/n): ").strip().lower()
        if choice == 'y':
            calculate_typing_speed()
        elif choice == 'n':
            print("Thank you for your time.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


"""
Certainly! This Python script is a Typing Speed Calculator. It allows users to test their typing speed by typing out a randomly chosen paragraph from a predefined set and then calculates their typing speed in words per minute (WPM) along with the number of typing errors.

Let's break down the code:

1. **Imports**:
    - `import time`: This module provides various time-related functions. It's used here to measure the elapsed time during typing.
    - `import random`: This module provides functions for generating random numbers. It's used here to select a random paragraph from a predefined set.

2. **Function Definitions**:
    - `count_errors(actual, typed)`: This function takes two strings as input - the actual text (the randomly chosen paragraph) and the typed text (what the user typed). It counts the number of errors between the two texts by comparing each character. It returns the total number of errors.
    - `calculate_typing_speed()`: This function is the main part of the program. It:
        - Selects a random paragraph from a predefined set.
        - Displays the paragraph to the user.
        - Prompts the user to type the displayed paragraph.
        - Measures the time taken by the user to type the paragraph.
        - Calculates the typing speed (in words per minute) based on the time taken and the number of words typed.
        - Calculates the number of typing errors by calling the `count_errors` function.
        - Displays the typing speed and the number of errors to the user.

3. **Main Program**:
    - The main program runs in an infinite loop (`while True:`).
    - It displays a prompt asking the user if they are ready to start the typing test.
    - If the user enters 'y', the `calculate_typing_speed()` function is called to conduct the typing test.
    - If the user enters 'n', a farewell message is displayed, and the program breaks out of the loop, ending the execution.
    - If the user enters any other input, it prompts the user to enter 'y' or 'n' and repeats the loop until a valid input is received.

Overall, this script provides a simple and interactive way for users to test and improve their typing speed.
"""