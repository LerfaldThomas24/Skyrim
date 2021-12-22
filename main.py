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
















print("You encounter a menacing wall. Waht do?")

print("1. Punch wall")
print("2. Reason with wall")
print("3. Climb wall")
print("4. Magic wall")

choice = input()

if choice == "1":
    roll = random.randrange(0,strength)
    if roll > 20:
        print("The wall crumbles to the blow you deliver")

    else:
        print("Your fist shatters.")
        exit()
elif choice == "2":
    print()
elif choice == "3":
    print()
elif choice == "4":
    print()
else:
    print("You can't do that! You lose.")

