import csv
import os

def expense_tracker(): 
    print("Welcome to Expense Tracker!")

    filename = "exp_tracker.csv"  # Path to store data
    user_data = exit_data(filename)  # Load existing data from the CSV file


    try:
        name = input("User Name: ").strip()
        if not name:  # Check if the username is empty
            raise ValueError("Username cannot be empty. Please enter a valid name.")
    except ValueError as e:
        print(f"Error: {e}")
        return
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
        return

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
    try:
        salary = int(input("Enter your salary: "))
        spend_amt = int(input("Enter your spending amount: "))
    except ValueError:
        print("Invalid input! Please enter a valid number for salary or spending amount.")
        return

    if salary < spend_amt:
        print("Your spending amount is more than your salary.")
        print("Thank you. Please enter the details again.")
        return

    print(f"Hi {name}, you planned to spend ₹{spend_amt}")

    try:
        num_categories = int(input("How many categories do you want to plan?: "))
    except ValueError:
        print("Invalid input! Please enter a valid number of categories.")
        return

    categories = []   # creating an empty list for saving  future data
    expenses = {}  # creating an empty dict for saving  future data
    print(f"Your planned for {num_categories} categories")

    for i in range(num_categories):
        try:
            category = input(f"Enter the name of category {i+1}: ").strip()
            if not category:
                raise ValueError("Category name cannot be empty!")
            categories.append(category)
        except ValueError as e:
            print(f"Error: {e}")
            continue

    bal = spend_amt
    filled_categories = 0

    for category in categories:
        print(f"Category: {category}")
        try:
            expense = input(f"Enter the amount spent on {category} (or press Enter to skip): ").strip()
            if not expense:
                print(f"Skipping the {category}")
                continue

            expense = float(expense)
            filled_categories += 1
            expenses[category] = expense

            if expense > bal:
                excess_amount = expense - bal
                print(f"Alert! You are spending more than your balance.\nExcess amount: ₹{excess_amount}")
                conti_decision = input("Do you want to proceed? (y/n): ").strip().lower()

                if conti_decision == "y":
                    try:
                        expense = float(input(f"Re-enter the amount spent on {category}: ").strip())
                    except ValueError:
                        print("Invalid input! Skipping this category.")
                        continue

                    expenses[category] = expense
                    bal -= expense
                    print(f"Spending amount: ₹{expense}")
                    print(f"Remaining Balance: ₹{bal}")
                    continue
                else:
                    print(f"Skipping {category} due to insufficient balance.")
                    continue

            bal -= expense
            print(f"Spending amount: ₹{expense}")
            print(f"Remaining balance: ₹{bal}")
        except ValueError:
            print("Invalid input! Please enter a valid number for expenses.")
            continue

    # Handle unfilled categories before saving the data
    unfill_categories = num_categories - filled_categories
    if unfill_categories > 0:
        print(f"Your planned {num_categories} categories but you filled only {filled_categories}.")
        print(f"{unfill_categories} categories are left unfilled.")
        print(f"Your remaining balance is ₹{bal}")

        for category in categories:
            print(f"Category: {category}")
            try:
                expense = input(f"Enter the amount spent on {category} (or press Enter to skip): ").strip()
                if not expense:
                    print(f"Skipping the {category}")
                    continue

                expense = float(expense)
                filled_categories += 1
                expenses[category] = expense

                if expense > bal:
                    excess_amount = expense - bal
                    print(f"Alert! You are spending more than your balance.\nExcess amount: ₹{excess_amount}")
                    conti_decision = input("Do you want to proceed? (y/n): ").strip().lower()

                    if conti_decision == "y":
                        try:
                            expense = float(input(f"Re-enter the amount spent on {category}: ").strip())
                        except ValueError:
                            print("Invalid input! Skipping this category.")
                            continue

                        expenses[category] = expense
                        bal -= expense
                        print(f"Spending amount: ₹{expense}")
                        print(f"Remaining Balance: ₹{bal}")
                        continue
                    else:
                        print(f"Skipping {category} due to insufficient balance.")
                        continue

                bal -= expense
                print(f"Spending amount: ₹{expense}")
                print(f"Remaining balance: ₹{bal}")
            except ValueError:
                print("Invalid input! Please enter a valid number for expenses.")
                continue       

   # Save data to CSV file
    try:
        csv_file(name, salary, spend_amt, expenses, bal, filename)
        print("Your data is saved successfully.")
    except Exception as e:
        print(f"Error saving data to file: {e}")

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