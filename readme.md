# Expense Tracker

The Expense Tracker is a Python-based application designed to help users plan and track their monthly expenses. 
It provides insights into spending habits, ensures expenses are within a predefined budget, and allows for 
category-wise allocation and tracking of expenses. All data is stored persistently in a CSV file for future reference.

## Features
- Create a personalized expense tracking plan based on your monthly salary.
- Allocate spending limits for multiple categories.
- Track spending and get alerts when exceeding the planned budget.
- Save and retrieve expense data using a CSV file.
- User-friendly interaction through a text-based interface.

## Requirements
- Python 3.6 or higher
- CSV file module (built-in with Python)
- A text editor or IDE (e.g., Visual Studio Code)

## How to Run
1. Clone or download the project files to your local machine.
2. Open the terminal and navigate to the project directory.
3. Ensure Python is installed by running:
   ```bash
   python --version

## File Descriptions

- **exp_tracker.py**: The main Python script for the Expense Tracker application.
- **exp_tracker.csv**: A CSV file used to store user data persistently, including salaries, spending amounts, and expenses by category.
- **backup.py** (if applicable): A script to manage backup operations for the data file.

## sample input and output

welcome to Expense Tracker !...
user Name:john
Enter your salary:50000
Enter your spending amount:20000
Hi john, you planned to spend ₹ 20000
how many category you want to plan?:3
your planned for 3 categories
Enter the name of categories 1: Groceries
Enter the name of categories 2: Rent
Enter the name of categories 3: Entertainment
category:Groceries
Enter the amount spent on Groceries (or press Enter to skip): 5000
Spending amount: 5000.0
Remaining Balance: 15000.0
category:Rent
Enter the amount spent on Rent (or press Enter to skip): 10000
Spending amount: 10000.0
Remaining Balance: 5000.0
category:Entertainment
Enter the amount spent on Entertainment (or press Enter to skip): 3000
Spending amount: 3000.0
Remaining Balance: 2000.0
your data are save successfully...
Thank you for using the Expense Tracker. Goodbye!!!

input:
Welcome to Expense Tracker! User Name: John Enter your salary: 50000 Enter your spending amount: 20000 How many categories do you want to plan?: 3
Enter the name of category 1: Groceries Enter the name of category 2: Rent Enter the name of category 3: Entertainment 
Enter the amount spent on Groceries: 5000 Enter the amount spent on Rent: 10000 Enter the amount spent on Entertainment: 3000

output:
Hi John, you planned to spend ₹ 20000. Category: Groceries Spending amount: ₹ 5000 Remaining balance: ₹ 15000 Category: Rent Spending amount: ₹ 10000
Remaining balance: ₹ 5000 Category: Entertainment Spending amount: ₹ 3000 Remaining balance: ₹ 2000

Your data is saved successfully... Thank you for using the Expense Tracker. Goodbye!

## Potential Enhancements

- Add a graphical user interface (GUI) for better usability.
- Include visualizations for spending trends and savings (e.g., charts).
- Integrate with external storage options like a database or cloud services.
- Add support for exporting reports to PDF or Excel formats.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
