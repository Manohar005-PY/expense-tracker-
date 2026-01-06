def validate_amount(value):
    try:
        amount = float(value)
    except ValueError:
        raise ValueError("Amount must be a number.")

    if amount < 0:
           raise ValueError("Amount cannot be negative.")
    return amount

def validate_category(value):
    if len(value.strip()) == 0:
        raise ValueError("Category cannot be empty.")
     
    if not isinstance(value, str):
        raise ValueError("Category must be a string.")
    
    return value.lower()

def validate_date(value):
    if not isinstance(value, str):
        raise ValueError("Date must be a string in YYYY-MM-DD format.")
    
    parts = value.split("-")
    if len(parts) != 3:
        raise ValueError("Date must be in YYYY-MM-DD format.")
    year, month, day = parts
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        raise ValueError("Date must contain only numbers in YYYY-MM-DD format.")
    year, month, day = int(year), int(month), int(day)
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")
    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31.")
    return value
        