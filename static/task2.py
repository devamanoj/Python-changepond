class Bank:
    initial_amount = 1000

    @staticmethod
    def display_kyc_info():
        print("1. Submit Aadhar form \n2. Two passport size photos")

    @staticmethod
    def withdraw(amount):
        Bank.initial_amount -= amount
        print(f"Withdrawn {amount}. Current balance: {Bank.initial_amount}")

    @staticmethod
    def deposit(amount):
        Bank.initial_amount += amount
        print(f"Deposited {amount}. Current balance: {Bank.initial_amount}")

# Display KYC information
Bank.display_kyc_info()

# Perform banking operations
Bank.withdraw(300)
Bank.deposit(500)
