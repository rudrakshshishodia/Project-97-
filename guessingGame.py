import random
print("Guess the number")
number = random.randint(1,9)
chances = 0
print("Guess a number (between 1 - 9):")

while chances < 5:

    guess = int(input("Enter your guess:"))

    if guess == number:
        print("Congratulations your guess is correct!")
        break

    elif guess < number:
        print("Your guess is too low:( . Try another numbber", guess)
        
    else:
        print("Your guess is too high. Try another number", guess)
        

    chances += 1
    if not chances < 5:
        print("You didn't make it to the end. The number is", number)
        

    