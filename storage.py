import json
FILE_PATH = "data.json"
def load_expenses():
    try:
        with open(FILE_PATH,"r",encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    
def save_expense(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

data = load_expenses()
print(data)