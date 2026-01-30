X=int(input("Enter the number of shoes:"))
cx=[]
for a in range(X):
    y=int(input("enter the shoe size:"))
    cx.append(y)    
N=int(input("Enter the number of customers:"))
C=[]
for b in range(N):
    s=int(input("Enter the shoe size:"))
    if s in cx:
        c=int(input("Enter the amount:"))
        C.append(c)
    else:
        print("No available size") 
print(sum(C))
        
