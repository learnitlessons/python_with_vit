employees = [
    ["Alice", "IT", 75000],
    ["Bob", "HR", 65000],
    ["Carol", "IT", 78000]
]

it_salaries = [emp[2] for emp in employees if emp[1] == "IT"]
print(it_salaries)

average_it_salary = sum(it_salaries) / len(it_salaries)
print(f" Average IT Salary: ${average_it_salary}")

departments = set([emp[1] for emp in employees])
print(departments)