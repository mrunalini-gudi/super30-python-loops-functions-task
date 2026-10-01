#Employee Salary Calculator
def employee_salary_calculator(name,basic_salary,bonus_percent,tax_percent):
    gross_salary = basic_salary + (basic_salary * bonus_percent / 100)
    tax_amount = gross_salary * tax_percent / 100
    final_salary = gross_salary - tax_amount
    return f"Employee: {name}\nGross Salary: ${gross_salary:.2f}\nTax Amount: ${tax_amount:.2f}\nFinal Salary: ${final_salary:.2f}"
i = 0
while i<5:  # Assuming we want to calculate salary for 5 employees
    name = input("Enter employee name : ")
    basic_salary = float(input("Enter basic salary: "))
    bonus_percent = float(input("Enter bonus percentage: "))
    tax_percent = float(input("Enter tax percentage: "))
    result = employee_salary_calculator(name, basic_salary, bonus_percent, tax_percent)
    print(result)
    i += 1
