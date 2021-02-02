import time
import random

def begin():
    print("""
 ▓█████   ██████  ▄████▄   ▄▄▄       ██▓███  ▓█████    ▄▄▄█████▓ ██░ ██ ▓█████     ▄▄▄▄    ▄▄▄        ██████ ▓█████  ███▄ ▄███▓▓█████  ███▄    █ ▄▄▄█████▓
 ▓█   ▀ ▒██    ▒ ▒██▀ ▀█  ▒████▄    ▓██░  ██▒▓█   ▀    ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█████▄ ▒████▄    ▒██    ▒ ▓█   ▀ ▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒
 ▒███   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██░ ██▓▒▒███      ▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██▒ ▄██▒██  ▀█▄  ░ ▓██▄   ▒███   ▓██    ▓██░▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░
 ▒▓█  ▄   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄    ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██░█▀  ░██▄▄▄▄██   ▒   ██▒▒▓█  ▄ ▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
 ░▒████▒▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██▒ ░  ░░▒████▒     ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▓█  ▀█▓ ▓█   ▓██▒▒██████▒▒░▒████▒▒██▒   ░██▒░▒████▒▒██░   ▓██░  ▒██▒ ░ 
 ░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░     ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░▒▓███▀▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   
  ░ ░  ░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░▒ ░      ░ ░  ░       ░     ▒ ░▒░ ░ ░ ░  ░   ▒░▒   ░   ▒   ▒▒ ░░ ░▒  ░ ░ ░ ░  ░░  ░      ░ ░ ░  ░░ ░░   ░ ▒░    ░    
    ░   ░  ░  ░  ░          ░   ▒   ░░          ░        ░       ░  ░░ ░   ░       ░    ░   ░   ▒   ░  ░  ░     ░   ░      ░      ░      ░   ░ ░   ░      
        ░  ░      ░  ░ ░            ░  ░            ░    ░             ░  ░  ░   ░  ░    ░            ░  ░      ░     ░  ░       ░      ░  ░         ░          
                  ░                                                                      ░                                                             
""")
    time.sleep(4)
    print("You wake up in a basement and look around the room. A door faces you, and there's a window to the left.")
    time.sleep(3)
    print("You search your pockets...")
    time.sleep(3)
    print("Empty.")
    time.sleep(2)
    options = ["Yes", "No"] 
    print(options)
    wanna_play = input("Would you like to play?: ")
    if wanna_play.capitalize() == "Yes" or wanna_play.capitalize() =="Y":
        time.sleep(2)
        print("\nGreat, then let us begin.")
        the_room()
    elif wanna_play.capitalize() == "No" or wanna_play.capitalize() =="N":
        time.sleep(2)
        print("Lost your nerve on the first question? Maybe multiple choice games arent your thing")
    else:
        print("Sorry I didnt catch that, could you give an answer that's provided? 'Kay thanks :)")
        begin()
def the_room():
    time.sleep(1)
    print("You try to remember how you got here, maybe.... too much booze?")
    time.sleep(3)
    print("Could it be YET ANOTHER prank from the gang of mates you hang with?")
    time.sleep(4)
    print("Seems a bit extreme even for them... oh well, best get to sleuthing.")
    time.sleep(2)
    what_to_do = ["Go to the door", "Go to the window"]
    print(what_to_do)
    decisions = input("What shall you do?: ")
    if decisions.capitalize() == "Go to the door" or decisions.capitalize() =="Door":
        print("\nYou approach the door.")
        time.sleep(2)
        on_the_way()
    elif decisions.capitalize() == "Go to the window" or decisions.capitalize() =="Window":
        print("\nYou approach the window.")  
        time.sleep(2)  
        on_the_way()
    else:
        print("\nCome on take this seriously, you're stuck in someone's basement afterall :P")
        the_room()
