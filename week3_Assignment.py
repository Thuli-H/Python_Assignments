# This function calculates the final price after applying a discount
def calculate_discount(price, discount_percent):
    # If discount is 20% or more, apply the discount
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Ask the user to enter the original price
original_price = float(input("Enter the original price of the item: "))

# Ask the user to enter the discount percent
discount = float(input("Enter the discount percentage: "))

# Use the function to calculate the final price
final_price = calculate_discount(original_price, discount)

# Show the final price to the user
if discount >= 20:
    print(f"The final price after {discount}% discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The price remains: ${final_price:.2f}")
