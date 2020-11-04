#pip install random
import random


#random_number is the function to generate a random number within a range 1 to 20
def random_number():
    num=random.randint(1,21)        #generates the random number
    return num                      #returns the randomly generated num

result=random_number()

guesses=1
for guesses in range(1,4):
    guess = int(input("Guess the number within 1 to 20 :")) #takes the input from user
    if guess==result:
        print("You guessed it right!")
        break
    elif guess>result:
        print(f"your guess is too high,{3-guesses}attempts left")
    else:
        print(f"your guess is too low,{3-guesses}attempts left")

if guesses==3:
    print("Sorry! you failed")