def on_the_way():
    print("Heading over you notice something... a hazy curtain maybe?..")
    time.sleep(3)
    print("You soon realise it's... spider webs! 'EWWWW gross' ")
    time.sleep(4)
    print("""
     \_______/
 `.,-'\_____/`-.,'
  /`..'\ _ /`.,' |
 /  /`.,' `.,'\   |
/__/__/     \__\__ |__
\  \  \     /  /  /
 \  \,'`._,'`./  /
  \,'`./___\,'`./
 ,'`-./_____\,-'`.
     /       |
    """)
    print("Only 1 action to take I guess, Rip 'em Up! Or you know, whatever... you do you.")
    time.sleep(2)
    gross = ["Flail", "Shudder", "Scream"]
    print(gross)
    spider_web = 1
    hp = 100
    eww = input("How will you handle this?: ")
    while hp > 0 and spider_web > 0:
        print("your health is", hp)
        if eww.capitalize() == "Flail":
            print("The spider webs health is ", spider_web)
            print("In an adrenaline filled panic, you swing your arms like your trying to shoo away a fly.")
            damage = random.randint(1, 3)
            print(str('The damage you do to the spider web is: '),  damage)
            spider_web = spider_web - damage 
            print("The cobweb strength is now", spider_web)
        elif eww.capitalize() == "Shudder":
            print("The spider web health is ", spider_web)
            print("Officially grossed out, you cringe and shudder damaging the spider web.")
            damage = random.randint(1, 2)
            print(str('The damage you do to the spider web is: '),  damage)
            spider_web = spider_web - damage 
            print("The cobweb strength is now", spider_web)
        elif eww.capitalize() ==  "Scream":
            print("The spider web health is ", spider_web)
            print("You scream as the web envelops you and some goes into your mouth.")
            time.sleep(3)
            print("Your gag reflex kicks in and well... grim.")
            time.sleep(3)
            damage = random.randint(8, 20)
            print(str('The meal you had yesterday tears through the web like a fire hose through a paper sheet: '),  damage)
            spider_web = spider_web - damage 
            print("The cobweb strength is now", spider_web)
        else:
            print("Fine...fine let's reset")
            the_room()
        first_task()    
def first_task():
    print("\nShaken after the spider webs ordeal, you take a moment to compose yourself.")
    time.sleep(4)
    print("... don't take too long though, you're still in someone's basement remember?")
    time.sleep(4)
    what_to_do = ["Go to the door", "Go to the window"]
    print(what_to_do)
    decisions = input("What shall you do?: ")
    if decisions.capitalize() == "Go to the door" or decisions.capitalize() == "Door":
        print("\nYou approach the door")
        door_decision()
    elif decisions.capitalize() == "Go to the window" or decisions.capitalize() == "Window":
        print("\nYou approach the window")    
        window_decision()
    else:
        print("I mean, we can sit an argue all you like, i'm not the one in a random basement >:)")
        first_task()
def door_decision():
    time.sleep(5)
    print("Now, this is some door in a basement you're randomly in so... barging in isnt going to be the smartest choice.\n")
    options2 = ["Look through the keyhole" , "Go to the window"]
    print(options2)
    decide = input("What will you do?: ")
    if decide.capitalize() == "Look through the keyhole" or decide.capitalize() == "Keyhole":
        keyhole()
    elif decide.capitalize() == "Go to the window" or decide.capitalize() == "Window":
        print("\nThe door intimidates you and you decide to take your chances with the window.")
        window_decision()
    else:
        print("\nTake all the time you like to type the options... no rush :)")
        door_decision()
def window_decision():
    time.sleep(5)
    print("You go up to the window to peak through and spot some guards, wonderful.\n")
    options3 = ["Jump out", "Sneak out", "Call for help"]
    print(options3)
    the_window = input("what shall you do?: ")
    if the_window.capitalize() == "Jump out":
        print("\nlike an action hero, you leap out from the building like a badass and...")
        time.sleep(3)
        print("Break your legs. :) smart move")
        window_decision()
    elif the_window.capitalize() == "Sneak out":
        print("\nYou sneakily manage to stealth your way out the room, you ninja.")
        guards()
    elif the_window.capitalize() == "Call for help" :
        print("\nThe guards hear screaming, noticing oh... its you... now alerted they are charging toward your location.\n")
        what_next()
    else:
        print("\nThe options are here to help you, i think, but it helps to type them exactly as they are ;)")
        window_decision()
