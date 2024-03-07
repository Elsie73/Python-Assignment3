def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    Parameters:
    - price: Original price of the item.
    - discount_percent: Discount percentage to be applied.

    Returns:
    - Final price after applying the discount.
    """
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price by subtracting the discount amount
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        # If the discount percentage is less than 20%, return the original price
        return price

def main():
    # Prompt the user to enter the original price of the item
    original_price = float(input("Enter the original price of the item: "))
    # Prompt the user to enter the discount percentage
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percent)
    
    # Check if a discount was applied
    if final_price == original_price:
        # If no discount was applied, print the original price
        print("No discount applied. Final price:", final_price)
    else:
        # If a discount was applied, print the final price after discount
        print("Final price after applying discount:", final_price)

if __name__ == "__main__":
    # Call the main function to execute the program
    main()
