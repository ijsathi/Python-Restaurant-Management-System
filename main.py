from foodItem import FoodItem
from menu import Menu
from order import Order
from restaurent import Restaurent
from users import User, Customer, Employee, Admin
khai_khai_rest = Restaurent("Khai Khai")

def customer_menu():
    name = input("Enter your Name: ")
    email = input("Enter your Email: ")
    phone = input("Enter your Phone: ")
    address = input("Enter your Address: ")
    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {customer.name}!!!")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            customer.view_menu(khai_khai_rest)
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            item_quantity = int(input("Enter Item Quantity: "))
            customer.add_to_cart(khai_khai_rest, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid. Please Enter valid digit")


def admin_menu():
    name = input("Enter your Name: ")
    email = input("Enter your Email: ")
    phone = input("Enter your Phone: ")
    address = input("Enter your Address: ")
    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {admin.name}!!!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Items")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
           item_name = input("Enter Item Name: ")
           item_price = int(input("Enter Item Price: "))
           item_quantity = int(input("Enter Item Quantity: "))
           item = FoodItem(item_name, item_price, item_quantity)

           admin.add_new_item(khai_khai_rest, item)
        elif choice == 2:
            name = input("Enter Employee Name: ")
            email = input("Enter Employee Email: ")
            phone = input("Enter Employee Phone: ")
            address = input("Enter Employee Address: ")
            designation = input("Enter Employee Designation: ")
            age = input("Enter Employee Age: ")
            salary = input("Enter Employee Salary: ")
            employee = Employee(name, phone, email, address, age, designation, salary)
            admin.add_employee(khai_khai_rest, employee)
        elif choice == 3:
            admin.view_employee(khai_khai_rest)
        elif choice == 4:
            admin.view_menu(khai_khai_rest)
        elif choice == 5:
            item_name = input("Enter Item Name: ")
            admin.remove_item(khai_khai_rest, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid. Please Enter valid digit")

while True:
    print("Welcome!!")
    print("1.  Customer")
    print("2.  Admin")
    print("3.  Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid")
