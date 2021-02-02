import time
def guards():
    print ("You hide behind the trees and escape from sight of the guards, running towards a moat you noticed earlier.")
    time.sleep(2)
    print ("You can either swim away to hopefully escape faster, or slowly look around the water for more clues, which will inevitably waste more time.")
    time.sleep(2)
    look_or_swim = input("Will you either: A) look around or B) swim?")
    if look_or_swim.upper() == "A" :
        moat()
    elif look_or_swim.upper() == "B":
        croc()
    else:
        ("Your input was invalid, try again!")
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
    time.sleep(2)
    print ("AAAAAHHHHHH IT’S A CROCODILEEEEE")
    time.sleep(2)
    print ("You panic at the sight of the beast before you and realise that there are only 3 options to choose from.")
    time.sleep(2)
    print ("You can either A) RUN FOR YOUR LIFE, B) Distract the creature whilst you flee or C) Sneak past them quietly.")
    time.sleep(2)
    run_distract_sneak = input ("Will you choose A, B or C?")
    if run_distract_sneak.upper() == "A":
        print("Someone has way too much confidence in their speed.")
        time.sleep(1)
        print ("The crocodile quickly catches up with you and gobbles you up.")
        time.sleep(1)
        print ("Maybe you should consider hitting the gym more...")
        time.sleep(1)
        print ("GAME OVER")
    elif run_distract_sneak.upper() == "B":
        print ("You stumble upon a large branch that just so happens to strongly resemble a crocodile.")
        time.sleep(2)
        print ("Lucky you!")
        time.sleep(2)
        print ("You throw it towards the creature to create a distraction.")
        time.sleep(2)
        print ("He is incredibly confused at the prospect of this flying crocodile hurtling towards him.")
        time.sleep(2)
        print ("This gives you the chance to flee.")
        time.sleep(2)
        print ("As you are running you notice a crack between the towering brick walls that are enclosing you.")
        time.sleep(2)
        print ("Could it be...")
        time.sleep(2)
        print ("A stong push of the wall reveals a door to your freedom.")
        time.sleep(2)
        print ("YOU WIN")
    elif run_distract_sneak.upper() == "C":
        print ("You quietly sneak away  from the beast, making no sudden movements.")
        time.sleep(2)
        print ("You see an oddly decedant door located within the walls that are holding you back from freedom.")
        time.sleep(2)
        print ("It is a metallic gold with a swirling design surrounding the handle.")
        time.sleep(2)
        print (" ‘How odd!’ You think...")
        time.sleep(2)
        print ("Your curiosity gets the better of you so you enter the stange room.")
        time.sleep(2)
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
        time.sleep(2)
        print ("The door suddenly slams shut and you feel a strong blow to the head.")
        time.sleep(2)
        print ("You fall to the floor and black out.")
        doors()
    else:
        ("Your input was invalid, try again!")
def croc():
    print ("You clearly have too much faith in your own swimming abilities.")
    time.sleep(2)
    print ("Why on earth did you think you could escape from a FULLY GROWN crocodile?")
    time.sleep(2)
    print ("The crocodile snaps you up for his lunch, as you quite rightly deserve.")
def doors() :
    print ("’Hmmm... Where am I?’")
    time.sleep(2)
    print ("As you start to awaken you take in your surroundings.")
    time.sleep(2)
    print ("You are in a dusty cellar which appears to be underground.")
    time.sleep(2)
    print ("A strong sense of panic starts to set in. Who did this to you?")
    time.sleep(2)
    print ("As you start to calm down you notice 3 doors in front of you, each with a mysterious marking etched on the front of it.")
    time.sleep(2)
    print ("Door 1 has a sun marking, door 2 a moon marking and door 3 a star marking.")
    door_picked = input ("Do you choose either door 1, 2 or 3? >")
    if  door_picked == "1":
        print ("You picked door number 1...")
        room_1()
    elif door_picked == "2":
        print ("You picked door number 2...")
        room_2()
    elif door_picked == "3":
        print ("You picked door number 3...")
        room_3()
def room_1():
    print ("A sliver of light appears through the doorframe - could it be? As the door opens you see the outside world and run to freedom. YOU WIN")
def room_2():
    print("The room is filled with an abundance of letters and images.")
    time.sleep(2)
    print("Upon looking closer you realise that these letters are written in handwriting very familiar to your own.")
    time.sleep(2)
    print("How peculiar!")
    time.sleep(4)
    print("Horror dawns on you as you come to learn you were part of a top secret organisation.")
    time.sleep(2)
    print("One letter in particular highlights that you have had your memory wiped by them so you don’t reveal any of their secrets.")
    time.sleep(2)
    print("The secret agency speak to you through microphones attached to the wall - they have been watching you the entire time.")
    time.sleep(2)
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
    time.sleep(2)
    print("The room is blown up to destroy all evidence, including you. GAME OVER")
def room_3():
    print ("NO! IT CAN’T BE!")
    time.sleep(2)
    print ("A strong sense of dread takes over your entire body.")
    time.sleep(2)
    print ("It dawns on you that you are back where you started in the basement where you first awoke.")
    time.sleep(2)
    print ("Maybe if you put a little thought into your decisions you might have actually made some progress...")
    time.sleep(2)
    print ("But I’m just a voice inside your head, who am I to judge?")

guards()