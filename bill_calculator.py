print("Welcome to the Python Pizza Delivery!")
size_of_pizza = input("What size of pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni on your pizza? Y or N ")
extra_cheese = input("Do you want extra cheese on your pizza? Y or N  ")
bill = 0
if size_of_pizza == "S":
    bill += 15
if size_of_pizza == "L":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if size_of_pizza == "S":
       bill += 2
else:
    bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}, Have a nice day!")
    