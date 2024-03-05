import json
import os

def load_data():
    if os.path.exists("budget_data.json"):
        with open("budget_data.json", "r") as file:
            return json.load(file)
    else:
        return {"income": 0, "expenses": []}

def save_data(data):
    with open("budget_data.json", "w") as file:
        json.dump(data, file)

def add_income(data):
    income = float(input("Enter income amount: "))
    data["income"] += income
    print("Income added successfully!")

def add_expense(data):
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    data["expenses"].append({"amount": amount, "category": category})
    print("Expense added successfully!")

def calculate_budget(data):
    total_expenses = sum(expense["amount"] for expense in data["expenses"])
    budget = data["income"] - total_expenses
    return budget

def analyze_expenses(data):
    expense_categories = {}
    for expense in data["expenses"]:
        category = expense["category"]
        amount = expense["amount"]
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount
    return expense_categories

def main():
    data = load_data()

    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Analyze Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_income(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            budget = calculate_budget(data)
            print(f"Your remaining budget is: {budget}")
        elif choice == "4":
            expense_analysis = analyze_expenses(data)
            print("Expense Analysis:")
            for category, amount in expense_analysis.items():
                print(f"{category}: {amount}")
        elif choice == "5":
            save_data(data)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
