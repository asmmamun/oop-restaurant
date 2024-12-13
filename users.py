from abc import ABC
from orders import Order

# Users: Employee, Employee, Admin and Customer
class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super.__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    
    def add_employee(self, restaurant, employee):
        restaurant.add_employee()

    def view_employee(self, restaurant):
        restaurant.show_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()
        

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print(f'Item exceeded!!')
            else:
                item.quantity = quantity
                self.cart.add_item(item)
        else:
            print(f'Item not found!')

    def view_cart(self):
        print(f'***View Cart***')
        print(f'Item Name\tPrice\tQuantity')
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{item.quantity}")
        print(f"Total Price: {self.cart.total_price}")

    def pay_bill(self):
        print("Total Bill {self.cart.total_price} paid successfully.")
        self.cart.clear()





