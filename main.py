

""" 







"""

print(" ====Monthly Budget==== ")


def get_valid_number(prompt):
    
 

    while True:
    
            value = input(prompt)
            
            if value.replace(".", "", 1).isdigit():
                return float(value)
            
            else:
                print("enter a monthly income") 
 
    

# step 1
def get_user_details():
    name = input("enter your name:")
    income = get_valid_number("Enter your monthly income:$")
    return name,income



def get_expenses():
    expense_categories = ["Rent", "Groceries", "Transport", "Entertainment"]
    expenses = {}
    
    for category in expense_categories:
        expenses[category] = get_valid_number(f"Enter Your {category} expense:$")
    return expenses    
    


def calculate_budget(income, expenses):
    total_expenses = sum(expenses.values())
    remaining_balance = income - total_expenses
    savings_ratio  =  (remaining_balance / income) * 100
    
    return total_expenses, remaining_balance, savings_ratio
    
    
        

def display_summary(name, income,total_expenses,remaining_balance, savings_ratio):  
    
        print("==== Monthly budget Summary==== ")
        print(f"Monthly budget summmary for {name}")
        print(f"monthly income:${income:.2f}")

        print(f"Total  expenses:${total_expenses:.2f}")
        print(f"Remaining balance:${remaining_balance:.2f}")
        print(f"Savings Ratio:{savings_ratio:.2f}%")

        # step 5

        print("==============================")

        if savings_ratio < 10:
            print("YOur savings are low, try reducing expenses")
        elif savings_ratio < 30:
            print("You are saving fairly, keep improving")
        else:
            print("great job!!, you are saving nicely")  
            
            
            
def show_expense_breakdown(expenses):
    choice =  input("\nWould you like to see breakdown of your expenses?(yes/no):").strip().lower()

    if choice == "yes":
       
       
        total = sum(expenses.values())
    
        print("\nExpense breakdown")
        for category, amount in expenses.items():
            percent = (amount / total) * 100
            print(f"{category}:{amount:.2f} ({percent:.2f})")
            
            
    
 
 
def main():
    name, income = get_user_details()
    expenses = get_expenses()

    total_expenses, remaining_balance, savings_ratio = calculate_budget(income, expenses)

    display_summary(name, income, total_expenses, remaining_balance, savings_ratio)
    show_expense_breakdown(expenses)

    print("=== Thank You for using the Personal Budget Saving Tool ===")

    
    
main()    
    
    
       
            
            
                   
                    
    
 
             
    










    
 

     
             