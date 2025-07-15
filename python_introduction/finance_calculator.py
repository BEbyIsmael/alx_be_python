income = float(input("Enter your monthly income: "))  # Changed to float
expenses = float(input("Enter your total monthly expenses: "))  # Changed to float
Monthly_savings = income - expenses

# Your original (correct) interest formula:
projected_savings = Monthly_savings * 12 + (Monthly_savings * 0.05 * 12)

# Better output formatting:
print(f"Your monthly savings are ${Monthly_savings:.2f}")  # :.2f for 2 decimal places
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")
