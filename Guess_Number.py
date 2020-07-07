answer = 44

questions = "What number am I thinking of?"
print("Let's play the guessing game!")

while True:
    guess = int(input(questions))

    if guess < answer:
        print("Little higher")
    elif guess > answer:
        print("Little lower")
    else: # guess==answer
        print("Are you a MINDREADER!!!")
        break