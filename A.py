def shopping_cart():
    cart = []

    while True:
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout")
        choice = input("Enter your choice (1-4): ")
# Add item to cart        if choice == "1":
# item = input("Enter item name: ")
# price = float(input("Enter item price: "))
# if item.lower() == "alcohol":
# age = int(input("Please enter your age: "))
# if age < 18:
# print("Sorry, you must be 18 or older to buy alcohol.")
# continue
# cart.append((item, price))
# print(f"{item} added to cart.")
# Remove item from cart
# elif choice == "2":
# item = input("Enter item name: ")
# for i, (name, price) in enumerate(cart):
# if name == item:
# cart.pop(i)
# print(f"{name} removed from cart.")
# break
# else:
# print(f"{item} not found in cart.")
# View cart        elif choice == "3":            if not cart:                print("Cart is empty.")            else:                total = 0                for item, price in cart:                    print(f"{item} - ${price}")                    total += price                print(f"Total: ${total}")        # Checkout        elif choice == "4":            if not cart:                print("Cart is empty.")            else:                total = sum(price for item, price in cart)                print(f"Your total is ${total}. Thank you for shopping!")                break        else:            print("Invalid choice. Please try again.")shopping_cart()