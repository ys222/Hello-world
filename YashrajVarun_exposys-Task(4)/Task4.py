##2) Declare a class Bank, write methods for deposit , withdrawal and information of customer

# BankAccount class
class Bankaccount:
    def __init__(self):
        def deposit(self):
            amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)
        def withdraw(self):
            amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
            def display(self):
                print("\n Net Available Balance =", self.balance)
                class Bank_Account:
                      def __init__(self):
                          self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Net Available Balance=",self.balance)
        s = Bank_Account()
        print(s.deposit())
        print(s.withdraw())
        print(s.display())
