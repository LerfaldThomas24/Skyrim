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
    if roll > 45 and roll2 > 30:
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



sleep(1)

print("After traveling a good distance, you approach a locked door. Waht do?")

print("1.")
print("2.")
print("3.")
print("4.")
