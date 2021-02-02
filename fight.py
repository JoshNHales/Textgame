import time
import random
def fight() :
    print("\n So you've chosen to fight. Opponent entering arena....")
    time.sleep(2)
    print("'Weighing in at 400 lbs, THE BASEMENT DWELLER")
    time.sleep(2)
    print("Big guy, but nothing a true grandmaster cannot handle.")
    print("\u0332".join('\nWhat style will you use?'))
    style = input(""" A - Slippery Salmon Style. "
    \n B - Dancing Crane Style.
    \n C - Crouching Monkey Style.
    \n D - Hibernating Bear Style  
     \n(A/B/C/D): """)
    if style.upper() == "A" :
        print("n\ Ah, so you've chosen Slippery Salmon Style.... Is that even a style?")



hp = 100
def health(damage_taken) :
    global hp
    hp -= num
    print(f"You're health is now {hp}.)


    def combat() :
        if style.upper == "A" :
            dodge_you = random.randint(1,2)
            attack = random.randint(1,10)
            damage_given = 0
            damage_taken = random.randint(20,40)
        print("The slippery salmon lacks in speed. You get attacked first.")
            if dodge %2 == 0 :
                print('\nYou dodged the attack.')
            else :
                health()
            if attack %2 == 0 :
                print('You attacked back. Unfortunately the Slippery Salmon is a pure defensive style.')
            else :
                print('You missed your attack.')            
            

        if style.upper == "B" :
            dodge_you = random.randint(1,3)
            attack = random.randint(1,2)
            damage_given = random.randint(10,25)
            damage_taken = random.randint(20,25)

        if style.upper == "C" :
            dodge = random.randint(1,5)
            attack = random.randint(1,3)
            damage_given = random.randint(10,40)
            damage_taken = random.randint(20,40)

        if style.upper == "D" :
            dodge = random.randint(1,10)
            attack = random.randint(1,5)
            damage_given = random.randint(40:50)
            damage_taken = random.randint(10:30)
