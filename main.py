

""" 







"""
# step 2
print(" ====Monthly Budget==== ")

name = input("enter your name:")

valid = False

while not valid:
    
    monthly_income = input("Enter yur monthly income:$",)
    
    if monthly_income.replace(".", "", 1).isdigit():
        monthly_income = float(monthly_income)
        valid = True
    
    else:
        print("enter a monthly income")    
          
    
    
valid = False

while not valid:    
    
    rent = input("enter your rent Expenses:$")
    if rent.replace(".", "", 1).isdigit():
        rent = float(rent)
        valid = True
    else:
        print("enter a valid rent")    
             
    
valid = False 
while not valid:  
    groceries = input("enter your groceries Expenses:$")
    
    if groceries.replace(".", "", 1).isdigit():
        groceries = float(groceries)
        valid = True
    else:
        print("enter a valid groceries expenses")
        
valid = False 
while not valid:  
    transport = input("enter your transport Expenses:$")
    
    if transport.replace(".", "", 1).isdigit():
        transport = float(transport)
        valid = True
    else:
        print("enter a valid transport expenses")
        

valid = False 
while not valid:  
    entertainment = input("enter your entertainment Expenses:$")
    
    if entertainment.replace(".", "", 1).isdigit():
        entertainment = float(entertainment)
        valid = True
    else:
        print("enter a valid entertainment expenses")

# step 3
total_expenses = rent + groceries + transport + entertainment
remaining_balance = monthly_income - total_expenses
# savings = monthly_income - total_expenses
if monthly_income > 0:
    savings_ratio = (remaining_balance / monthly_income) * 100
else:
    savings_ratio = 0



# step 4
print("==== Monthly budget Summary==== ")
print(f"Monthly budget summmary for {name}")
print(f"monthly income:${monthly_income}")

print(f"Rent expenses:${rent}")
print(f"Groceries Expenses:${groceries}")
print(f"Transport expenses:${transport}")
print(f"Entertainment Expenses:${entertainment}")
print(f"Savings Ratio:${savings_ratio}")

# step 5

print("==============================")

if savings_ratio < 10:
    print("YOur savings are low, try reducing expenses")
elif savings_ratio < 30:
    print("You are saving fairly, keep improving")
else:
    print("great job!!, you are saving nicely")   
    
 
choice =  input("\nWould you like to see breakdown of your expenses?(yes/no):").strip().lower()

if choice == "yes":
    categories = ["Rent", "Groceries", "Transport", "Entertainment"]
    values = [rent, groceries, transport, entertainment]
    total = total_expenses
    
    print("\nExpense breakdown")
    
    i = 0
    while i < len(categories):
        percent = (values[i] / total) * 100
        print(categories[i], ":",  f"${values[i]:.2f}", ":" f"({percent:.2f}%)")
        
        i += 1
        
        
print("===Thank You for using the Personal Budget saving tool")        
     
             