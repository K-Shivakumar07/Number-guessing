#Python Number guessing Game
import random as r

lowest_num = 1
highest_num = 100
answer = r.randint(lowest_num,highest_num)
guesses = 0
is_running = True

print("*** Python Number Guessing Game ***")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    user_guess = input("Enter your guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1
        
        if user_guess < lowest_num or user_guess > highest_num:
            print("Your Number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif user_guess < answer:
            print("Too low, try again!")
        elif user_guess > answer:
            print("Too high, try again!")
        else:
            print(f"Congratulations,your answer was {answer} .you have guessed the number in {guesses} guesses!")
            is_running = False
    else:
        print(f"Invalid input. Please enter a number between {lowest_num} and {highest_num}")
        