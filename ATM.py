# Submitted By Aniket Sominath Thale (Batch 11)
# Task 1: ATM simulator
'''Create a program that simulates the all atm
functionalities and operations (Check balance,
Deposit, Withdraw)'''
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"₹{amount} deposited successfully."
        else:
            return "Invalid amount. Deposit failed."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"₹{amount} withdrawn successfully."
        elif amount > self.balance:
            return "Insufficient funds. Withdrawal failed."
        else:
            return "Invalid amount. Withdrawal failed."

def main():
    print("Welcome to the ATM Simulator!")
    initial_balance = float(input("Enter your initial account balance: "))
    atm = ATM(initial_balance)

    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            balance = atm.check_balance()
            print(f"Your account balance is ₹{balance:.2f}")
        elif choice == "2":
            amount = float(input("Enter the amount to deposit: "))
            result = atm.deposit(amount)
            print(result)
        elif choice == "3":
            amount = float(input("Enter the amount to withdraw: "))
            result = atm.withdraw(amount)
            print(result)
        elif choice == "4":
            print("Thank you for using the ATM Simulator!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
