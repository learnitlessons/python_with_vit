employee_name = 'John Smith'
department = 'Information Technology'
feedback = "The customer's system was successfully updated"

sql_query = """
SELECT 
    employee_id,
    department,
    hire_date
FROM
    employees
WHERE
    department = 'IT'
    AND hire_date >= '2025-01-02'
"""