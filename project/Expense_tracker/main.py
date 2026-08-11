expences=[]
this_expence = {}
choice = 1
total_expence = 0

while True:

    print("1. Add Expence")
    print("2. Show Expence")
    print("3. Exit")
    print(f"\nTotal: {total_expence}$\n")
    choice = input("Enter choice: ")

    match choice:
        case "1":
            date = input("Enter date: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))

            total_expence += amount

            this_expence = {"date" : date, 
                            "category" : category, 
                            "description" : description, 
                            "amount" : amount
                            }
            expences.append(this_expence)
        case "2":
            for expence in expences:
                print(f"\n\nDate: {expence["date"]}\nCategory: {expence["category"]}\nDescription: {expence["description"]}\nAmount: {expence["amount"]}$\n\n")

        case "3":
            break

        case _ :
            print("Unvalid selection!!")