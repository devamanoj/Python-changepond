#instance variable:name,amount,address,accountno
# instance method: createaccount(),displayaccountinfo()
#class variable:bank
#class method :displaybankinformation
class Bank:
    Bankname = "cholabank"
    roi_on_fd = 2.0
    def __init__(self):
        self.name=""
        self.amount=0
        self.address=""
        self.accountno=0
    def createaccount(self):
        self.name = input('Enter your name:')
        self.amount = int(input("Enter your initial amount:"))
        self.address = input("Enter your address:")
        self.accountno = int(input('Enter your accountno:'))
    def displayaccountinfo(self):
        print('--------------your account information below-----------')
        print('Name of the account holder:',self.name)
        print('Account Number:',self.accountno)
        print('address:',self.address)
        print('amount:',self.amount)
    def displaybankinformation(cls):
        print('displaybankname:',cls.Bankname)
Bank.display = classmethod(Bank.displaybankinformation)
Bank.display()
# def main():
user1 = Bank()
user1.createaccount()
user1.displayaccountinfo()
print('bank:',user1.Bankname)
print('rate of interest:',user1.roi_on_fd)

# if __name__ == '__main__':
#     main()
