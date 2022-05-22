x = input('Pick a number between 1 and 100')
x = int(x)
questions = 0
if x > 100:
    print("That's not between 1 and 100!  Try again! :)")
if x < 1:
    print("That's not between 1 and 100!  Try again! :)")
if x > 0:
    if x < 100:
        print("Let me take a guess, is your number 50?")
        questions = questions + 1
