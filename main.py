import sys 
from time import sleep
import random
#strength
#intelligence
#magic
#sneak
#charisma

points = 250

print("Welcome, adventurer! Skill point time! You will have 5 skills to spend points on. (250 points available)")

print("Press enter to continue")
preset = input()

if preset == "My preset":
    strength = 75
    intelligence = 75
    magic = 40
    sneak = 30
    charisma = 30

else:
    strength = int(input("How strong are you? (0-100)\n>"))


    if strength > 100 or strength < 0 or strength > points:
        print("You can't do that! You lose.")
        exit()
    points = points - strength
    print("Wow such stronk! STRENGTH SET TO " + str(strength))
    print("You have " + str(points) + " skill points remaining")

    intelligence = int(input("How smart are you? (0-100)\n>"))

    if intelligence > 100 or intelligence < 0 or intelligence > points:
        print("You can't do that! You lose.")
        exit()
    points = points - intelligence
    print("Wow such smart! INTELLIGENCE SET TO " + str(intelligence))
    print("You have " + str(points) + " skill points remaining")

    magic = int(input("What is your magic stat? (0-100)\n>"))

    if magic > 100 or magic < 0 or magic > points:
        print("You can't do that! You lose.")
        exit()
    points = points - magic
    print("Wow such magics! MAGIC SET TO " + str(magic))
    print("You have " + str(points) + " skill points remaining")

    sneak = int(input("What is your sneak? (0-100)\n>"))

    if sneak > 100 or sneak < 0 or sneak > points:
        print("You can't do that! You lose.")
        exit()
    points = points - sneak
    print("Wow such sneak! SNEAK SET TO " + str(sneak))
    print("You have " + str(points) + " skill points remaining")

    charisma = int(input("What is your charisma? (0-100)\n>"))

    if charisma > 100 or charisma < 0 or charisma > points:
        print("You can't do that! You lose.")
        exit()
    points = points - charisma
    print("Wow such charisma! CHARISMA SET TO " + str(charisma))
    print("You have " + str(points) + " skill points remaining")
    if points > 0:
        print("You have points left over... next time try to use all available points.")
        sleep(1)

    sleep(1)

    print("You encounter a menacing wall. Waht do?")

print("1. Punch wall")
print("2. Reason with wall")
print("3. Climb wall")
print("4. Magic wall")

choice = input(">")

if choice == "1":
    roll = random.randrange(0,strength)
    if roll > 20:
        print("The wall crumbles to the blow you deliver")

    else:
        print("Your fist shatters.")
        exit()
elif choice == "2":
    roll = random.randrange(0, charisma)
    if roll >= 50:
        print("By some miracle you reasoned a wall out of the way")

    else:
        print("You stupidly try to reason with the wall. You fail.")
        exit()
elif choice == "3":
    roll = random.randrange(0, strength)
    roll2 = random.randrange(0, intelligence)
    if roll > 30 and roll2 > 30:
        print("You scale the wall.")

    else:
        print("You start to climb the wall but before reaching the top you fall, breaking your neck.")
        exit()
    print()
elif choice == "4":
    roll = random.randrange(0, magic)
    if roll > 30:
        print("You magic the wall out of the way.")
    
    else:
        print("Your magic fails you, leaving the wall in its place.")
        exit()
else:
    print("You can't do that! You lose.")
    exit()


sleep(1)

print("After traveling a good distance, you approach a locked door covered in runes. Waht do?")

print("1. Break down door")
print("2. Search for a key")
print("3. Pick the lock")
print("4. Use magic to open the door")


choice = input(">")

if choice == "1":
    roll = random.randrange(0,strength)
    if roll >= 30:
        print("You rip the door down, leaving nothing standing in your way")

    else:
        print("You fail to break down the door, and you are left with no more options")
        exit()
elif choice == "2":
    roll = random.randrange(0, intelligence)
    if roll >= 35:
        print("By using your superior intellect, you reveal the hiding place of the key and unlock the door")

    else:
        print("While searching for the key, you are ambushed")
        exit()
elif choice == "3":
    roll = random.randrange(0, charisma)
    roll2 = random.randrange(0, intelligence)
    if roll > 15 and roll2 > 30:
        print("You pick the lock and the door swings open, making way for you")

    else:
        print("While trying to pick the lock, you trigger a hidden mechanism and the door falls from its hinges, crushing you ")
        exit()
    print()
elif choice == "4":
    roll = random.randrange(0, magic)
    if roll >= 40:
        print("Your magic is stronger than the enchantment on the door and it is reduced to nothing")
    
    else:
        print("Your magic falters as it is overpowered by the enchantments on the door, and you are left powerless")
        exit()
else:
    print("You can't do that! You lose.")
    exit()
sleep(1)

print("While traveling through the cave the door gaurded, you begin to see a faint light getting closer. Within minutes, you are approached by a group of four armed men carrying a lantern, which was the source of the light you had seen before.")
print("Waht do?")

print("1. Attempt to sneak away")
print("2. Fight the four men in hand to hand combat")
print("3. Reason with the men and talk your way out")
print("4. Use magic to disable the men and escape")

choice = input(">")

