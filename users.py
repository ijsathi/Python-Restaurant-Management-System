from abc import ABC
class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

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

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = [] # Its our Database

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


ad = Admin('karim', 1234, 'k@gmail.com', 'dhaka')
ad.add_employee('hahim', 9874, 'h@gmail.com', 'dhaka', 34, 'IT', 34000)
ad.view_employee()