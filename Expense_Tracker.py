expenses = {}

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        category = input("Enter category (Food, Travel, Bills, etc): ").capitalize()
        amount = float(input("Enter amount: "))

        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount

        print("Expense added successfully.")

    elif choice == "2":
        if not expenses:
            print("\nNo expenses added yet.")
        else:
            print("\nYour Expenses:")
            for cat, amt in expenses.items():
                print(f"{cat}: ₹{amt}")

    elif choice == "3":
        total = sum(expenses.values())
        print(f"\nTotal Spent: ₹{total}")

    elif choice == "4":
        print("\nExiting... Thank you for using the tracker!")
        break

    else:
        print("Invalid choice, try again.")

