
import json
""" 







"""

print(" ====Monthly Budget==== ")


class InvalidInputError(Exception):
    "custom exceptio for invalid input"



class BudegtCalculator:
    
    def __init__(self):
        self.name = ""
        self.income = 0.0
        self.expenses = {}
        
    @staticmethod        
    def validate_number(value):
      try:
        return float
    
      except ValueError:
        InvalidInputError("Enter a valid number")
        
        
        
    def to_json(self):
        json.dumps({
            "name":self.name,
            "income":self.income,
            "expenses":self.expenses
        })
    
    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        obj = cls
        obj.name = data["name"]
        obj.income = data["income"]
        obj.expenses = data["expenses"]  
        return obj  


    @classmethod 
    def save_to_json(self, filename="budget_saving.json"):
       with open(filename, "w") as file:
           file.write(self.to_json())
           
           
    def load_from_json(cls, filename="budget_saving.json"):
        with open(filename, "r") as file:
            json_data = file.read()
        
        return cls.from_json(json_data)           
        
            

    def get_valid_number(self, prompt):
        
    

        while True:
            
            try:
        
                    value = input(prompt)
                    return BudegtCalculator.validate_number()
            except   InvalidInputError as e:
                print(e)         
    
    

    # step 1
    def get_user_details(self):
        self.name = input("enter your name:")
        self.income = self.get_valid_number("Enter your monthly income:$")
       



    def get_expenses(self):
        expense_categories = ["Rent", "Groceries", "Transport", "Entertainment"]
        print("\n------print your expenses----")
        
        
        for category in expense_categories:
            try:
                self.expenses[category] = self.get_valid_number(f"{category} expense:$")
                
            except Exception:
                print("error entering expenses.please try again")    
        
                
        


    def calculate_budget(self):
        total_expenses = sum(self.expenses.values())
        remaining_balance = self.income - total_expenses
        
        try:
           savings_ratio  =  (remaining_balance / self.income) * 100 if self.income > 0 else 0
        except ZeroDivisionError:
            savings_ratio = 0     
        
        return total_expenses, remaining_balance, savings_ratio
    
    
        

    def display_summary(self,total_expenses,remaining_balance, savings_ratio):  
        
            print("==== Monthly budget Summary==== ")
            print(f"Monthly budget summmary for {self.name}")
            print(f"monthly income:${self.income:.2f}")

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
            
            
            
    def show_expense_breakdown(self):
        choice =  input("\nWould you like to see breakdown of your expenses?(yes/no):").strip().lower()

        if choice == "yes":
        
        
            total = sum(self.expenses.values())
        
            print("\nExpense breakdown")
            for category, amount in self.expenses.items():
                percent = (amount / total) * 100
                print(f"{category}:{amount:.2f} ({percent:.2f})")
            
            
    
 
 
def main():
    
    calculator = BudegtCalculator()
    calculator.get_user_details()
    calculator.get_expenses()

    total_expenses, remaining_balance, savings_ratio = calculator.calculate_budget()

    calculator.display_summary(total_expenses, remaining_balance, savings_ratio)
    calculator.show_expense_breakdown()
    
    
    # print("\n------serialized data----")
    # json_data = calculator.to_json()
    # print(json_data)
    
    # print("\n----deserialized Json data")
    # new_calculator = calculator.from_json(to_json)
    # print(f"Deserialized data for:{new_calculator.name}")
    
    print("\nsaving budget in file.....")
    calculator.save_to_json()
    
    print("\n loaded data from file")
    loaded_calc = calculator.load_from_json()
    print(f"loaded data for:{loaded_calc.name}")
    

    print("=== Thank You for using the Personal Budget Saving Tool ===")

    
if __name__ == "__main__":  
    main()   
   
    
    
       
            
            
                   
                    
    
 
             
    










    
 

     
            #commit it  