monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses:"))

#Calculating the monthly savings
monthly_savings = monthly_income - monthly_expenses
#calculating the projected savings
projected_savings = monthly_savings * 12 +(monthly_savings * 12* 0.05)

#printing the projected annual savings
print(f"Projected savings after one year , with interest, is ${projected_savings}")

