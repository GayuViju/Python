
import random

#Generate randominteger
rand_int=random.randint(1,100)
#Loop
while(True):
#Read input as Guessing number
    try:
        guess_no=int(input("Guess the number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid number" )
    #check whether guess is correct or not 
    if  guess_no >100:
            print("Please enter a valid number" )
#Else give clues
    elif guess_no<rand_int:
            print("Too low!")
    elif guess_no>rand_int:
            print("Too high!")
    else:
             print("Congratualations! You guessed the number")
#Get the number so break
             break

