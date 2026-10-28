# Module 3 - Laboratory 4: The Tracker Makes Decisions
# Made by: Mardex A. Cantiga

print("=" * 40)
print("          EXPENSE TRACKER")
print("      Know where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("  [1] Add an expense       (coming soon)")
print("  [2] View all expenses    (coming soon)")
print("  [3] Show total spent     (coming soon)")
print("  [4] Exit                 (coming soon)")

name = input("\nWhat's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

expense1 = input("\nFirst expense? ")
amount1 = float(input("Amount? "))

if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

expense2 = input("Second expense? ")
amount2 = float(input("Amount? "))

if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

tax_rate = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

subtotal = amount1 + amount2
average = subtotal / 2
tax = subtotal * tax_rate / 100
grand_total = subtotal + tax

over_budget = grand_total > budget

print("\n" + "-" * 40)
print("SUMMARY")
print(f"  - {expense1 + ':':<12}${amount1:>7.1f}")
print(f"  - {expense2 + ':':<12}${amount2:>7.1f}")
print(f"  {'Subtotal:':<15}${subtotal:>7.1f}")
print(f"  {'Average:':<15}${average:>7.1f}")
print(f"  {'Tax (' + str(tax_rate) + '%):':<15}${tax:>7.1f}")
print(f"  {'Grand total:':<15}${grand_total:>7.1f}")

if over_budget:
    print(f"  Over budget by ${grand_total - budget:.1f}!")
elif grand_total > budget * 0.90:
    print(f"  Careful: only ${budget - grand_total:.1f} left.")
else:
    print(f"  Within budget. ${budget - grand_total:.1f} left.")

print("-" * 40)
print("Made by: Mardex A. Cantiga | Installment 4")

