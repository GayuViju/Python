#Infinite Loop
    #Read user input
    #if user said yes then generate random integers 
    #if no then print thank you and exit
    #other input need to display invalid
        #terminate from loop
"""


import random

while(True):
    ch=input("Roll the dice?(Y/N)")
    if(ch=="y" or ch=="Y"):
        n=random.randrange(1,6)
        m=random.randrange(1,6)
        print("(",n,",",m,")")
    elif(ch=="n" or ch=="N"):
         print("Thanks for playing")
         break
    else:
        print("Invalid choice!")

"""
#solution of mosh
"""
import random

while(True):
    ch=input("Roll the dice(Y/N)").lower()
    if ch=='y':
        n=random.randint(1,6)
        m=random.randint(1,6)
        print(f"({n},{m})")
    elif(ch=='n'):
        print("Thanks for Playing")
        break
    else:
        print("Invalid choice!")

"""