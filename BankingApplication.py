class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = {"name": name, "balance": balance}
            print("Account created successfully.")
        else:
            print("Account with this account number already exists.")

    def display_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]["balance"]
            print(f"Account Balance for {self.accounts[account_number]['name']}: ${balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            print("Deposit successful.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")


bank = Bank()

while True:
    print("\n1. Create Account\n2. Display Balance\n3. Deposit\n4. Withdraw\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        account_number = input("Enter account number: ")
        name = input("Enter account holder's name: ")
        bank.create_account(account_number, name)

    elif choice == "2":
        account_number = input("Enter account number: ")
        bank.display_balance(account_number)

    elif choice == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        bank.deposit(account_number, amount)

    elif choice == "4":
        account_number = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        bank.withdraw(account_number, amount)

    elif choice == "5":
        print("Exiting the banking application. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
