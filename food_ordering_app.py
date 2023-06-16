class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Restaurant:
    def __init__(self):
        self.food_items = []
        self.users = []
        self.orders = []

    # Admin functionalities
    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.food_items) + 1
        food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(food_item)

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                break

    def view_food_items(self):
        for food_item in self.food_items:
            print(f"FoodID: {food_item.food_id}")
            print(f"Name: {food_item.name}")
            print(f"Quantity: {food_item.quantity}")
            print(f"Price: {food_item.price}")
            print(f"Discount: {food_item.discount}")
            print(f"Stock: {food_item.stock}")
            print("")

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if  self.food_items == food_id:
                self.food_items.remove(food_item)
                break

    # User functionalities
    def register_user(self, full_name, phone_number, email, address, password):
        user = User(full_name, phone_number, email, address, password)
        self.users.append(user)

    def login_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None

    def place_new_order(self, user):
        print("Food Menu:")
        self.view_food_items()
        food_numbers = input("Enter the numbers of the food items you want to order (separated by commas): ")
        food_numbers = list(map(int, food_numbers.split(",")))
        order_items = []
        total_price = 0

        for number in food_numbers:
            if number >= 1 and number <= len(self.food_items):
                selected_food_item = self.food_items[number - 1]
                order_items.append(selected_food_item)
                total_price += selected_food_item.price

        if len(order_items) > 0:
            print("Selected Items:")
            for item in order_items:
                print(f"{item.name} ({item.quantity}) [INR {item.price}]")

            place_order = input("Place the order? (yes/no): ")
            if place_order.lower() == "yes":
                order = {
                    "user": user,
                    "items": order_items,
                    "total_price": total_price
                }
                self.orders.append(order)
                print("Order placed successfully!")
        else:
            print("No valid food items selected.")

    def view_order_history(self, user):
        print(f"Order History for {user.full_name}:")
        for order in self.orders:
            if order["user"] == user:
                print("Order Items:")
                for item in order["items"]:
                    print(f"{item.name} ({item.quantity}) [INR {item.price}]")
                print(f"Total Price: INR {order['total_price']}")
                print("")

    def update_profile(self, user):
        new_full_name = input("Enter new full name: ")
        new_phone_number = input("Enter new phone number: ")
        new_email = input("Enter new email : ")
        new_address = input("Enter new address: ")
        new_password = input("Enter new password: ")
        print("update successful!!!")
        print(f"The new updated full name is {new_full_name}")
        print(f"The new updated phone no  is {new_phone_number}")
        print(f"The new updated email is {new_email}")
        print(f"The new updated address is {new_address}")
        print(f"The new updated password is {new_password}")
        self.full_name = new_full_name
        self.phone_number = new_phone_number
        self.email = new_email
        self.address = new_address
        self.password = new_password
# Usage
restaurant = Restaurant()

# Admin functionalities
admin = Admin("admin", "password")
restaurant.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 100)
restaurant.add_food_item("Vegan Burger", "1 Piece", 320, 0, 50)
restaurant.add_food_item("Truffle Cake", "500gm", 900, 0, 10)

# User functionalities
restaurant.register_user("Psych", "1234567890", "johndoe@example.com", "123 Main St", "password")
user = restaurant.login_user("johndoe@example.com", "password")

check = input("select an option: (1)admin (2)user: ")
for ele in check:
   if ele =="1":
        admin_choice = input("select an option: (1)add food item, (2)Edit food item, (3)view food item, (4)remove food item")
        if admin_choice=="1":
            restaurant.add_food_item(name='',quantity="",price='',discount='',stock='')
        elif admin_choice=="2":
            restaurant.edit_food_item('food_id', 'name', 'quantity', 'price', 'discount','stock')
        elif admin_choice=="3":
            restaurant.view_food_items()
        elif admin_choice=="4":
            restaurant.remove_food_item()
        else:
             break
            
   else:
        user_choice = input("Select an option: (1) Place New Order, (2) Order History, (3) Update Profile: ")
        for cho in user_choice:
            if cho == "1":
               restaurant.place_new_order(user)
            elif cho == "2":
             restaurant.view_order_history(user)
            elif cho == "3":
                 restaurant.update_profile(user)       
            else:
    #else:
              print("incorrect choice")  
