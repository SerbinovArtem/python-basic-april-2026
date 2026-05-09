
square_meters = int(input("Please enter your square in meters please: "))
registered_user = input("Is user registered? y/n: ")


sqm_price = 7.61


if registered_user == "y":
    sqm_price *= 0.82

total_price = square_meters * sqm_price

print(f"The total price is ${total_price}")
