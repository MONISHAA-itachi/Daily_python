#Number guessing game

import random

s=int(input("Enter the start range:"))
l=int(input("Enter the last range:"))
no = random.randrange(s,l)

a=int(input("Enter the attempts to guess within :"))

for b in range(a):
    try:
        print("Enter the number to guess between ",s," to ",l," :")
        g_no = int(input())
        
        if g_no < s or g_no > l:
            print("Please enter number within the range\n")
            continue
        
        if g_no > no :
            print("Too high")
        if g_no < no :
            print("Too low")
        elif g_no == no:
            print("correct ! YOU WON ")
            
    except ValueError:
        print("Invalid input, Kindly enter a number\n")
    
else:
    print("You ran out of attempts. The number is ",no)
    
    
