
emplyee_data = [
    [1001, 50000, 'HR', 'Active'],
    [1002, 60000, 'IT', 'Active'],
    [1003, 55000, 'Sales', 'Inactive'],
    [1004, 65000, 'IT', 'Active']
]

adjusted_salaries = [employee[1] + 5000 for employee in emplyee_data]
print(adjusted_salaries)
it_department = [employee[1] for employee in emplyee_data if employee[2] == 'IT']
print(it_department)
active_employee_ids = [employee[0] for employee in emplyee_data if employee[3] == 'Active']
print(active_employee_ids)
department_codes = [employee[2] for employee in emplyee_data]
formatted_codes = [code.lower() for code in department_codes]
print(formatted_codes)
high_salary_employees = [employee for employee in emplyee_data if employee[1] > 55000]
print(high_salary_employees)