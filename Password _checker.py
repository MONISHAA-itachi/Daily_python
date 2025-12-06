p = input("Enter password: ")

l = len(p)
u = any(i.isupper() for i in p)
d = any(i.isdigit() for i in p)
s = any(i in "!@#$%^&*()" for i in p)

print("\nChecking password...")

if l >= 8 and u and d and s:
    print("Strong Password 💪")
elif l >= 6 and (u or d or s):
    print("Medium Password 👍")
else:
    print("Weak Password ❌")
    
print(f"\nLength: {l}")
print(f"Uppercase: {'✔' if u else '✘'}")
print(f"Digit: {'✔' if d else '✘'}")
print(f"Symbol: {'✔' if s else '✘'}")
