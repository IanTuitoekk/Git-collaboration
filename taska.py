class Payroll:
    # This is the constructor method. It runs automatically when we create a Payroll object.
    # It takes basic_salary and benefits as input from the user or program.
    def __init__(self, basic_salary, benefits):
        # Store the basic salary in the object so we can use it later
        self.basic_salary = basic_salary
        # Store the benefits in the object for later use
        self.benefits = benefits
        # Calculate gross salary as the sum of basic salary and benefits
        self.gross_salary = self.basic_salary + self.benefits
