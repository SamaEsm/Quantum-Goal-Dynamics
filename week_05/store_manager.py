import json

class product:
    def __init__(self, name , price, quantity):
        self.name= name
        self.price= price
        self. quantity= quantity

    def __str__(self):
        return f"{self.name} | price: {self.price} | quantity: {self.quantity}"
    
class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added successfully.")

    def show_products(self):
        if len(self.products) == 0:
            print("Store is empty.")
        else:
            print("\nProduct List:")
            for product in self.products:
                print(product)

    def sell_product(self, name, amount):
        for product in self.products:
            if product.name == name:
                if product.quantity >= amount:
                    product.quantity -= amount
                    print(f"{amount} of {name} sold successfully.")
                else:
                    print("Not enough stock.")
                return
        print("Product not found.")

    def search_product(self, name):
        for product in self.products:
            if product.name == name:
                print("Product found:")
                print(product)
                return
        print("Product not found.")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{name} removed successfully.")
                return
        print("Product not found.")


    def save_to_json(self, filename):
        data = []
        for product in self.products:
            data.append({
                "name": product.name,
                "price": product.price,
                "quantity": product.quantity
            })

        with open(filename, "w") as file:
            json.dump(data, file)

        print("Products saved successfully.")

    def load_from_json(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)

        self.products = []

        for item in data:
            product = product(item["name"], item["price"], item["quantity"])
            self.products.append(product)

        print("Products loaded successfully.")

store = Store()

while True:
    print("\n--- Store Menu ---")
    print("1. Add product")
    print("2. Show products")
    print("3. Sell product")
    print("4. Search product")
    print("5. Remove product")
    print("6. Save to JSON")
    print("7. Load from JSON")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Product name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        product = Product(name, price, quantity)
        store.add_product(product)

    elif choice == "2":
        store.show_products()

    elif choice == "3":
        name = input("Product name: ")
        amount = int(input("Amount to sell: "))
        store.sell_product(name, amount)

    elif choice == "4":
        name = input("Product name: ")
        store.search_product(name)

    elif choice == "5":
        name = input("Product name: ")
        store.remove_product(name)

    elif choice == "6":
        filename = input("File name: ")
        store.save_to_json(filename)

    elif choice == "7":
        filename = input("File name: ")
        store.load_from_json(filename)

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")


