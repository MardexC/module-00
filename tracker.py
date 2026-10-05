# Expense Tracker - Installment 2: Talking to the User
# Author: Junsay, Geme Earl C.
# A simple expense tracker that accepts two expenses from the user.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("MAIN MENU")
print("\t[1] Add an expense (coming soon)")
print("\t[2] View all expenses (coming soon)")
print("\t[3] Show total spent (coming soon)")
print("\t[4] Exit (coming soon)")
print()

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)
print(f"Made by: {name} | Installment 2")
