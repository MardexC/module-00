# Module 3 - Laboratory 5: The Menu Comes Alive
# Made by: Mardex A. Cantiga

print("=" * 40)
print("          EXPENSE TRACKER")
print("      Know where your money goes.")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

print(f"Welcome, {name}!")

subtotal = 0.0
count = 0
choice = ""

while choice != "4":
    print("\nMAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses (coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))

        subtotal += amount
        count += 1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * tax_percent / 100
        grand_total = subtotal + tax
        over_budget = grand_total > budget

        print(f"Expenses:     {count:>7}")
        print(f"Subtotal:     ${subtotal:>7.1f}")
        print(f"Tax ({tax_percent:.1f}%): ${tax:>7.1f}")
        print(f"Grand total:  ${grand_total:>7.1f}")

        if over_budget:
            print(f"Over budget by ${grand_total - budget:.1f}!")
        elif grand_total > budget * 0.90:
            print(f"Careful: only ${budget - grand_total:.1f} left.")
        else:
            print(f"Within budget. ${budget - grand_total:.1f} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: Mardex A. Cantiga | Installment 5")
        print("=" * 40)

    else:
        print("Please choose 1, 2, 3 or 4.")
