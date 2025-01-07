employee_names = ['John Smith', 'Maria Garcia', 'David Kim']
# email_dict = {name: name.lower().replace(' ', '.') + '@learnitlessons.com' for name in employee_names}
# print(email_dict)

email_dict = {}
for name in employee_names:
    email_dict[name] = name.lower().replace(' ', '.') + '@learnitlessons.com'
print(email_dict)

employees = [('John', 'active'), ('Maria', 'inactive'), ('David', 'active')]
active_emails = {name: name.lower() + '@company.com' for name, status in employees if status == 'active'}

prices_usd = {'laptop': 1000, 'phone': 500, 'tablet': 300}
exchange_rate = 0.85
prices_eur = {item: price * exchange_rate for item, price in prices_usd.items()}
print(prices_eur)

prices_eur = {}
for item, price in prices_usd.items():
    prices_eur[item] = price * exchange_rate