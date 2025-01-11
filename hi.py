from expense import Expense


def main():
    print(f"🎯Running Expense Tracker!")
    expense_file_path = "expenses.csv"

    #Get user input for expense.
    expense = get_user_expense()
    

    #Write their expense to a file.
    save_expense_to_file(expense,expense_file_path)

    #Read file and summarize expenses.
    summarize_expenses(expense_file_path)
    


def get_user_expense():


    print(f"🎯Getting User Expense")
    expense_name = input("Enter expense name:")
    expense_amount = float(input("Enter expense amount:" ))
    

    expense_categories =[
        "🍟Food\n",
        "🏡Home\n",
        "💼Work\n",
        "🎉Fun\n",
        "💕misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i+1}. {category_name}")

        value_range = f" [1- {len(expense_categories)}]"
        selected_index = int (input(f"Enter a category number {value_range}: ")) - 1

        if 0 <= selected_index < len(expense_categories) :
            selected_category = expense_categories [selected_index]
            new_expense = Expense(
                name = expense_name ,category = selected_category , amount=expense_amount
            )
            print(f"New expense created: {new_expense}")
            break
        else:
            print(f"Invalid selection. Please try again!")