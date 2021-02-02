import time
import random
def fight() :
    print("\nSo you've chosen to fight. Opponent entering arena....")
    time.sleep(2)
    print("Weighing in at 400 lbs, THE BASEMENT DWELLER.")
    time.sleep(2)
    print("Big guy, but nothing a true Kung-Fu master can't handle.")
    time.sleep(3)
    print("\u0332".join('\nWhat style will you use?'))
    global style
    style = input(""" A - Slippery Salmon Style. "
    \n B - Dancing Crane Style.
    \n C - Crouching Monkey Style.
    \n D - Hibernating Bear Style  
     \n(A/B/C/D): """)
    if style.upper() == "A" :
        print("\nAh, so you've chosen Slippery Salmon Style.... Is that even a style?")
        time.sleep(2)
        print("Nows probably a good time to let you know, the slippery salmon is purely a defensive style, and deals no damage. Good luck!")
        time.sleep(3)
        print("The slippery salmon lacks in speed. You get attacked first..")
        combat()
    elif style.upper() == 'B' :
        print("\nSo you've picked the Dancing Crane, I hope you've good balance. Good luck little birdie.")
        time.sleep(2)
        print("The Dancing Crane ALWAYS waits for his opponent to move....")
        combat()
    elif style.upper() == 'C' :
        print("\nThe Crouching Monkey, your 'signature' style. Make your sensei proud.")
        time.sleep(2)
        print("The Monkey remains crouched, ready to pounce after his opponent moves.")
        combat()
    elif style.upper() == "D" :
        print("The Hibernating Bear, risky choice.\nThe bear sleeps and is poor at dodging, but if he wakes, he'll be sure to dish out some pain.")
        time.sleep(4)
        print("The bear stays sleepy, and cannot move first.")
        combat()
    else :
        print('\nTry again..')
        fight()
        





hp = 100
def health(damage_taken) :
    global hp
    hp -= damage_taken
    if hp <0 :
        hp = max(0, 0)
    print(f"They did {damage_taken} damage. Your health is now {hp}.")

their_hp = 100
def their_health(damage_given) :
    global their_hp
    their_hp -= damage_given
    if their_hp <0 :
        their_hp = max(0, 0)
    print(f"You did {damage_given} damage. Their health is now {their_hp}.")


def combat() :
    time.sleep(3)
    while hp > 0 and their_hp > 0 :
        if style.upper() == "A" : 
            dodge = random.randint(1,2)
            attack = random.randint(1,10)
            damage_given = 0
            damage_taken = random.randint(20,40)
        elif style.upper() == "B" :
            dodge = random.randint(1,3)
            attack = random.randint(1,2)
            damage_given = random.randint(10,25)
            damage_taken = random.randint(20,25)
        elif style.upper() == "C" :
            dodge= random.randint(1,5)
            attack = random.randint(0,3)
            damage_given = random.randint(10,40)
            damage_taken = random.randint(20,40)
        elif style.upper() == "D" :
            dodge= random.randint(1,1)
            attack = random.randint(1,5)
            damage_given = random.randint(40,50)
            damage_taken = random.randint(10,30)
        
        print("\nYou get attacked...")
        time.sleep(1)
        if dodge % 2 == 0 :
            print('You dodged the attack.')
            time.sleep(2)
        else :
            health(damage_taken)
        if attack %2 == 0 and hp > 0 and their_hp > 0:
            print('\nYou attack back...')
            time.sleep(1)
            their_health(damage_given)
            time.sleep(2)
        elif attack % 2 != 0 and hp>0 and their_hp > 0 :
            print('\nYou attack back...')
            time.sleep(1)
            print('You missed your attack.') 
            time.sleep(2)
        elif hp == 0  :
            print("You died.")
    if their_hp == 0 :
        print('\nWow, you actually did it. All those kung fu flicks really did pay off.')
        
    
fight()