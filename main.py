#Jes
def main():
	# Get user input
	basic_salary = float(input("Enter basic salary: "))
	benefits = float(input("Enter benefits: "))
	
	gross_salary = basic_salary + benefits
	payee = calculate_payee(gross_salary)
	nssf = calculate_nssf(gross_salary)
	shif = calculate_shif(gross_salary)
	house_levy = calculate_house_levy(gross_salary)
	net_salary = calculate_net_salary(gross_salary, payee, nssf, shif, house_levy)
	# Display
	print(f"\nGross salary: {gross_salary:.2f}")
	print(f"\nPayee deduction: {payee:.2f}")
	print(f"\nNssf deductions: {nssf:.2f}")
	print(f"\nShif deductions: {shif:.2f}")
	print(f"\nHousing levy deduction: {house_levy:.2f}")
	print(f"\nNet salary: {net_salary:.2f}")
	
#Karen	
def calculate_payee(gross_salary):
    """
    Calculating PAYE based on KRA brackets.
    Uses gross salary minus NSSF as taxable income.
    """
    # Subtracting NSSF to get taxable income
    taxable_income = gross_salary - calculate_nssf(gross_salary)#nssf
    
    # KRA brackets
    if taxable_income <= 24000:
        tax = taxable_income * 0.10
    elif taxable_income <= 32333:
        # 24,000 taxed at 10% + the rest at 25%
        tax = (24000 * 0.10) + ((taxable_income - 24000) * 0.25)
    else:
        # 24,000 @10% + 8,333 @25% + the rest @30%
        tax = (24000 * 0.10) + (8333 * 0.25) + ((taxable_income - 32333) * 0.30)
    
    return tax

#James
def calculate_nssf(gross_salary):#nssf deductions
	tier1_nssf = 8000
	tier2_nssf = 72000
	tier1 = min(gross_salary, tier1_nssf) * 0.06#tier one 
	#tier two
	tier2 = 0 
	if gross_salary > tier1_nssf:
		tier2 = (min(gross_salary, tier2_nssf) - tier1_nssf) * 0.06
	total_nssf = tier1 + tier2
	return total_nssf

def calculate_shif(gross_salary):#calculate shif
	return gross_salary * 0.0275

def calculate_house_levy(gross_salary):#calculate housing levy
	house_levy = gross_salary * 0.015
	return house_levy

def calculate_net_salary(gross_salary, payee, nssf, shif, house_levy):#calculate net salary
	net_salary = gross_salary - (payee + nssf + shif + house_levy)
	return net_salary
main()