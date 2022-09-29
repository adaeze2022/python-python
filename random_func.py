import random
names_string = input("Give me everybody's name separated by a comma.\n")
names = names_string.split(",")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_to_pay = names[random_choice]
print(f"{person_to_pay} should pay the bills today!")
