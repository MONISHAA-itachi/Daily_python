import random

choices = ("r","p","s")
s={"r":"✊","p":"✋","s":"✌️"}

while 1:
    u = input("\nRock, Paper, Scissors ? (r/p/s) :").lower()
    if u in choices:
        c = random.choice(choices)

        print(f'You chose {s[u]}')
        print(f'Computer chose {s[c]}')

        if ((u == "r" and c == "p") or
            (u=="r" and c=="s") or
            (u=="p" and c=="r") or
            (u=="s" and c=="p")):
            print("You win")
        else:
            print("You lose")
        ch=input("\nDo you want to continue ? (y/n) :").lower()
        if ch == "n" :
            break
    else:
        print("Invalid input. Try again")

    

    
    

