import random
import string
from datetime import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, password, balance=0, date_of_opening=None):
        self.account_number = account_number
        self.customer_name = customer_name
        self.password = password
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}.\nNew balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}.\nNew balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance is {self.balance}.")

    def account_details(self):
        print("Account Details:")
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: {self.balance}")
        print(f"Date of Opening: {self.date_of_opening}")
        print("----------------------")

def generate_account_number():
    return '290' + ''.join(random.choices(string.digits, k=9))

def generate_password():
    return ''.join(random.choices(string.digits, k=5))

def main():
    accounts = {}

    while True:
        print("\n\n-------------------------------------------------------\n")
        print("\tWELCOME TO FORTUNE INTERNATIONAL BANK UGANDA")
        print("Banking Operation")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Statement")
        print("5. Check Balance")
        print("6. Account Details")
        print("7. Exit")
        print("-------------------------------------------------------------")

        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            customer_name = input("\n\nEnter customer name: ")
            date_of_opening = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            account_number = generate_account_number()
            password = generate_password()
            accounts[account_number] = BankAccount(account_number, customer_name, password, date_of_opening=date_of_opening)
            print("Account created successfully.")
            print(f"Account Number: {account_number}")
            print(f"Password: {password}")
            print(f"Date of Opening: {date_of_opening}\n\n")

        elif choice == 2: 
            account_number = input("Enter account number: ")
            if account_number in accounts:
                password = input("Enter password: ")
                if accounts[account_number].password == password:
                    amount = float(input("Enter amount to deposit: "))
                    accounts[account_number].deposit(amount)
                else:
                    print("Incorrect password.")
            else:
                print("Account not found.")

        elif choice == 3:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                password = input("Enter password: ")
                if accounts[account_number].password == password:
                    amount = float(input("Enter amount to withdraw: "))
                    accounts[account_number].withdraw(amount)
                else:
                    print("Incorrect password.")
            else:
                print("Account not found.")

        elif choice == 4:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                password = input("Enter password: ")
                if accounts[account_number].password == password:
                    accounts[account_number].account_details()
                else:
                    print("Incorrect password.")
            else:
                print("Account not found.")

        elif choice == 5:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                password = input("Enter password: ")
                if accounts[account_number].password == password:
                    accounts[account_number].check_balance()
                else:
                    print("Incorrect password.")
            else:
                print("Account not found.")

        elif choice == 6:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                password = input("Enter password: ")
                if accounts[account_number].password == password:
                    accounts[account_number].account_details()
                else:
                    print("Incorrect password.")
            else:
                print("Account not found.")

        elif choice == 7:
            print("Exiting the banking system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()