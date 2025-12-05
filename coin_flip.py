import random

choices = ("h", "t")
names = {"h": "Heads", "t": "Tails"}

while True:
    coin = random.choice(choices)  
    user = input("Heads or Tails? (h/t) : ").lower()

    if user not in choices:
        print("Invalid input! Please enter 'h' or 't'.")
        continue

    if user == coin:
        print(f"{names[coin]} — You win! You guessed right.")
    else:
        print(f"{names[coin]} — You guessed wrong.")

    cont = input("Do you want to continue? (y/n) : ").lower()
    if cont == "n":
        print("Thanks for playing!")
        break
    elif cont != "y":
        print("Invalid input! Exiting game.")
        break
