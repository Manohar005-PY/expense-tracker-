from storage import save_expense, load_expenses
from expense import create_expense, get_total_spent, filter_by_category
from validators import validate_amount, validate_category, validate_date

def main():
    expenses = load_expenses()

    while True:
        print(" 1. Add Expense \n2. View All Expenses \n3.View Total Spent \n4. view Expenses by Category \n5. Exit")
        choice  = input("Enter your choice:")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue
        if choice == 1:
            amount = input("Enter the amount:")
            category = input("Enter the category:")
            note = input("Enter a note (optional):")
            date = input("Enter the date (YYYY-MM-DD):")
            try:
                amount = validate_amount(amount)
                category = validate_category(category)
                date = validate_date(date)
                expense = create_expense(amount, category, note, date)
                expenses.append(expense)
                save_expense(expenses)
                print("Expense added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 2:
            if not expenses:
                print("No expenses found.")
            else:
                for expense in expenses:
                    print(expense)
        elif choice == 3:
            total = get_total_spent(expenses)
            print(f"Total spent: {total}")
        
        elif choice == 4:
            category  = input("Enter the category to filter by:")
            try:
                category = validate_category(category)
                filtered_expenses = filter_by_category(expenses, category)
                if not filtered_expenses:
                    print(f"No expenses found for category: {category}")
                else:   
                    for expense in filtered_expenses:
                        print(expense)
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == 5:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()