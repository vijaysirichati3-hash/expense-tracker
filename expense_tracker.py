import csv
import os

FILE_NAME = "expenses.csv"


def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: ₹"))

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Category", "Description", "Amount"])

        writer.writerow([date, category, description, amount])

    print("\n✅ Expense added successfully!\n")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.\n")
        return

    total = 0

    print("\n------ EXPENSES ------")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(
                f"{row['Date']} | "
                f"{row['Category']} | "
                f"{row['Description']} | "
                f"₹{row['Amount']}"
            )

            total += float(row["Amount"])

    print("----------------------")
    print(f"Total Expense: ₹{total:.2f}\n")


def main():
    while True:
        print("===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("❌ Invalid option. Try again.\n")


main()
