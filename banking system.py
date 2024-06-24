class BankAccount:
    def __init__(self, account_number, password):
        self.account_number = account_number
        self.password = password
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance is {self.balance}."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance is {self.balance}."
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def get_balance(self):
        return f"Current balance is {self.balance}."


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, password):
        if account_number in self.accounts:
            return "Account already exists."
        else:
            self.accounts[account_number] = BankAccount(account_number, password)
            return "Account created successfully."

    def login(self, account_number, password):
        account = self.accounts.get(account_number)
        if account and account.password == password:
            return account
        else:
            return "Invalid account number or password."

def main():
    bank = BankingSystem()

    while True:
        print("\nWelcome to the Banking System")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter a new account number: ")
            password = input("Enter a new password: ")
            print(bank.create_account(account_number, password))

        elif choice == "2":
            account_number = input("Enter your account number: ")
            password = input("Enter your password: ")
            account = bank.login(account_number, password)

            if isinstance(account, BankAccount):
                print("Login successful.")
                while True:
                    print("\n1. Deposit Amount")
                    print("2. Withdraw Amount")
                    print("3. Check Balance")
                    print("4. Logout")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == "1":
                        amount = float(input("Enter amount to deposit: "))
                        print(account.deposit(amount))

                    elif sub_choice == "2":
                        amount = float(input("Enter amount to withdraw: "))
                        print(account.withdraw(amount))

                    elif sub_choice == "3":
                        print(account.get_balance())

                    elif sub_choice == "4":
                        print("Logged out.")
                        break

                    else:
                        print("Invalid choice. Please try again.")
            else:
                print(account)

        elif choice == "3":
            print("Thank you for using the Banking System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
