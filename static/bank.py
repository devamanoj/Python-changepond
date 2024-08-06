# Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That Class Contains one class variable as ROI which is initialize to 10.5
# Inside init method initialize all name and amount variable by accepting the values from user.
# There are four instance methods inside class as Display() , Deposit (), Withdraw( ), CalculateInterest()
# Deposit( ) method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateInterst() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI
# And Display () method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects
class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter the account holder's name: ")
        self.Amount = float(input("Enter the initial amount: "))

    def Display(self):
        print(f"Account Holder: {self.Name}")
        print(f"Current Amount: {self.Amount}")

    def Deposit(self):
        deposit_amount = float(input("Enter the amount to deposit: "))
        self.Amount += deposit_amount
        print(f"{deposit_amount} has been deposited.")

    def Withdraw(self):
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount > self.Amount:
            print("Insufficient balance.")
        else:
            self.Amount -= withdraw_amount
            print(f"{withdraw_amount} has been withdrawn.")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest calculated at {BankAccount.ROI}% ROI: {interest}")
    @staticmethod
    def displaykycinfo():
        print("1.submit adhar form \n 2.two passport size photo")


# Creating multiple objects and calling instance methods
account1 = BankAccount()
account1.Display()
account1.Deposit()
account1.Display()
account1.Withdraw()
account1.Display()
account1.CalculateInterest()
BankAccount.displaykycinfo()

print()  

account2 = BankAccount()
account2.Display()
account2.Deposit()
account2.Display()
account2.Withdraw()
account2.Display()
account2.CalculateInterest()
BankAccount.displaykycinfo()
