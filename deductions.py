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