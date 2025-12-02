

""" 







"""

print(" ====Monthly Budget==== ")

name = input("enter your name:")
monthly_income = float(input("Enter yur monthly income:$",))
rent = float(input("enter your rent Expenses:$"))
groceries = float(input("enter your groceries Expenses:$"))
transport = float(input("enter your transport Expenses:$"))
entertainment = float(input("enter your entertaiment Expenses:$"))

total_expenses = rent + groceries + transport + entertainment
savings = monthly_income - total_expenses
savings_ratio = (savings / monthly_income) * 100


print("==== Monthly budget Summary==== ")
print(f"Monthly budget summmary for {name}")
print(f"monthly income:${monthly_income}")

print(f"Rent expenses:${rent}")
print(f"Groceries Expenses:${groceries}")
print(f"Transport expenses:${transport}")
print(f"Entertainment Expenses:${entertainment}")
print(f"Savings Ratio:${savings_ratio}")