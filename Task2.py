# Task 2- Create a number guessing game where the program generates a random number and the user guess the number.
# The excercise is to create a guessing game for the user

import random 

generated_number = random.randint(1,100)
print(generated_number)

while True:
    user_guess = int(input("Guess a Number: \n"))
    if user_guess == generated_number:
        #guess += 1
        print("Congratulations! You have guessed the number correctly")
        break
    elif user_guess > generated_number:
        print("Too High! Try again.")
    elif user_guess < generated_number: 
        print("Too Low! Try again.")

