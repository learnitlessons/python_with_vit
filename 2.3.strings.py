customer_name  = 'John Smith'
# customer_name[0] - 'j'
modified_name = 'j' + customer_name[1:]
print(modified_name)

company_name = 'TechCorp'
name_chars = list(company_name)
name_chars[0] = 't'
modified_company = ' '.join(name_chars)
print(modified_company)


