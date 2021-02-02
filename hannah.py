import time
def guards():
    print ("You hide behind the trees and escape from sight of the guards, running toward a moat you noticed earlier.")
    time.sleep(1)
    print ("You can either swim away to hopefully escape faster, or slowly look around the water for more clues, which will inevitably waste more time.")
    time.sleep(1)
    look_or_swim = input("Will you either: A) look around or B) swim?")
    if look_or_swim.upper() == "A":
        moat()
    elif look_or_swim.upper() == "B":
        croc_attack()
    else:
        ("Your input was invalid, try again!")

def moat():
    print("You look around and your impeccible senses notice a strange ripple in the water...")
    time.sleep(1)
    print ("""
        
               _.'^^'.    
    _      .-' ((@)) '.   ./\/\/\/\/\/\,.---._
 ..'o'...-'      ~~~    '~/\/\/\/\/\/\_.---.   `-.
:                          /\/\/\/\,-'              `-.__  
^VvvvvvvvvvvVvVv                   |                     `-._
  ;^^^^^^^^^^^`      /             `\        /               `-._
  
`````````
'.`                `\     (                    `'-._
            .-----'`   /\              \    )--.______.______._______/ 
           (((------'``  '--------'(((----'
""")
    print ("AAAAAHHHHHH IT'S A CROCODILEEEEE")

def crocodile():
    print ("You panic at the sight of the beast before you and realise that there are only 3 options to choose from.")
    time.sleep(1)
    print ("You can either A) RUN FOR YOUR LIFE, B) Distract the creatures whilst you flee or C) Sneak past them quietly.")
    time.sleep(1)
    run_distract_sneak = input ("Will you choose A, B or C?")
    if run_distract_sneak.upper() == "A":
        print("The crocodiles are too fast for you and gobble you up before you can escape! GAME OVER")
    elif run_distract_sneak.upper() == "B":
        print ("You find a secret doorway which leads to your freedom")
    elif run_distract_sneak.upper() == "C":
        print ("You find an empty room with a note saying 'you can't run from your past...' The door suddenly slams shut and you black out.")
    else:
        ("Your input was invalid, try again!")

def doors() :
    print ("You notice 3 doors in front of you, each with a mysterious marking etched on the front of it. Door 1 has a sun marking, door 2 a moon marking and door 3 a star marking.")
    door_picked = input ("Do you choose either door 1, 2 or 3? >")
    if  door_picked == "1":
        print ("You picked door number 1...")
    elif door_picked == "2":
        print ("You picked door number 2...")
    elif door_picked == "3":
        print ("You picked door number 3...")

def room_1():
    print ("A sliver of light appears through the doorframe - could it be? As the door opens you see the outside world and run to freedom. YOU WIN")

def room_2():
    print("The room is filled with an abundance of letters and images.")
    print("Upon looking closer you realise that these letters are written in handwriting very familiar to your own.")
    print("How peculiar!")
    print("Horror dawns on you as you come to learn you were part of a top secret organisation.")
    print("One letter in particular highlights that you have had your memory wiped by them so you don't reveal any of their secrets.")
    print("The secret agency speak to you through microphones attached to the wall - they have been watching you the entire time.")
    print("'You were never supposed to find out our plans...'")
    print("The room is blown up to destroy all evidence, including you. GAME OVER")

def room_3():
    print ("You are back where you started in the basement where you first awoke.")

guards()