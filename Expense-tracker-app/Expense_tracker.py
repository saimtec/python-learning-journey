from Expense import Expense
from datetime import datetime, timedelta


def main():
# getting data from user
   try:
       expense = user_expense()
       expense_file_path = "Expencse tracker app\expense.csv"
       budget = 2000 



# # saving user expense related all data into the file
       saving_to_file(expense, expense_file_path)



# fetching the expense data of user from the file
       getting_expense(expense_file_path, budget)

   except Exception as e:
       print(f"Unexpected error in main: {e}")






def user_expense():
    try:
        print("\n")
        print(f"\t💵 Getting user expense : ")
        while True:
            name_expense = input("Enter Expense name : ")
            if not name_expense.replace(" ", "").isalpha():
                print("❌ Name must contain only letters. Please try again.")
            else:
                break

        while True:
            try:
           
                amount_expense = float(input("Enter amount of expense: "))
                break
            except ValueError:
                print("❌ Please enter a valid number for amount.")
            except NameError:
                print("❌ Please enter a valid name .")

        print(f"You have entered {name_expense} , 💲{amount_expense} ")

        category_expense = [
            "🍍Food",
            "🏠Home",
            "🏢Work",
            "🎉Fun",
            "✨Others"
        ]


        while True:
            print("Select a Category ")
            for i, category_name in enumerate(category_expense):    #enumrate use to print value with index number
                print(f"  {i+1}. {category_name}")

            cat_range = f"[1 - {len(category_expense)}]"
            try:
                index = int(input(f"Enter a category {cat_range} : ")) - 1
                if index in range(len(category_expense)):
                    selected_category = category_expense[index]
                    new_expense = Expense(
                        name=name_expense,
                        category=selected_category,
                        amount=amount_expense
                    )
                    return new_expense
                else:
                    print("❌ Invalid category. Please enter a number within the valid range.")
            except ValueError:
                print("❌ Please enter a valid number.")
    except Exception as e:
        print(f"Error in user_expense: {e}")







def saving_to_file(expense: Expense, expense_file_path):
    try:
        print(f"Saving you {expense} to {expense_file_path} ")
        with open(expense_file_path, "a", encoding="utf-8") as file:
            file.write(f"{expense.name},{expense.amount},{expense.category},{datetime.today().strftime('%Y-%m-%d')}\n")
    except Exception as e:
        print(f"Error saving to file: {e}")







def getting_expense(expense_file_path, budget):
    try:
        expenses: list[Expense] = []
        with open(expense_file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    name_expense, amount_expense, category_expense, date_expense = parts
                    try:
                        line_expenses = Expense(
                            name=name_expense,
                            amount=float(amount_expense),
                            category=category_expense
                        )
                        line_expenses.date = date_expense
                        expenses.append(line_expenses)
                    except ValueError:
                        print(f"Skipping invalid expense entry: {line.strip()}")
                    except Exception as e:
                        print(f"Error creating Expense object: {e}")

        for e in expenses:
            print(f"{e.name} - {e.amount} - {e.category}")





        amount_by_category = {}
        for exp in expenses:
            key = exp.category
            if key in amount_by_category:
                amount_by_category[key] += exp.amount
            else:
                amount_by_category[key] = exp.amount



        print("\n📊 Total Amount by Category:")
        for category, total in amount_by_category.items():
            print(f"{category}: 💲{total}")



        total_spent = sum([x.amount for x in expenses])
        print(f"You spent total 💲{total_spent}:.. this month ")

        remaining_budget = budget - total_spent
        print(f"Your ramaining budget is 💲{remaining_budget}:.. this month ")





        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        weekly_expenses = [
            e for e in expenses
            if hasattr(e, "date") and start_of_week <= datetime.strptime(e.date, "%Y-%m-%d") <= end_of_week
        ]

        total_weekly_spent = sum([
        e.amount for e in expenses
         if hasattr(e, "date") and datetime.strptime(e.date, "%Y-%m-%d") <= today
         ])

        weeks_passed = (today.day - 1) // 7 + 1
        weekly_budget = budget / 4 
        used_budget_till_now = weekly_budget * weeks_passed
        remaining_weekly_budget = used_budget_till_now - total_weekly_spent

        print(f"Your remaining weekly budget is 💲{remaining_weekly_budget}")


    except FileNotFoundError:
        print("❌ Expense file not found. Please ensure the file exists.")
    except Exception as e:
        print(f"Error in getting_expense: {e}")



if __name__ == "__main__":     # in future if i make this file the part of another project to avoid running main directly using this main should only run when i run this file only
    main()
