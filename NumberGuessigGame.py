import random

min_value = 1
max_value = 10
secret_number = random.randint(min_value, max_value)

print("Welcome to the Number Guessing Game!")
print(f"Try to guess the secret number between {min_value} and {max_value}.")

has_guessed_correctly = False

while not has_guessed_correctly:
    user_guess = int(input("Enter the number you guess: "))

    if user_guess < secret_number:
        print("The number is too low.")
    elif user_guess > secret_number:
        print("The number is too high.")
    else:
        print("You Win!")
        has_guessed_correctly = True
