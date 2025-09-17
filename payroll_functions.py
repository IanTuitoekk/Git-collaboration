#Jerolina
def main():
	# Get user input.
	basic_salary = float(input("Enter basic salary: "))
	benefits = float(input("Enter benefits amount: "))
	# Do the calculations.
	gross_salary = basic_salary + benefits
	# Display.
	display(gross_salary, calculate_paye(gross_salary), calculate_nssf(gross_salary), calculate_shif(gross_salary), calculate_housing_levy(gross_salary), calculate_net_salary(gross_salary))

# Karen.
def calculate_paye(gross_salary): # calculate paye.
	taxable_income = gross_salary - calculate_nssf(gross_salary) ## Subtracting NSSF to get taxable income
	if taxable_income <= 24000:  # Bracket one - 10%
		tax = taxable_income * 0.10
	elif 24000 < taxable_income <= 32333:  # Bracket two - 10% 25%
		tax = ((24000 * 0.10) + ((taxable_income - 24000) * 0.25))
	elif 32333 < taxable_income <= 500000:  # Bracket three - 10% 25% 30%
		tax = (24000 * 0.10) + (8333 * 0.25) + ((taxable_income - 32333) * 0.30)
	elif 500000 < taxable_income <= 800000:  # Bracket four - 10% 25% 30% 32%
		tax = (24000 * 0.10) + (8333 * 0.25) + (467667 * 0.30) +((taxable_income - 500000) * 0.32)
	else: # Above our brackets - 10% 25% 30% 32% 35%
		tax = (24000 * 0.10) + (8333 * 0.25) + (467667 * 0.30) + (300000 * 0.32) + ((taxable_income - 800000) * 0.35)
	return tax

# James.
def calculate_nssf(gross_salary): # return nssf deductions
	tier1_nssf = 8000
	tier2_nssf = 72000
	tier1 = min(gross_salary, tier1_nssf) * 0.06 # tier one 
	#tier two.
	tier2 = 0 
	if gross_salary > tier1_nssf:
		tier2 = (min(gross_salary, tier2_nssf) - tier1_nssf) * 0.06
	total_nssf_deductions = tier1 + tier2
	return total_nssf_deductions

def calculate_shif(gross_salary): # return shif deduction.
	return gross_salary * 0.0275

def calculate_housing_levy(gross_salary): # return housing levy deduction.
	house_levy = gross_salary * 0.015
	return house_levy

def calculate_net_salary(gross_salary): # return the net salary.
	net_salary = gross_salary - (calculate_paye(gross_salary) + calculate_nssf(gross_salary) + calculate_shif(gross_salary) + calculate_housing_levy(gross_salary))
	return net_salary

# Ian. 
def display(gross_salary, paye, nssf, shif, housing_levy, net_salary): # Function to display output.
	print("\n\tTaxable Salary")
	print(f"gross salary : {gross_salary:.2f}")
	print(f"\n\tDeductions")
	print(f"paye : {paye:.2f}")
	print(f"nssf : {nssf:.2f}")
	print(f"shif : {shif:.2f}")
	print(f"housing levy : {housing_levy:.2f}")
	print(f"\n\tNet Income and Deductions")
	print(f"net salary : {net_salary:.2f}")
	print(f"total deductions : {paye + nssf + shif + housing_levy:.2f}")

main() # entry point.
