import random

while 1:
    c=0
    choice=input("\nDo you want to play ? (y/n) :").lower()
    if choice=="y":
        dice=int(input("Enter how many dices to play with ?"))
        for a in range(1,dice+1):
            print("Dice",a,"-",random.randint(1,6),)
        c+=1
        if c==1 or c==0:
            print("\nYou have played this many time",c)
        else:    
            print("\nYou have played this many times",c)
    elif choice =="n":
        print("Thank you for playing")
        break
    else:
        print("Invalid choice")
            
    
