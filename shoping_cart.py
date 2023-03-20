""""This is amazon cart solution"""


cart = []
name = input("Enter your name please: ")
items = ["Groceries, Fruits, Vegetables, Toys"]
user_input = "yes"

def greetings():
    print(f"Hello {name}, welcome to our cart")

def view_items():
    print(items)

def add_item(item):
    cart.append(item)
    print(cart)


while user_input == "yes":
    greetings()
    view_items()
    add_item("Groceries")
    user_input = input("Do you want to continue purchas?")
else:
    print("Thank you for doing business with us. See you soon")

