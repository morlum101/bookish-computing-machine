# import library for saving and loading data
import json

# this is a global list where we store all items in inventory
inventory = []

# class for creating item objects, it holds details of each item
class Item:
    def __init__(self, name, quantity, price):
        # set item details like name, quantity, and price
        self.name = name
        self.quantity = quantity
        self.price = price

    # method to show item details, return a string with name, quantity, and price
    def show(self):
        return f"Name: {self.name}, Qty: {self.quantity}, Price: {self.price}"

# function to add new items in inventory
def add_item(name, quantity, price):
    global inventory
    try:
        # convert quantity to int and price to float
        quantity = int(quantity)
        price = float(price)
        # check if quantity or price is negative
        if quantity < 0 or price < 0:
            print("quantity and price must not be negative!")
            return
        # create new item and add it to inventory
        new_item = Item(name, quantity, price)
        inventory.append(new_item)
        print("item added!")
    except ValueError:
        # handle error if input is not a number
        print("invalid input! quantity and price must be numbers.")

# function to remove item from inventory
def remove_item(name):
    for item in inventory:
        if item.name == name:  # check if item is in inventory
            inventory.remove(item)
            print("item removed!")
            break
    else:
        # if item is not found
        print(f"item '{name}' not found in inventory.")

# function to update item details like quantity and price
def update_item(name, quantity, price):
    for item in inventory:
        if item.name == name:  # check if item exists
            try:
                quantity = int(quantity)
                price = float(price)
                if quantity < 0 or price < 0:
                    print("quantity and price must not be negative!")
                    return
                # update item details
                item.quantity = quantity
                item.price = price
                print("item updated!")
                break
            except ValueError:
                # handle error if input is wrong
                print("invalid input! quantity and price must be numbers.")
                return
    else:
        print(f"item '{name}' not found in inventory.")

# function to check if an item is in stock
def check_stock(name):
    for item in inventory:
        if item.name == name:
            return item.quantity > 0  # return true if quantity is more than 0
    return False  # return false if item not found

# function to save inventory to a file
def save_inventory():
    try:
        with open("inventory.json", "w") as file:
            json_data = [{"name": item.name, "quantity": item.quantity, "price": item.price} for item in inventory]
            json.dump(json_data, file)
            print("inventory saved to file!")
    except Exception as e:
        print("error saving inventory:", e)

# function to load inventory from file
def load_inventory():
    global inventory
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)
            for entry in data:
                add_item(entry["name"], entry["quantity"], entry["price"])
            print("inventory loaded from file!")
    except FileNotFoundError:
        print("no inventory file found, starting fresh.")
    except Exception as e:
        print("error loading inventory:", e)

# generator to go through all items in inventory one by one
def inventory_generator():
    for item in inventory:
        yield item.show()


# main loop of program
try:
    load_inventory()  # load inventory from file if exists

    while True:
        print("\noptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update item")
        print("4. Show inventory")
        print("5. Check stock")
        print("6. Save and exit")
        print("7. Next program that apply assert, del , lambda, raise ,yield  ") #7 to see the next program that apply assert, del , lambda, raise ,yield



        # get user input for what they want to do
        choice = input("Enter your choice: ")

        if choice == "1":
            # for adding a new item
            name = input("Enter item name: ")  # ask for the item name
            quantity = input("Enter quantity: ")  # ask for how many
            price = input("Enter price: ")  # ask for the price
            add_item(name, quantity, price)  # call the function to add it
        elif choice == "2":
            # for removing an item
            name = input("Enter name of item to remove: ")  # ask the name of the item to delete
            remove_item(name)  # call the function to remove it
        elif choice == "3":
            # for updating an item
            name = input("Enter item name to update: ")  # ask the name of the item
            quantity = input("Enter new quantity: ")  # ask the new quantity
            price = input("Enter new price: ")  # ask the new price
            update_item(name, quantity, price)  # call the function to update it
        elif choice == "4":
            # for showing the whole inventory
            for item in inventory_generator():  # loop through the generator
                print(item)  # print all the items one by one
        elif choice == "5":
            # for checking if an item is in stock
            name = input("Enter item name to check stock: ")  # ask the name to check
            if check_stock(name):  # check if it exists in inventory
                print("Item is in stock.")  # item exists
            else:
                print("Item is out of stock.")  # item doesn’t exist
        elif choice == "6":
            # save inventory and exit
            save_inventory()
            print("Inventory saved. goodbye!")
            break
        elif choice == "7":
            # apply to next program
            save_inventory()
            print("Inventory saved. switching to next program...")
            break
        else:
            print("Ivalid choice. please enter a number between 1 and 7.")
except Exception as e:
    # handle unexpected errors
    print("An unexpected error happened:", e)
finally:
    print("Thanks for using the inventory system.\n")


# next program


print("This program apply assert, del , lambda, raise ,yield\n")
# function to check if number is positive
def check_positive(num):
    try:
        # assert makes sure the number is not negative
        assert num >= 0, "number must be positive"
        return f"{num} is positive"
    except AssertionError as e:
        # show message if assert fails
        print(e)
        return "please input again"

# function to get square of number
square = lambda x: x * x  # lambda is for one-line functions

# function to show how raise works
def raise_error_example():
    # raise creates an error on purpose
    raise ValueError("this is a test error. something went wrong")

# generator function to use yield
def generate_numbers(limit):
    # yield gives numbers one by one
    for i in range(limit):
        yield i

# main program
try:
    while True:
        try:
            # ask user for a number and check if it’s positive
            user_num = int(input("enter a number to check if it’s positive: "))
            result = check_positive(user_num)  # this will test assert
            if result != "please input again":
                print(result)
                break
        except ValueError:
            # show error if input is not a number
            print("please enter a valid number")

    while True:
        try:
            # ask user for another number to test lambda
            square_num = int(input("enter a number to find its square: "))
            print("the square is:", square(square_num))  # this will use lambda
            break
        except ValueError:
            # show error if input is not a number
            print("please enter a valid number")

    # test raise by asking user to see if they want an error
    user_choice = input("do you want to see an error? (yes/no): ").lower()
    if user_choice == "yes":
        raise_error_example()  # raise will create an error here

    while True:
        try:
            # test yield by asking for a limit
            limit = int(input("enter a limit to generate numbers: "))
            print("numbers from generator:")
            for num in generate_numbers(limit):
                print(num)  # print each number from the generator
            break
        except ValueError:
            # show error if input is not a number
            print("please enter a valid number")

    # test del by deleting a variable
    x = 100
    print(f"variable x before delete: {x}")
    del x  # del removes x
    # print(x)  # uncomment this to see error after deleting x

except Exception as e:
    print("an error happened:", e)  # catch any error
