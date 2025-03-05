def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    amount = input("Enter amount spent: ")
    category = input("Enter category (e.g., Food, Transport, Entertainment): ")
    with open("expenses.txt", "a") as file:
        file.write(f"{date},{amount},{category}\n")
    print("Expense added successfully!\n")
def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            if not expenses:
                print("No expenses recorded yet.\n")
                return
            print("Date | Amount | Category")
            print("-" * 30)
            for expense in expenses:
                print(" | ".join(expense.strip().split(",")))
            print()
    except FileNotFoundError:
        print("No expenses recorded yet.\n")
def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.\n")
if __name__ == "__main__":
    main()