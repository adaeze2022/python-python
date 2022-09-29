print("Welcome to the rollercoaster!")
height = int(input("What is your height in m? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you?"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $16.")
else:
    print("Sorry, you cannot be allowed on the ride.")
    