def calculate_total(price, quantity, discount_percentage=0):
    if price < 0 or quantity < 0 or discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Invalid parameters provided")
    
    subtotal = price * quantity
    discount_amount = subtotal * (discount_percentage / 100)
    return round(subtotal - discount_amount, 2)

def menu():
    print("\n--- Shopping Bill Calculator (v2 with Discount) ---")
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        discount = float(input("Enter discount percentage (0-100): "))
        
        total = calculate_total(price, quantity, discount)
        print(f"Total Bill (after discount): ${total}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    menu()
