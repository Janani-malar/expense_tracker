import csv
import os

def expense_tracker(): 
    print("Welcome to Expense Tracker!")

    filename = "exp_tracker.csv"  # Path to store data in exp_tracker.csv
    user_data = exit_data(filename)  #load existing data from the CSV file
    name = input("User Name: ") 

    if name in user_data:  
        print(f"Welcome Back, {name}!")
        user_data = user_data[name]
        print(f"Your saved details:\n"
              f"Salary: ₹{user_data['salary']}\n"
              f"Spending Amount: ₹{user_data['spending amount']}\n"
              f"Balance: ₹{user_data['balance']}\n"
              f"Expenses: {user_data['expenses']}")
        print("Thank you for using the Expense Tracker. Goodbye!")
        return  # Return early for existing users

    # New user flow
    salary = int(input("Enter your salary: "))
    spend_amt = int(input("Enter your spending amount: "))

    if salary < spend_amt:
        print("Your spending amount is more than your salary.")
        spend_amt = salary

    print(f"Hi {name}, you planned to spend ₹{spend_amt}")

    num_categories = int(input("How many categories do you want to plan?: "))
    categories = []  # creating an empty list for saving  future data
    expenses = {}  #creating an empty dictionary for saving  future data

    print(f"Your planned for {num_categories} categories")

    for i in range(num_categories):  # Code for appending categories with numbering ({i+1})  
        category = input(f"Enter the name of category {i+1}: ")
        categories.append(category)

    bal = spend_amt
    filled_categories = 0

    for category in categories:
        print(f"Category: {category}")
        expense =input(f"Enter the amount spent on {category} (or press Enter to skip): ").strip()

        if not expense:
            print(f"Skipping the {category}")
            continue
            
        expense=float(expense)  # Convert to integer after ensuring input is not empty  (strip())
        filled_categories += 1
        expenses[category] = expense

        if expense > bal:
            excess_amount = expense - bal
            print("Alert! You are spending more than your balance.\n"
                f"Excess amount: ₹{excess_amount}")
            conti_decision = input("Do you want to proceed? (y/n): ").strip().lower()

            if conti_decision == "y":
                expense = float(input(f"Re-enter the amount spent on {category}: ").strip())

                # Update the balance and store the expense in the dictionary
                expenses[category] = expense
                bal -= expense

                print(f"Spending amount: ₹{expense}")
                print(f"Remaining Balance: ₹{bal}")

                continue  # Skip to the next iteration
            else:
                print(f"Skipping {category} due to insufficient balance.")
                print("thank you")
                return


        bal -= expense
        print(f"Spending amount: ₹{expense}")
        print(f"Remaining balance: ₹{bal}")

    # Handle unfilled categories before saving the data
    unfill_categories = num_categories - filled_categories
    if unfill_categories > 0:
        print(f"Your planned {num_categories} categories but you filled only {filled_categories}.")
        print(f"{unfill_categories} categories are left unfilled.")
        print(f"Your remaining balance is ₹{bal}")

        for category in categories:
            if category not in expenses:
                print(f"Category: {category}")
                expense = input(f"Enter the amount spent on {category} (or press Enter to skip): ").strip()

                if not expense:
                    print(f"Skipping the {category}")
                    continue

                expense = float(expense)
                filled_categories += 1
                expenses[category] = expense

                if expense > bal:
                    excess_amount = expense - bal
                    print("Alert! You are spending more than your balance.\n"
                        f"Excess amount: ₹{excess_amount}")
                    conti_decision = input("Do you want to proceed? (y/n): ").strip().lower()

                    if conti_decision == "y":
                        expense = float(input(f"Re-enter the amount spent on {category}: ").strip())

                        # Update the balance and store the expense in the dictionary
                        expenses[category] = expense
                        bal -= expense

                        print(f"Spending amount: ₹{expense}")
                        print(f"Remaining Balance: ₹{bal}")

                        continue  # Skip to the next iteration
                    else:
                        print(f"Skipping {category} due to insufficient balance.")
                        print("thank you")
                        return

                bal -= expense
                print(f"Spending amount: ₹{expense}")
                print(f"Remaining balance: ₹{bal}")

    # Save data to CSV file
    csv_file(name, salary, spend_amt, expenses, bal, filename)
    print("Your data are saved successfully...")
    print("Thank you for using the Expense Tracker. Goodbye!")

def exit_data(filename): #Load existing data from the CSV file
    user_data={}
    if os.path.exists(filename):
        with open(filename,mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name=row['name']
                if name not in user_data:
                    user_data[name]={
                        "salary":int(row["salary"]),
                        "spending amount":int(row['spend_amt']),
                        "balance":float(row['bal']),
                        'expenses':{}
                }
                user_data[name] ['expenses'] [row['category']] = float(row['expense'])
    return user_data


def csv_file(name,salary,spend_amt,expenses,bal,filename):  #Append data to the CSV file
    filename="exp_tracker.csv"
    file_exists = os.path.exists(filename)
    with open (filename,mode="a", newline="") as file:
        writer=csv.writer(file)

        if not file_exists:    #Write header only if the file doesn't exist
            writer.writerow(['name','salary','spend_amt','category','expense','balance'])
        for category ,expense in expenses.items():
            writer.writerow([name,salary,spend_amt,category,expense,bal])


expense_tracker()