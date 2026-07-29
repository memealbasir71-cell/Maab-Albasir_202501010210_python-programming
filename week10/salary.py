# Calculate Gross Salary
def gross_salary(basic_salary, allowance):
    return basic_salary + allowance


# Calculate EPF (11%)
def epf(gross):
    return gross * 0.11


# Calculate SOCSO (0.5%)
def socso(gross):
    return gross * 0.005


# Calculate Net Salary
def net_salary(gross, epf_amount, socso_amount):
    return gross - epf_amount - socso_amount