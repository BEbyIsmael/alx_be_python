income = input("Enter your monthly income: ")
expenses = input("Enter your total monthly expenses: ")
Monthly_savings = int(income) - int(expenses)
projected_savings = Monthly_savings * 12 + (
    Monthly_savings * 0.05 * 12
)  # Assuming a 5% increase in savings
print(f"Your monthly savings are ${Monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
