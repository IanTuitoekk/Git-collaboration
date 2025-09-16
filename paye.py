def calculate_payee(self):
    """
    Calculating PAYE based on KRA brackets.
    Uses gross salary minus NSSF as taxable income.
    """
    # Subtracting NSSF to get taxable income
    taxable_income = self.gross_salary - self.calculate_nssf()
    
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
