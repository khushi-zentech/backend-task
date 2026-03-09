from controller.atm_controller import ATMController
from controller.transaction_controller import TransactionController
from model.database import DatabaseConnection

def menu():
    '''This view interact with user'''
    
    db = DatabaseConnection()

    atm_controller = ATMController(db)
    transaction_controller = TransactionController(db)

    print("\nWelcome to ATM System!")
    while True:
        print("\n1. Login")
        print("2. Exit")

        try:
            choice = int(input("\nEnter choice: "))

            if choice == 1:
                user_name = input("Enter User Name: ")

                db.cursor.execute("SELECT * FROM users WHERE user_name=%s", (user_name,))
                user = db.cursor.fetchone()

                if not user:
                    bank = input("Enter Bank Name: ")
                    atm = input("Enter ATM Name (Bank-ATM): ")

                    result = atm_controller.insert_user(user_name, bank, atm)

                    print(result.get("message"))
                    print("\nPlease login again.")

                    continue

                card = input("Enter Card: ")
                pin = input("Enter PIN: ")

                print(f"\nWelcome {user_name}!")

                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Display Details")
                    print("4. Change PIN")
                    print("5. Logout")

                    try:
                        user_choice = int(input("\nEnter choice: "))

                        if user_choice == 1:
                            atm_name = input("\nEnter ATM (Bank-ATM) Name or Quit to this Operation: ")
                            
                            if atm_name.lower() == "quit":
                                continue

                            try:
                                amount = input("Enter Amount or Quit to this Operation: ")
                                
                                if amount.lower() == "quit":
                                    continue
                                
                                amount = float(amount)
                            except ValueError:
                                print("\nInvalid amount!")
                                continue

                            result = transaction_controller.deposit(card, pin, atm_name, amount)
                            print(result.get("message"))
                        elif user_choice == 2:
                            atm_name = input("\nEnter ATM (Bank-ATM) Name or Quit to this Operation: ")
                            
                            if atm_name.lower() == "quit":
                                continue

                            try:
                                amount = input("Enter Amount or Quit to this Operation: ")
                                
                                if amount.lower() == "quit":
                                    continue
                                
                                amount = float(amount)
                            except ValueError:
                                print("\nInvalid amount!")
                                continue

                            result = transaction_controller.withdraw(card, pin, atm_name, amount)
                            print(result.get("message"))
                        elif user_choice == 3:
                            result: dict = transaction_controller.display_details(user_name)
                            print(result.get("message"))
                        elif user_choice == 4:
                            new_pin = input("\nEnter New PIN: ")

                            result = transaction_controller.update_pin(card, new_pin)
                            print(result.get("message"))
                        elif user_choice == 5:
                            print("\nLogged out Successfully.")
                            break
                        else:
                            print("\nPlease Enter a valid choice (1-5).")
                    except ValueError:
                        print("\nEnter valid input!")
            elif choice == 2:
                print("\nYou selected Exit.\nThank you!")
                db.close_connection()
                break
            else:
                print("\nPlease Enter a valid choice (1-2).")
        except ValueError:
            print("\nEnter valid input!")

menu() # start ATM System from here