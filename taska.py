class Payroll:
    # This runs when we create a Payroll object
    def __init__(self, basic_salary, benefits):
        # Store the basic salary in the object so we can use it later
        self.basic_salary = basic_salary
        # Store the benefits in the object for later use
        self.benefits = benefits
        # Add them to get gross salary
        self.gross_salary = self.basic_salary + self.benefits
