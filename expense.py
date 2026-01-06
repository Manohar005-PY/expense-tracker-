def create_expense(amount,category,note,date):
    expense ={
        "amount": amount,
        "category": category,
        "note": note,
        "date": date
    }
    return expense

def get_total_spent(expenses):
    if len(expenses) == 0:
        return 0

    total_expenses = 0
    for expense in expenses:
        total_expenses += expense["amount"]
    
    return total_expenses
    
def filter_by_category(expenses,category):
    filtered_expenses = []
    for expense in expenses:
        if expense["category"] == category:
            filtered_expenses.append(expense)
    return filtered_expenses