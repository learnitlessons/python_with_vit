department_assignments = {'emp_101': 'sales', 'emp_102': 'finance', 'emp_103': 'IT'}

# keys_list = list(department_assignments.keys())
# keys_list.sort()
# for employee_id in keys_list:
#     print(employee_id, '=>', department_assignments[employee_id])

for employee_id in sorted(department_assignments):
    print(employee_id, '=>', department_assignments[employee_id])

for letter in 'techcorp':
    print(letter.upper())

time_remaining = 4
while time_remaining > 0:
    print('System shutdown in: ' * time_remaining)
    time_remaining -= 1