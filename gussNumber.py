from random import randint
for i in range(1, 10):
    guessNumber = int(input("Enter guess number 1 to 10 :"))
    randomNumber = randint(1, 10)
    if guessNumber == randomNumber:
        print("you are win")
    else:
        print("you are lose")
        print("your random number is", randomNumber)
