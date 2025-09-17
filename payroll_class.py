class Payroll: 
    def __init__(self, basic_salary, benefits): # initilized our aatribuites (basic_salary and benefits)
        self.basic_salary = basic_salary
        self.benefits = benefits
        self. gross_salary = basic_salary + benefits

    def calculate_paye(self):  # calculate paye.
        taxable_income = self.gross_salary - self.calculate_deductions()  ## Subtracting NSSF to get taxable income -- not sure really.
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
        tier1_nssf = 8000
        tier2_nssf = 72000
        tier1 = min(self.gross_salary, tier1_nssf) * 0.06  # tier one deductions

        # tier two.
        tier2 = 0
        if self.gross_salary > tier1_nssf:
            tier2 = (min(self. gross_salary, tier2_nssf) - tier1_nssf) * 0.06
        total_nssf_deductions = tier1 + tier2
        return total_nssf_deductions

    def calculate_shif(self):  # return shif deduction.
        return self.gross_salary * 0.0275

    def calculate_housing_levy(self):  # return housing levy deduction.
        house_levy = self.gross_salary * 0.015
        return house_levy

    def calculate_net_salary(self):  # return the net salary.
        net_salary = self.gross_salary - (self.calculate_paye() + self.calculate_nssf() + self.calculate_shif() + self.calculate_housing_levy())
        return net_salary

    def display(self, paye, nssf, shif, housing_levy, net_salary):  # method to display output.
        print("\n\tTaxable Salary")
        print(f"gross salary : {self.gross_salary:.2f}")
        print(f"\n\tDeductions")
        print(f"paye : {paye:.2f}")
        print(f"nssf : {nssf:.2f}")
        print(f"shif : {shif:.2f}")
        print(f"housing levy : {housing_levy:.2f}")
        print(f"\n\tNet Income and Deductions")
        print(f"net salary : {net_salary:.2f}")
        print(f"total deductions : {paye + nssf + shif + housing_levy:.2f}")
# get input
basic_salary = float(input("Enter basic salary: "))
benefits = float(input("Enter benefits amount: "))
# create instance of payroll class
employee = Payroll(basic_salary, benefits)
employee.display(employee.calculate_paye(), employee.calculate_nssf(), employee.calculate_shif(), employee.calculate_housing_levy(),employee.calculate_net_salary())

