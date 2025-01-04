sales_data = [
    [100, 150, 200], # Product A daily sales
    [300, 350, 400], # Product B daily sales
    [500, 550, 600]  # Product C daily sales
]

daily_totals = (sum(day) for day in sales_data)
print(f"Day 1 total sales: ${next(daily_totals)}")
print(f"Day 2 total sales: ${next(daily_totals)}")
print(f"Day 3 total sales: ${next(daily_totals)}")

product_totals = list(map(sum, sales_data))
print(product_totals)

# {sale for product in sales_data for sale in product}

unique_sales = set()
for product in sales_data:
    for sale in product:
        unique_sales.add(sale)

print("Unique sales value:", sorted(unique_sales, reverse=True))

daily_increases = [day2 - day1 for day1, day2 in zip(sales_data[0][:-1], sales_data[0][1:])]
print(daily_increases)
for increase in daily_increases:
    print(f"Increase: ${increase}")