<<<<<<< HEAD

# expenses = {"ticket des bus":"4.000 dt","déj":"3.500dt"}
expenses = []
def add_expense():
  description = input("Description : ")
  amount = float(input("Montant : "))
  expenses.append({"description": description,"amount": amount})
  print("Depense ajoutee !")


def show_expenses():
   if not expenses:
     print("Aucune depense enregistree.")
     return
   for number, expense in enumerate(expenses, start=1):
     print(f"{number}. {expense['description']} - "
     f"{expense['amount']:.2f}")

def show_total():
   total = sum(item["amount"] for item in expenses)
   print(f"Total : {total:.2f}")
   
def show_average():
   if not expenses:
      print("No expenses recorded.")
   return
total = sum(item["amount"] for item in expenses)
average = total / len(expenses)
print(f"Average expense: {average:.2f}")

def main():
   while True:
      print("\n===== SUIVI DES DEPENSES =====")
      print("1. Ajouter une depense")
      print("2. Afficher les depenses")
      print("3. Afficher le total")
      print("4. Quitter")
      print("5. Show average")
      choice = input("Votre choix : ")
      if choice == "1":
         add_expense()
      elif choice == "2":
         show_expenses()
      elif choice == "3":
         show_total()
      elif choice == "4":
         print("Au revoir !")
         break
      elif choice == "5":
         show_average()
      
      else:
        print("Choix invalide.")
if __name__ == "__main__":
 main()

=======
expenses = []

def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    expenses.append({"description": description, "amount": amount})
    print("Expense added successfully.")

def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - ${expense['amount']:.2f}")

def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total expenses: ${total:.2f}")


def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f" {number}. {expense['description']}")
    choice = input("Expense number to delete: ")
    if not choice.isdigit():
        print("Invalid expense number.")
        return
    index = int(choice) - 1
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Deleted: {removed['description']}")
    else:
        print("Invalid expense number.")

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Exit")
        print("5. Delete an expense") 
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Goodbye!")
            break
        elif choice == "5":
            delete_expense()  
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
>>>>>>> main
