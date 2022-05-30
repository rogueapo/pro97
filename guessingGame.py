import random
number = random.randint(1,9)
guess = int(input("Guess a number between 1 and 10: "))
print(number)

if (guess == number):
    print("Hooray!YOU WON")

elif(guess == number-5):
    print("Very close to answer")

elif(guess == number+5):
    print("Very close to answer")

else:
    print("Better luck next time")