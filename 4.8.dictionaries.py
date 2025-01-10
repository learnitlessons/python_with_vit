sales_transactions = {
    "John": 1200,
    "Emma": 1800,
    "Michael": 2400,
    "Sarah": 900,
    "David": 1500
}

commissions = [sale * 0.05 for sale in sales_transactions.values()]
               
commissions = []
for sale in sales_transactions.values():
    commissions.append(sale * 0.05)