class BasicSalary:
    def __init__(self, salary):
        self.basic_salary = salary

    def display_salary(self):
        print("Base Salary: ", self.basic_salary)
class Allowance(BasicSalary):
    def calculate_allowances(self):
        self.hra = (self.basic_salary / 100) * 20  # House Rent Allowance
        self.da = (self.basic_salary / 100) * 40  # Dearness Allowance
        self.ta = (self.basic_salary / 100) * 25  # Travel Allowance
        self.total_allowance = self.hra + self.da + self.ta
class Deduction(BasicSalary):
    def calculate_deductions(self):
        self.insurance = 5000
        self.pf = (self.basic_salary / 100) * 12  # Provident Fund
        self.gratuity = (self.basic_salary / 100) * 5  # Gratuity
        self.total_deduction = self.insurance + self.pf + self.gratuity
class SalarySlip(Allowance, Deduction):
    def generate_salary_slip(self):
        self.calculate_allowances()
        self.calculate_deductions()
        
        print("=" * 50)
        print("Base Salary: ", self.basic_salary)
        print("=" * 50)
        print("Total Allowances: ", self.total_allowance)
        print("=" * 50)
        print("Total Deductions: ", self.total_deduction)
        print("=" * 50)
        
        gross_salary = self.basic_salary + self.total_allowance
        print("Gross Salary: ", gross_salary)
        
        net_salary = gross_salary - self.total_deduction
        print("=" * 50)
        print("Net Salary: ", net_salary)
        print("=" * 70)
salary_input = int(input("Enter the  salary: "))
employee_salary_slip = SalarySlip(salary_input)
employee_salary_slip.generate_salary_slip()
