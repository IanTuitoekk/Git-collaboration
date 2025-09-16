def calculate_nssf(gross_salary):
	#nssf deductions.
	tier1_nssf = 8000
	tier2_nssf = 72000
	#tire one - 6% of 8000
	tier1 = min(gross_salary, tier1_nssf) * 0.06
	#tirer two
	tier2 = 0 
	if gross_salary > tier1_nssf:
		tier2 = (min(gross_salary, tier2_nssf) - tier1_nssf) * 0.06
	total_nssf = tier1 + tier2
	return total_nssf
def calculate_shif(gross_salary):
	#calculate shif
	return gross_salary * 0.0275
totalDeductions = calculate_nssf(25000) + calculate_shif(25000)
print(totalDeductions)