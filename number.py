import random

number = random.randint(1,100)
attempt = 0

print("Welcome to the number guessing game!!!")
print("I have selected a number in range 1 to 100")

while True:
    guess = int(input("Enter your guess:"))
    attempt+=1
    if guess==number:
        print("Congratulations! You guessed correctly!")
        break
    elif guess < number:
        print("Too Low!! Guess Againn!!")
    else:
        print("Too high! Guess Again!!")
    if attempt>=7:
        print("You  lost the game! The number was", number)
        break