if choice == "1":
    roll = random.randrange(0,sneak)
    if roll >= 40:
        print("You skillfully sneak past the men")

    else:
        print("You stumble and are caught")
        exit()
elif choice == "2":
    roll = random.randrange(0, strength)
    if roll >= 40:
        print("After a long and difficult battle you have single-handedly defeated all of the men")

    else:
        print("Whether you are stupidly confident or just stupid, you try to fight the men only to find yourself overwhelmed and dying")
        exit()
elif choice == "3":
    roll = random.randrange(0, charisma)
    if roll >= 45:
        print("With your great charisma, you talk your way out of the situation")

    else:
        print("In your attempts to be a smooth talker, you stumble over your words and are captured by the men")
        exit()
    print()
elif choice == "4":
    roll = random.randrange(0, magic)
    if roll >= 35:
        print("Using your magic, you freeze the men in their place and slip away")
    
    else:
        print("Your magic is not strong enough to hold the men in their place, and they are on you in an instant")
        exit()
else:
    print("You can't do that! You lose.")
    exit()

sleep(1)

print("Now following the cave to its end, you come to a wall of water with a long drop to a lake.")
print("Waht do?")

print("1. Get a running start and dive through the water, aiming for the lake below")
print("2. Search for another way")
print("3. Use magic to stop the water from flowing and slowly lower yourself into the lake")
print("4. Turn back")

choice = input(">")

if choice == "1":
    roll = random.randrange(0, strength)
    roll2 = random.randrange(0, intelligence)
    if roll > 30 and roll2 > 30:
        print("You gather your strength and courage, and dive through the wall of water, safely landing in the lake")

    else:
        print("You run at the wall of water and dive, but the force of the cascading water throws you off course and you belly flop into the lake, breaking every bone in your body and drowning")
        exit()
elif choice == "2":
    print("After searching for some time, you find that there is no other way out.\n Waht do?")
    sleep(1)
    print("1. Get a running start and dive through the water, aiming for the lake below")
    print("2. Use magic to stop the water from flowing and slowly lower yourself into the lake")
    print("3. Turn back")
    choice2 = input(">")
    if choice2 == "1":
        roll = random.randrange(0, strength)
        roll2 = random.randrange(0, intelligence)
        if roll > 30 and roll2 > 30:
            print("You gather your strength and courage, and dive through the wall of water, safely landing in the lake")

        else:
            print("You run at the wall of water and dive, but the force of the cascading water throws you off course and you belly flop into the lake, breaking every bone in your body and drowning")
            exit()
    elif choice2 == "2":
        roll = random.randrange(0, magic)
        if roll >= 30:
            print("Using your magic, you safely lower yourself to the lake")

        else:
            print("While bringing yourself closer to the lake, you lose control of your magic and fall to your death")
        exit()
    elif choice2 == "3":
        print("You decide to turn back, you lose!")
        exit()
    else:
        print("You can't do that! You lose.")
        exit()
elif choice == "3":
    roll = random.randrange(0, magic)
    if roll >= 30:
        print("Using your magic, you safely lower yourself to the lake")

    else:
        print("While bringing yourself closer to the lake, you lose control of your magic and fall to your death")
        exit()
elif choice == "4":
    print("You decide to turn back, you lose!")
    exit()

else:
    print("You can't do that! You lose.")
    exit()

print("After pulling yourself out of the lake and you approach your final challenge. A sword appears in your hand and standing before you is a giant. Five times your size, armed to the teeth, and its only priority is to kill you.\n Waht do?")
sleep(1)
print("1. Using brute force and speed, attack the giant")    
print("2. Attempt to outsmart the giant to trick him into doing your work for you")
print("3. Try sneaking past the giant and avoiding the fight")
print("4. Use your magic to defeat the giant")


choice = input(">")

if choice == "1":
    roll = random.randrange(0,strength)
    if roll >= 40:
        print("You launch yourself at the giant, cutting his legs out from under him, and he falls, defeated")
        sleep(1)
        print("F I N I S H   H I M")

    else:
        print("You run at the giant only to be swat aside like a fly and crushed")
        exit()
elif choice == "2":
    roll = random.randrange(0, intelligence)
    if roll >= 35:
        print("You start running around screaming random things and throwing things to confuse the beast. He trips over himself, falling forward, getting impaled by his own blade")

    else:
        print("You try to confuse the giant, but he was in fact a major in psychology back in his day. He keeps his ground and makes you a player pancake")
        exit()
elif choice == "3":
    roll = random.randrange(0, sneak)
    if roll >= 45:
        print("With your amazing sneak skills you slip between the giant's legs and escape")

    else:
        print("You try to sneak but the giant sees it coming. He sits down while you try to go under him and you are squashed")
        exit()
    print()
elif choice == "4":
    roll = random.randrange(0, magic)
    if roll >= 35:
        print("You summon magic of the gods, and reduce this giant to nothing more than a pile of ashes")
    
    else:
        print("Your magic fails you, and you are left with no time to draw your blade. The giant is upon you and the last thing you see is a double edged sword swinging at you at terminal velocity")
        exit()
else:
    print("You can't do that! You lose.")
    exit()