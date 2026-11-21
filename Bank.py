# class Bank:
#     def __init__(self, acc_no, name, balance, acc_type):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance
#         self.acc_type = acc_type
#
#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient balance")
#
#     def display(self):
#         print("Account No:", self.acc_no)
#         print("Name:", self.name)
#         print("Account Type:", self.acc_type)
#         print("Balance:", self.balance)
#
#
# b = Bank(101, "John", 5000, "Savings")
#
# b.display()
# b.deposit(1000)
# b.withdraw(2000)
# b.display()
class BankAccount:
    def __init__(self, acc_no, name, balance, acc_type):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.acc_type = acc_type

    def display(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance:", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
            print("Current Balance:", self.balance)
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
            print("Current Balance:", self.balance)
        else:
            print("Insufficient Balance!")


# Creating Bank Account
acc = BankAccount(1001, "John", 5000, "Savings")

while True:
    print("\n===== BANK MENU =====")
    print("1. Display Account Details")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        acc.display()

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        acc.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        acc.withdraw(amount)

    elif choice == 4:
        print("Current Balance:", acc.balance)

    elif choice == 5:
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Please try again.")
