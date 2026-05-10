
property_price = float(input("Please enter the property price here: "))

first_deposit_price = float(input("Please enter the first deposit price here: "))

annual_percentage_rate = float(input("Please enter the annual percentage rate here: "))

mortgage_term = float(input("Please enter the mortgage term in months here: "))

loan_amount = property_price - first_deposit_price

monthly_rate = annual_percentage_rate / 100 / 12

monthly_payment = (loan_amount * monthly_rate * (1 + monthly_rate) ** mortgage_term) / ((1 + monthly_rate) ** mortgage_term - 1 )

total_payment = monthly_payment * mortgage_term

overpayment = total_payment - loan_amount


print("Monthly payment: ",round(monthly_payment, 2))
print("Overpayment: ",round(overpayment, 2))
print("Your net loan: ", round(loan_amount, 2))
print("Total payment: ",round(total_payment, 2))
