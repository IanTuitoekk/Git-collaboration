def main():
	# Get user input
	basic_salary = float(input("Enter basic salary: "))
	benefits = float(input("Enter benefits: "))
	# Calculate Gross Salary
	gross_salary = basic_salary + benefits
	payee = calculate_payee(gross_salary)
	nssf = calculate_nssf(gross_salary)
	shif = calculate_shif(gross_salary)
	house_levy = calculate_house_levy(gross_salary)
	net_salary = calculate_net_salary(gross_salary, payee, nssf, shif, house_levy)
	# Display gross salary
	print(f"\nGross Salary: {gross_salary:.2f}")
	print(f"\nPayee: {payee:.2f}")
	print(f"\nNssf deductions: {nssf:.2f}")
	print(f"\nShif deductions: {shif:.2f}")
	print(f"\nHousing levy: {house_levy:.2f}")
	print(f"\nNet income: {net_salary:.2f}")