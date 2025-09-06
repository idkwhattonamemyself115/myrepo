energy=10
turns=0
import random 
while energy>0 and energy<20:
    turns+=1
    action=input("What do you want to do? (move/rest/guess) ")
    if action=="move":
        num=random.randint(1,10)
        if num<=5:
            energy-=2
            print("You lost 2 energy.")
        elif num<=8:
            print("nothing happened.")
        else:
            energy+=3
            print("You gained 3 energy.")
    elif action=="rest":
        energy+=2
        print(f"You rested. Energy is now {energy}.")
    elif action=="guess":
        guess=int(input("Guess a number between 1 and 5: "))
        num=random.randint(1,5)
        if guess==num:
            energy+=5
            print("You guessed right! You gained 5 energy.")
        else:
            energy-=2
            print(f"Wrong! The correct number was {num}. You lost 2 energy.")
    else:
        energy-=1
        print("Invalid action. Please choose move, rest, or guess.")
    print(f"Energy is now {energy}.")
if energy>=20:
    print("Congratulations! You escaped the maze and won the game!")
elif energy<=0:
    print("You ran out of energy and lost the game.")
