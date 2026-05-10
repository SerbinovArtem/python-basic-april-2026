
deposit_summ = float(input("Please enter a deposit amount here: "))

deposit_term = int(input("Plese enter a deposit term here: "))

deposit_percentage = 2.2 / 100

total_amount = deposit_summ + deposit_term * ((deposit_summ * deposit_percentage) / 12)

print(total_amount)