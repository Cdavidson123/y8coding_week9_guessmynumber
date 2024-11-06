from random import randint 

correct = randint(0,100)
number = None
while number != correct:
    print("Guess my number")
    number = int(input())

    if number > correct:
        print("LOWER!")

    if number < correct:
        print("HIGHER!")

    if number == correct:
        print("YOU GOT IT!")

    fiveless = correct - 5
    fivemore = correct + 5

    if number >= fiveless and number <= fivemore:
        print("ALMOST! WITHIN 5 AWAY!")
