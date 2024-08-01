class Salary:
        def __init__(self,salary):
            self.basic_salary =salary

        def getsalary(self):
            print("basic salary: ",self.basic_salary )
class Allowance(Salary):
    def calculate(self):
        self.HRA = (self.basic_salary/100)*20
        self.DA = (self.basic_salary/100)*40
        self.TA = (self.basic_salary/100)*25
    def getallocation(self):
        self.TOTAL = self.HRA+ self.DA + self.TA
            # print("Total allocation: ",self.TOTAL)
class Dedection(Salary):
    def dedection(self):
        self.insurance = 5000
        self.pf = (self.basic_salary/100)*12
        self.grati = (self.basic_salary/100)*5
        self.Totaldedection = self.insurance + self.pf + self.grati
    
class CalculateSalarySlip(Allowance,Dedection):
    def get_salary_slip(self):
        Allowance.calculate(self)
        Allowance.getallocation(self)
        Dedection.dedection(self)
        print("=" *50)
        print("Base Salary: ", self.basic_salary)
        print("=" * 50)
        print("total allocation: ", self.TOTAL)
        print("=" * 50)
        print("Total Dedection: ", self.Totaldedection)
        print("=" * 50)
        print("Gross Salary: ", self.basic_salary + self.TOTAL)
        self.final_output = self.basic_salary + self.TOTAL
        print("=" * 50)
        print("Net Salary: ", self.final_output - self.Totaldedection)
        print("=" * 70)
ob = CalculateSalarySlip(int(input("Enter the salary: ")))
ob.get_salary_slip()