def what_next():
    time.sleep(5)
    options4 = ["Lock the window", "Head to the door"]
    print(options4)
    print("\nWith few moments to react, the best course of action would be to get moving you reckon.\n")
    get_moving =input("What will you do?: ")
    if get_moving.capitalize() == "Lock the window" or get_moving.capitalize() == "Window" or get_moving.capitalize() == "Lock" :
        print("\nYou lock the window in record perfect time. That has bought you a few moments. You approach the door..")
        dore_problems()
    elif get_moving.capitalize() == "Head to the door" or get_moving.capitalize() == "Door":
        print("\nYou head to the door as footsteps approach your position.")
        dore_problems()
    else:
        print("\nHuh? sorry i can't understand you. Please type what is provided.")
        what_next()
def dore_problems():
    time.sleep(5)
    print("Time ticking down for you now")
    options5 = ["Hide", "Look through the keyhole"]
    print(options5)
    dilemma = input("What will you do?: ")
    if dilemma.capitalize() == "Hide":
        print("\nLike the badass you are, you decide to hide. However you are caught and killed by the guards.")
        time.sleep(2)
        play_again = input("Would you like to play again? [Y/N} :")
        if play_again.upper() == "Y" or "Yes" :
            begin()
        else:
            print('Tough.')
            time.sleep(1)
            begin()

    elif dilemma.capitalize() == "Look through the keyhole" or dilemma.capitalize() ==  "Look" or dilemma.capitalize() ==  "Keyhole":
        keyhole() 



def keyhole() :
    print("\nYou bend down and peer through the keyhole, taken aback by what exactly you're seeing...")
    time.sleep(2) 
    print("A Chinese buffet, untouched and fit for a king.... but who would leave such a spread?\n")
    time.sleep(3)
    print("\u0332".join('What will you do?'))
    enter_or_not = input(""" A - I'm starving! Barge through the door and beeline straight for the tasty looking food.
    \n B - Looks suspicious to me! Open the door and examine the room carefully.
    \n C - YUK, Chinese food makes me sick. Ignore this abomination and go examine the window \n(A/B/C): """ )
    if enter_or_not.upper() == "A" :
        print("\nBANG, you slam the door open and rush towards the buffet.")
        time.sleep(1)
        print("Although you were raised well, this is no time for manners.")
        time.sleep(1)
        print("You start shovelling in as much food as you can, only chewing when necessary.")
        time.sleep(2)
        print("You start to feel faint....")
        time.sleep(3)
        poisoned()
    elif enter_or_not.upper() == "B" :
        print("\nYou open the door slowly, looking out for traps or anything else suspicious...")
        time.sleep(2)
        print("All clear")
        time.sleep(1)
        carefully()
    elif enter_or_not.upper() == "C" :
        window_decision()
    else :
        print('\nWiseguy ey, back to the keyhole for you.')
        keyhole()

def poisoned() :
    print("\nRegreting the meal yet? You should be, it was poisoned. Fool.")
    time.sleep(2)
    print("You died - Cause of death : Poisoning")
    play_again = input("Would you like to play again? [Y/N} :")
    if play_again.upper() == "Y" or "Yes" :
        begin()
    else:
        print('Tough.')
        time.sleep(1)
        begin()

def carefully() :
    print("Proceeding with caution, you enter the room..")
    time.sleep(1)
    print("You're hit with a strange smell, and strange as it is, it's one that you recognise.")
    time.sleep(1)
    print("You're not quite sure why you know it, but you're certain that you do....")
    time.sleep(2)
    print("\nPoison. It must be the buffet...")
    time.sleep(2)
    print("\u0332".join('\nWhat will you do?'))
    buffet_poisoned = input(""" A - I'll take my chances, it would be a crime to leave all this food to go to waste! I'll be fine.
    \n B - Flip the table in anger! Who ruins such a spread!
    \n C - Put some of the food in your pocket, it might be useful later. \n(A/B/C): """ )
    if buffet_poisoned.upper() == "A" :
        print("\nReally? I'm impressed at your stupidity.")
        poisoned()
    elif buffet_poisoned.upper() == "B" :
        print("\nYou flip the table, food flys everywhere and you momentarily feel like you own the place.")
        time.sleep(2)
        print("You notice a switch on the underside of the table, you flick it....")
        time.sleep(2)
        print("\nA secret door opens in the wall. You proceed through it.")
        panic_room()


    elif buffet_poisoned.upper() == "C" :
        print("\nYou stash some food away in your pocket.")
        time.sleep(1)
        print('\nA secret door slams open, you hear footsteps approaching.')
        time.sleep(3)
        fight_or_flight()
    else :
        print('\nJust play the game. Resetting room...')
        carefully()

