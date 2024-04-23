from abc import ABC
class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item quantity exceeded!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item Added!!")
        else:
            print("Item Not Found!!")
    
    def view_cart(self):
        print("***View Cart***")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price}")

class Order:
    def __init__(self) -> None:
        self.items = {} #eta dictionary

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity # jodi cart e already thaake
        else:
            self.items[item] = item.quantity # cart e na thakle
    
    def remove(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear(self):
        self.items = {}
class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary
    
class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)
    
    def view_employee(self, restaurent):
        restaurent.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = [] # Its our Database
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address, emp.salary)

class Menu:
    def __init__(self):
        self.items = [] # Its Item DB
    
    def add_menu_item(self, item):
        self.items.append(item)
    
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Deleted!!")
        else:
            print("Item Not Found!!")
    
    def show_menu(self):
        print("****Menu****")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
rsturnt = Restaurent("Khai dai ghumai")

mn = Menu()
item = FoodItem("Pizza", 299, 15)
item2 = FoodItem("Burger", 210, 45)
item3 = FoodItem("Momos", 120, 10)
item4 = FoodItem("Khacchi", 350, 15)

admin = Admin("Israt Zahan", 1766548835, "israt@gmail.com", "Dhaka")
admin.add_new_item(rsturnt, item)
admin.add_new_item(rsturnt, item2)
admin.add_new_item(rsturnt, item3)
admin.add_new_item(rsturnt, item4)
# mn.show_menu()

cstmr = Customer("Israt Zahan", 1766548835, "israt@gmail.com", "Dhaka")
cstmr.view_menu(rsturnt)

item_name = input("Enter item name: ")
item_quantity = int(input("Enter item quantity: "))


cstmr.add_to_cart(rsturnt, item_name, item_quantity)
cstmr.view_cart()



# ad = Admin('karim', 1234, 'k@gmail.com', 'dhaka')
# ad.add_employee('hahim', 9874, 'h@gmail.com', 'dhaka', 34, 'IT', 34000)
# ad.view_employee()