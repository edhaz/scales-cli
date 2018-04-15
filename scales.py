import sys
import random

instruments = ['Violin', 'Piano']

grades = ['1', '2', '3', '4', '5', '6', '7', '8']

if len(sys.argv) != 3:
    print("Usage: python scales.py [instrument] [grade]")
    sys.exit(1)
elif sys.argv[1] not in instruments:
    print("We don't cater for that instrument yet, sorry!")
    print("Usage: python scales.py [instrument] [grade]")
    sys.exit(2)
elif sys.argv[2] not in grades:
    print("That's not a recognised Grade!")
    print("Usage: python scales.py [instrument] [grade]")
    sys.exit(3)

print("Welcome to the Scales application!")
print("This setup is for Grade {} {}.".format(sys.argv[2], sys.argv[1]))
print("If this is incorrect please restart the app. (Press Ctrl-C to exit)")
print("Usage: scales.py [instrument] [grade]")

if sys.argv[1] == 'Violin':
    if sys.argv[2] == '4':
        scales = ['Ab major', 'B major', 'C major', 'E major', 'G minor', 'B minor', 'C minor']

print("")
print("REMEMBER TO PRACTICE EACH SCALE AT LEAST 5 TIMES!") 
print("")
print("Your first scale is: ") 
print("")

while scales:
    scale = random.choice(scales)
    scales.remove(scale)
    print("  - {}, two octaves".format(scale))
    print("")
    if scales:
        user_input = input("Press enter for the next scale.")
        print("")
    else:
        print("")

print("")
print("That's all the scales, well done!")
print("")