def fight_or_flight() :
    print("The footsteps are getting louder and louder..")
    time.sleep(2)
    print("\u0332".join('\nWhat will you do?'))
    fight_flight = input(""" A - The approaching person has you SHOOK. You're no fighter after all. Hide. "
    \n B - Years of your Kung-Fu fandom will decide this encounter. Nobody stands a chance against the Crouching Monkey.
    \n C - Baseball is your passion. Wind up a pitch and try to throw the posioned food right into his kisser. \n(A/B/C): """)
    if fight_flight.upper() == "A" :
        print("You're a scaredy cat, and rightfully so. You hide under the table. ")
        time.sleep(2)
        print("A large figure enters the room, you can only see his feet from your position, but oh boy are they big.")
        time.sleep(2)
        print("The footsteps get closer...")
        time.sleep(2)
        print("And closer...")
        time.sleep(2)
        print("Until the figure is right beside you. You shut your eyes, waiting for him to look under the table and find you.")
        time.sleep(3)
        print("CRRRRRUUUUNNCCCCHHHHHH..... Could you be mistaken? Or did the figure really just eat from the posioned buffet?...")
        time.sleep(4)
        print("The man drops dead. Well that was easy!") 
        time.sleep(3)
        print("You proceed through the secret door.")
        panic_room()

    elif fight_flight.upper() == "B" :
        time.sleep(2)
        fight()

    elif fight_flight.upper() == "C" :
        print("\nAt the instant the man enters the room, you throw a nasty curveball....")
        time.sleep(3)
        print("HOMERUN BABY! You're taken aback by what you just achieved. You haven't seen a pitch like that since Babe Ruth.")
        time.sleep(2)
        print("\nStill standing and admiring your own talent, you notice the dying man is trying to murmur something to you...")
        time.sleep(3)
        print("You bend down to listen to his last breath...")
        time.sleep(2)
        print("'Nice throw son'")
        time.sleep(3)
        print("\nBlushing at the dying man's kind words, you stand again and proceed through the secret door.")
        time.sleep(4)
        print("You walk into the room, and are immeditately greeted by the mischievous grin of a thin dark figure.")
        time.sleep(3)
        print("'Are you my captor?', you ask.")
        time.sleep(3)
        print("Yes, say's the man. Or at least i was until i saw that baseball talent of yours")
        time.sleep(3)
        print("I've decided to cut you a deal... Your freedom, in exchange for a lifetime of service.")
        time.sleep(3)
        print("I want you on our baseball team kiddo. What d'ya say?")
        time.sleep(3)
        print("\u0332".join('\nWill you join his baseball team?'))
        baseball_team=input("[Y/N] :")
        if baseball_team.upper() == "Y" :
            print('Congrats, you escaped the basement!')
            time.sleep(2)
            print('You stick to your word and dedicate your life to baseball')
            time.sleep(3)
            print('You play professionally for 20 years and even win an MVP, along with a few all star selections. Not so bad after all ey.')
            time.sleep(8)
            play_again = input("Would you like to play again? [Y/N} :")
            if play_again.upper() == "Y" or "Yes"  :
                begin()
            else:
                print('Tough.')
                time.sleep(1)
                begin()
            
        elif baseball_team.upper() == "N" :
            print("As naive as your are talented. The man leaves the room, with a look of bitter disappointment.")
            time.sleep(2)
            print("He presses a button on his way out...")
            time.sleep(2)
            print("BEEP")
            time.sleep(1)
            print("BEEP")
            time.sleep(1)
            print("BEEP")
            time.sleep(1)
            print("BOOOOOOOM. The entire basement explodes. GAME OVER")
            play_again = input("Would you like to play again? [Y/N} :")
            if play_again.upper() == "Y" or "Yes" :
                begin()
            else:
                print('Tough.')
                time.sleep(1)
                begin()
        else :
                print('\nIt was a simple question... Back you go!')
                fight_or_flight()
            


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
            print('Your opponent swings back his right leg, and with all his might, thrusts it towards your head.')
            time.sleep(4)
            print(""" 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@     \\/        \//                                                        @
@     /\`\      /'/\                                             /\         @
@        \ \  / /           ::::: |~~\|\               ;;;;;    {  }        @
@          \/ /             :: -\ `~~\|  \             /- ;;    _{}_        @
@         / /\ \           /`---',.____\   \ _   /~~~~~'___'     ||         @
@        ( /  \ )         |  \\   \,_____\   \)/ /   \//   |     ||         @
@         `    '          |\   \___|_ ___  \  |/\\  // /  /      ||         @
@                         |__\_______|-'''  (\| ______/  /       ||         @
@                         /~~~~~~~~`\        (=`|______/         ||         @
@                        /___________\         `\    ||          ||         @
@                        /    / \    \          | \__ \\         ||         @
@   =|==||====||====.  /    /    \    \         |   |  ||        ||         @
@    =|=||====||==.   |   /       \    )        |   |            `'         @
@_____ /||----||\ ____|   |________|   |________|   |_______________________@
@~~~~~//~~~~~~~~\\~~~~|___|~~~~~~~~|___|~~~~~~~~|   |~~~~~~~~~~~~~~~~~~~~~~~@
@                    __| |          | |__       |___|                       @
@                    `~~~'          `~~~~'       | |                        @
@                                                `~~'                       @
@                                                                        @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")
            time.sleep(5)
            print('\nK.O')
            time.sleep(2)
            print("\nYou were pulverized into dust. GAME OVER.")
            play_again = input("Would you like to play again? [Y/N} :")
            if play_again.upper() == "Y" or "Yes" :
                keyhole()
            else:
                print('Tough.')
                time.sleep(1)
                keyhole() #begin
    if their_hp == 0 :
        print('\nWow, you actually did it. All those kung fu flicks really did pay off.')
        time.sleep(2)
        print('You stand in awe of your mighty Kung-Fu prowess.')
        time.sleep(3)
        print('You go through the secret door')
        panic_room()

def guards():
    time.sleep(3)
    print ("You hide behind the trees and escape from sight of the guards, running towards a moat you noticed earlier.")
    time.sleep(3)
    print ("You can either swim away to hopefully escape faster, or slowly look around the water for more clues, which will inevitably waste more time.")
    time.sleep(3)
    look_or_swim = input("Will you either: A) look around or B) swim?? [A/B]: ")
    if look_or_swim.upper() == "A" :
        moat()
    elif look_or_swim.upper() == "B":
        croc()
    else:
        ("Your input was invalid, try again!")
        guards()
def moat():
    print("You look around and your impeccible senses notice a strange ripple in the water...")
    time.sleep(4)
    print (""" 
               _.‘^^‘.    
    _      _.-’ ((@)) ’.   ./\/\/\/\/\/\,.---.__
 ..‘o’...-'      ~~~    ‘~/\/\/\/\/\/\__.---.   `-._
:                          /\/\/\/\,-’              `-.__   
^VvvvvvvvvvvVvVv                   |                     `-._
  ;^^^^^^^^^^^`      /             `\        /               `-._
   ```````````````‘.`                `\     (                    `‘-._
            .-----‘`   /\              `\    )--.______.______._______`/ 
           (((------‘``  `‘--------‘`(((----’
           """)
    time.sleep(3)
    print ("AAAAAHHHHHH IT’S A CROCODILEEEEE")
    time.sleep(3)
    print ("You panic at the sight of the beast before you and realise that there are only 3 options to choose from.")
    time.sleep(3)
    print ("You can either A) RUN FOR YOUR LIFE, B) Distract the creature whilst you flee or C) Sneak past them quietly.")
    time.sleep(3)
    run_distract_sneak = input ("Will you choose A, B or C? :")
    if run_distract_sneak.upper() == "A":
        print("Someone has way too much confidence in their speed.")
        time.sleep(3)
        print ("The crocodile quickly catches up with you and gobbles you up.")
        time.sleep(3)
        print ("Maybe you should consider hitting the gym more...")
        time.sleep(3)
        print ("GAME OVER")
        play_again = input("Would you like to play again? [Y/N} :")
        if play_again.upper() == "Y" or "Yes"  :
            begin()
        else:
            print('Tough.')
            time.sleep(1)
            begin()
    elif run_distract_sneak.upper() == "B":
        print ("You stumble upon a large branch that just so happens to strongly resemble a crocodile.")
        time.sleep(3)
        print ("Lucky you!")
        time.sleep(3)
        print ("You throw it towards the creature to create a distraction.")
        time.sleep(3)
        print ("He is incredibly confused at the prospect of this flying crocodile hurtling towards him.")
        time.sleep(3)
        print ("This gives you the chance to flee.")
        time.sleep(3)
        print ("As you are running you notice a crack between the towering brick walls that are enclosing you.")
        time.sleep(3)
        print ("Could it be...")
        time.sleep(3)
        print ("A stong push of the wall reveals a door to your freedom.")
        time.sleep(3)
        print ("YOU WIN")
    elif run_distract_sneak.upper() == "C":
        print ("You quietly sneak away  from the beast, making no sudden movements.")
        time.sleep(3)
        print ("You see an oddly decedant door located within the walls that are holding you back from freedom.")
        time.sleep(3)
        print ("It is a metallic gold with a swirling design surrounding the handle.")
        time.sleep(3)
        print (" ‘How odd!’ You think...")
        time.sleep(3)
        print ("Your curiosity gets the better of you so you enter the strange room.")
        time.sleep(3)
        print ("You find a scroll in the very centre of the room and read it out loud...")
        print (""" 
             _______________________
           =(__    ___      __     _)=
             |                     |
             |    You can never    |
             |    know our secret. |
             |                     |
             |    You can’t run    |
             |    from your past.  |
             |                     |
             |                     |
             |                     |
             |__    ___   __    ___|
           =(_______________________)=
           """)
        time.sleep(3)
        print ("The door suddenly slams shut and you feel a strong blow to the head.")
        time.sleep(3)
        print ("You fall to the floor and black out.")
        doors()
    else:
        ("Your input was invalid, try again!")
        moat()
def croc():
    print ("You clearly have too much faith in your own swimming abilities.")
    time.sleep(3)
    print ("Why on earth did you think you could escape from a FULLY GROWN crocodile?")
    time.sleep(3)
    print ("The crocodile snaps you up for his lunch, as you quite rightly deserve.")
    play_again = input("Would you like to play again? [Y/N} :")
    if play_again.upper() == "Y" or "Yes" :
        begin()
    else:
        print('Tough.')
        time.sleep(1)
        begin()
def doors() :
    print ("’Hmmm... Where am I?’")
    time.sleep(3)
    print ("As you start to awaken you take in your surroundings.")
    time.sleep(3)
    print ("You are in a dusty cellar which appears to be underground.")
    time.sleep(3)
    print ("A strong sense of panic starts to set in. Who did this to you?")
    time.sleep(3)
    print ("As you start to calm down you notice 3 doors in front of you, each with a mysterious marking etched on the front of it.")
    time.sleep(3)
    print ("Door 1 has a sun marking, door 2 a moon marking and door 3 a star marking.")
    door_picked = input ("Do you choose either door 1, 2 or 3?: ")
    if  door_picked == "1":
        print ("You picked door number 1...")
        room_1()
    elif door_picked == "2":
        print ("You picked door number 2...")
        room_2()
    elif door_picked == "3":
        print ("You picked door number 3...")
        room_3()
    else:
        print('Try again..')
        doors()
def room_1():
    print ("A sliver of light appears through the doorframe - could it be? As the door opens you see the outside world and run to freedom. YOU WIN")
def room_2():
    print("The room is filled with an abundance of letters and images.")
    time.sleep(3)
    print("Upon looking closer you realise that these letters are written in handwriting very familiar to your own.")
    time.sleep(3)
    print("How peculiar!")
    time.sleep(4)
    print("Horror dawns on you as you come to learn you were part of a top secret organisation.")
    time.sleep(3)
    print("One letter in particular highlights that you have had your memory wiped by them so you don’t reveal any of their secrets.")
    time.sleep(3)
    print("The secret agency speak to you through microphones attached to the wall - they have been watching you the entire time.")
    time.sleep(3)
    print("‘You were never supposed to find out our plans...‘")
    time.sleep(5)
    print (""" . . .                         
              \|/                          
            `--+--’                        
              /|\                          
             ’ | '                         
               |                           
               |                           
           ,--‘#`--.                       
           |#######|                       
        _.-‘#######`-._                    
     ,-‘###############`-.                 
   ,‘#####################`,               
  /#########################\              
 |###########################|             
|#############################|            
|#############################|            
|#############################|            
|#############################|            
 |###########################|             
  \#########################/              
   `.#####################,'               
     `._###############_,'                 
        `--..#####..--'
        """)
    time.sleep(3)
    print("The room is blown up to destroy all evidence, including you. GAME OVER")
    play_again = input("Would you like to play again? [Y/N} :")
    if play_again.upper() == "Y" or "Yes"  :
        begin()
    else:
        print('Tough.')
        time.sleep(1)
        begin()
def room_3():
    print ("NO! IT CAN’T BE!")
    time.sleep(3)
    print ("A strong sense of dread takes over your entire body.")
    time.sleep(3)
    print ("It dawns on you that you are back where you started in the basement where you first awoke.")
    time.sleep(3)
    print ("Maybe if you put a little thought into your decisions you might have actually made some progress...")
    time.sleep(3)
    print ("But I’m just a voice inside your head, who am I to judge?")

    
def panic_room():
    time.sleep(3)
    print("You enter another(!) room with a single overhead light and dark wall.")
    time.sleep(3)
    print('A small rat cycles past on a tricycle. Pretty grim. Very weird.')
    time.sleep(3)
    print('You notice a red button on the right and a note pinned to the left wall.')
    time.sleep(3)
    print('What could go wrong?')
    time.sleep(3)
    print('*CLANK* *GEARS GRINDING*')
    time.sleep(3)
    print('As soon as you stepped forward into the room the walls started to close in.')
    time.sleep(3)
    print('This decision will have to be quick...')
    time.sleep(3)
    response = input("What's your choice? [button/note]: ")
    if response.lower() == "button" or response.upper() == "BUTTON":
        print("You absolute lunatic. You're dead and to be honest, you deserve it")
        begin()
    elif response.lower() == "note" or response.upper() == "NOTE":
        time.sleep(1)
        print("\nThe note reads..." )
        time.sleep(3)
        print (""" ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄      ▄▀▀▄ █  ▄▀▀▄ ▀▄  ▄▀▀▀▀▄   ▄▀▀▄    ▄▀▀▄                                           
█   █    ▐  █ ▐  ▄▀   ▐     █  █ ▄▀ █  █ █ █ █      █ █   █    ▐  █                                           
▐  █        █   █▄▄▄▄▄      ▐  █▀▄  ▐  █  ▀█ █      █ ▐  █        █                                           
  █   ▄    █    █    ▌        █   █   █   █  ▀▄    ▄▀   █   ▄    █                                            
   ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄       ▄▀   █  ▄▀   █     ▀▀▀▀      ▀▄▀ ▀▄ ▄▀                                            
         ▀     █    ▐       █    ▐  █    ▐                     ▀                                              
               ▐            ▐       ▐                                                                         
 ▄▀▀▄    ▄▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀█▄   ▄▀▀▀█▀▀▄      ▄▀▀▄ ▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄      ▄▀▀█▄▄   ▄▀▀█▀▄    ▄▀▀█▄▄    
█   █    ▐  █ █  █   ▄▀ ▐ ▄▀ ▀▄ █    █  ▐     █   ▀▄ ▄▀ █      █ █   █    █     █ ▄▀   █ █   █  █  █ ▄▀   █   
▐  █        █ ▐  █▄▄▄█    █▄▄▄█ ▐   █         ▐     █   █      █ ▐  █    █      ▐ █    █ ▐   █  ▐  ▐ █    █   
  █   ▄    █     █   █   ▄▀   █    █                █   ▀▄    ▄▀   █    █         █    █     █       █    █   
   ▀▄▀ ▀▄ ▄▀    ▄▀  ▄▀  █   ▄▀   ▄▀               ▄▀      ▀▀▀▀      ▀▄▄▄▄▀       ▄▀▄▄▄▄▀  ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▀ ▄ 
         ▀     █   █    ▐   ▐   █                 █                             █     ▐  █       █ █     ▐    
               ▐   ▐            ▐                 ▐                             ▐        ▐       ▐ ▐          """)
        time.sleep(5)
        print("\nAlso, smart choice. The button would of blown you up.")
        time.sleep(3)
        thou_shall_enter()
    else :
        print('Try again...')
        panic_room()
# prints next step when it should not
# after winning the task you have to decide what's next.

def thou_shall_enter():
    print ("\nWith no time to revel in your minor victory you must choose what to do next. Those spring rolls from earlier have you feeling pretty weird and lying down on the ground seems a nice option. The lil' rat on the tricycle is also intriguing. What would you like to do?""")
    time.sleep(2)
    print ("""  A. Hop on the back of the tricycle and head off into the darkness with lil ratty
  B. You're about to vom. Have a lie down and wait for the walls to slowly turn you into recycling
  """)
    choice = input("What will you do? A or B :  ")
    if choice.lower() == "a" or choice.upper() == "A":
        print("Hop on...it's gonna be a bumpy ride!")
        hallway()
    elif choice.lower() == "b" or choice.upper() == "B":
        print("\nEnjoy your nap because...it's forever. GAME OVER.")
        time.sleep(3)
        play_again = input("Would you like to play again? [Y/N} :")
        if play_again.upper() == "Y" or "Yes"  :
            begin()
        else:
            print('Tough.')
            time.sleep(1)
            begin()
    else:
        print('Try again...')
        thou_shall_enter()
        
# set off down the hallway for the next choice...window to crocodiles, trap door to game over, door to fight with goblin???
def hallway() :
    print("You hop on the back of the tricyle and head down a dark hallway.")
    time.sleep(3)
    print("There's a glimmer of light coming through a window to the left(A) and a door straight ahead(B).")
    time.sleep(2)
    print("As you jump off your ride you land on what seems to be a hatch on the floor(C).")
    time.sleep(3)
    print('Which route will you take?"')
    time.sleep(3)
    door_picked = input ("What will it be? A, B or C? : ")
    if door_picked.upper() == "A":
        print ("\nYou picked door A... You will have to fight. Prepare yourself.")
        fight()
    elif door_picked.upper() == "B":
        print ("\nYou picked door B...")
        room_22()
    elif door_picked.upper() == "C":
        print ("\nYou picked door C...")
        room_3()
    else: 
        print('Try again...')
        hallway()
    # CODE GOOD AS OF 12:21PM
def room_A():
    print ("The note in the last room warned me about this...whatever is in there...it can't be good")

def room_22() :

    print("'What could go wrong?' You climb up and peer out the window...you can only see a grey sky")
    time.sleep(3)
    print("Oh, I must be in Manchester... you think to yourself...")
    time.sleep(3)
    print("You pry open the window and pull yourself onto what seems to be a rooftop.") 
    time.sleep(3)
    print("You can hear some voices on the ground and wander closer to the edge...")
    time.sleep(3)
    print("Slipping on a loose tile, you scramble to keep your balance but it's too late...")
    time.sleep(3)
    print("efore you know what's going on...you've fallen into some kind of moat!.")
    moat()
    
def room_3 ():
    print ("It's that pesky trap door again...GAME OVER") 
    play_again = input("Would you like to play again? [Y/N} :")
    if play_again.upper() == "Y" or "Yes"  :
        begin()
    else:
        print('Tough.')
        time.sleep(1)
        begin()  
#   (  (      )     )      (          )      (   (    
#   )\))(  ( /(    (      ))\    (   /((    ))\  )(   
#  ((_))\  )(_))   )\  ' /((_)   )\ (_))\  /((_)(()\  
#   (()(_)((_)_  _((_)) (_))    ((_)_)((_)(_))   ((_) 
#  / _` | / _` || '  \()/ -_)  / _ \\ V / / -_) | '_| 
#  \__, | \__,_||_|_|_| \___|  \___/ \_/  \___| |_|   
#  |___/                                              """

begin()