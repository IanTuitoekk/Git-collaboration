from abc import ABC, abstractmethod
class Payroll(ABC): 
    def __init__(self, basic_salary, benefits): # initialized our attributes (basic_salary and benefits)
        self.basic_salary = basic_salary
        self.benefits = benefits
        self.gross_salary = self.basic_salary + self.benefits

    @abstractmethod
    def calculate_bonuses(self):
        pass

    def calculate_paye(self):  # calculate paye.
        taxable_income = self.gross_salary - self.calculate_nssf()  # Subtracting NSSF to get taxable income -- not sure really.
        if taxable_income <= 24000:  # Bracket one - 10%
            tax = taxable_income * 0.10
        elif 24000 < taxable_income <= 32333:  # Bracket two - 10% 25%
            tax = ((24000 * 0.10) + ((taxable_income - 24000) * 0.25))
        elif 32333 < taxable_income <= 500000:  # Bracket three - 10% 25% 30%
            tax = (24000 * 0.10) + (8333 * 0.25) + ((taxable_income - 32333) * 0.30)
        elif 500000 < taxable_income <= 800000:  # Bracket four - 10% 25% 30% 32%
            tax = (24000 * 0.10) + (8333 * 0.25) + (467667 * 0.30) + ((taxable_income - 500000) * 0.32)
        else:  # Above our brackets - 10% 25% 30% 32% 35%
            tax = (24000 * 0.10) + (8333 * 0.25) + (467667 * 0.30) + (300000 * 0.32) + ((taxable_income - 800000) * 0.35)
        return tax

    def calculate_nssf(self): # calculate nssf deductions.
        tier1_nssf_rate = 8000
        tier2_nssf_rate = 72000
        tier1 = min(self.gross_salary, tier1_nssf_rate) * 0.06  # tier one rate

        # tier two rate.
        tier2 = 0
        if self.gross_salary > tier1_nssf_rate:
            tier2 = (min(self.gross_salary, tier2_nssf_rate) - tier1_nssf_rate) * 0.06
        total_nssf_deductions = tier1 + tier2
        return total_nssf_deductions

    def calculate_shif(self):  # return shif deduction.
        return self.gross_salary * 0.0275

    def calculate_housing_levy(self):  # return housing levy deduction.
        house_levy = self.gross_salary * 0.015
        return house_levy

    def calculate_net_salary(self):  # return the net salary.
        deductions = self.calculate_paye() + self.calculate_nssf() + self.calculate_shif() + self.calculate_housing_levy()
        net_salary = self.gross_salary - deductions + getattr(self, "bonus", 0)
        return net_salary

    def display(self):  # method to display output.
        paye = self.calculate_paye()
        nssf = self.calculate_nssf()
        shif = self.calculate_shif()
        housing_levy = self.calculate_housing_levy()
        net_salary = self.calculate_net_salary()
        print(f"gross salary : {self.gross_salary:.2f}")
        print(f"\n\tDeductions")
        print(f"paye : {paye:.2f}")
        print(f"nssf : {nssf:.2f}")
        print(f"shif : {shif:.2f}")
        print(f"housing levy : {housing_levy:.2f}")
        print(f"\n\tNet Income and Deductions")
        print(f"net salary : {net_salary:.2f}")
        print(f"total deductions : {paye + nssf + shif + housing_levy:.2f}")
class Driver(Payroll): # driver class.
    def __init__(self, basic_salary, benefits, kilometers):
        super().__init__(basic_salary, benefits)
        self.kilometers = kilometers
        self.bonus = self.calculate_bonuses()

    def calculate_bonuses(self): # plus 0.01% of basic.
        return (self.basic_salary * 0.001) * self.kilometers

    def display(self):
        print("\tDrivers Payroll Details:")
        super().display()
        print(f"bonus : {self.bonus:.2f}")

class Loader(Payroll): # loader class.
    def __init__(self, basic_salary, benefits, kilometers):
        super().__init__(basic_salary, benefits)
        self.kilometers = kilometers
        self.bonus = self.calculate_bonuses()
    
    def calculate_bonuses(self): # plus 0.5% of basic.
        return (self.basic_salary * 0.002) * self.kilometers

    def display(self):
        print("\tLoader Payroll Details:")
        super().display()
        print(f"bonus : {self.bonus:.2f}")

# get input -- basic salary and benefits.
basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter benefits amount: "))
kilometers = float(input("Enter kilometers travelled: "))
employee_type =  input("Enter the employee type: ").strip().lower()

# check for non-negative values.
if basic_salary < 0 or benefits < 0 or kilometers < 0:
    print("basic salary, benefits and kilometers must be non-negative")
    exit()
# Initialize class.
if employee_type == "driver":
    employee = Driver(basic_salary, benefits, kilometers)
elif employee_type == "loader":
    employee = Loader(basic_salary, benefits, kilometers)
else:
    print("enter a valid employee.")
    exit()

# display output.
employee.display()