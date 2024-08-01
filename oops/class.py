import datetime

today = datetime.date.today()
year = today.year

class Company:
    area = "SIPCOT, SIRUSERI"
    __city = "chennai"
    
    def __init__(self, cname):
        self.cname = cname
    
    def displayCname(self):
        print("Company Name:", self.cname)
    
    def address(self):
        return self.area + ", " + self.__city + ", TamilNadu"

class Employee:
    empcount = 0
    isMarried = False
    
    def __init__(self, fname, lname, yob):
        self.fname = fname
        self.lname = lname
        self.age = year - yob
        Employee.empcount += 1
        self.id = Employee.empcount
    
    def getEmpDetails(self):
        print("Employee ID:", self.id)
        print("Full Name:", self.fname, self.lname)
        print("Age:", self.age, "years")
        print("Marital Status:", self.isMarried)

c1 = Company("Changepond Technologies")
c1.displayCname()
# c1.__city cannot be changed directly as it's a private attribute
print("Address:", c1.address())

print("," * 70)

e1 = Employee("Parag", "Joshi", 1980)
e1.isMarried = True
e1.getEmpDetails()

print("*" * 70)
