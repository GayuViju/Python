'''
import random
#Normal algm
    #Loop
    #Read input from user
    #computer guess
    #Through a function check who wins
        #from 0to 1/3 is rock then 1/3 to 1/6 paper and rest is scissor
    #ask to continue or not
"""
    More standard algorithm
"""

def get_userchoice():
    while True:
        user_choices=input("Rock,Paper, or Scissor(r/p/s): ").lower()
        if user_choices in['r','p','s']:
           return user_choices
        else:
            print("Invalid choice!!")
    
def wins(choice,comp):
    #Using a dictionary to print emoji's
    #To get emojis win+. in windows and in mac cmd+ctrl+space  
    emojis={'r':'🪨','p':'📃','s':'✂️'}
    print(f"You Choose {emojis[choice] }  and computer choose {emojis[comp]}")
    if choice==comp:
        print("It's a Tie!!!")
    elif(
        (choice=='r' and comp=='p') or 
        (choice=='s' and comp=='r') or 
            (choice=='p' and comp=='s')):
        print("You lose!!!")
    else:
        print("You Win!!!")

while(True):
    user=get_userchoice()
    comp=random.choice(['r','p','s'])
    """ comp_ch=random.randrange(0,1)
    if comp_ch<=(1/3):
        comp="r"
    elif comp_ch<=(1/6):
        comp="p"
    else:
      comp="s"""  
    wins(user,comp)
    play=input("Continu?(y/n): ").lower()
    if play=="n":
        break'''

#Here  in above code
    # if we use program variable like r to rock or p to paper we need to rewrite
#DRY-Dont Repeat Yourself
import random

ROCK='r'
PAPER='p'
SCISSORS='s'
emojis={ROCK:'🪨',PAPER:'📃',SCISSORS:'✂️'}


def get_user_choice():
     while True:
        user_choices=input("Rock,Paper, or Scissor(r/p/s): ").lower()
        if user_choices in[ROCK,PAPER,SCISSORS]:
           return user_choices
        else:
            print("Invalid choice!!")

def wins(choice,comp):
    #Using a dictionary to print emoji's
    #To get emojis win+. in windows and in mac cmd+ctrl+space  
    print(f"You Choose {emojis[choice] }  and computer choose {emojis[comp]}")
    if choice==comp:
        print("It's a Tie!!!")
    elif(
        (choice==ROCK and comp==PAPER) or 
        (choice==SCISSORS and comp==ROCK) or 
            (choice==PAPER and comp==SCISSORS)):
        print("You lose!!!")
    else:
        print("You Win!!!")

while(True):
    user=get_user_choice()
    comp=random.choice(['r','p','s']) 
    wins(user,comp)
    play=input("Continu?(y/n): ").lower()
    if play=="n":
        break
