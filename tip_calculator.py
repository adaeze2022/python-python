print("Welcome to the tip calculator!")
bill = (float(input("What was the total bill?$")))
tip = (int(input("What percentage would you like to give? 10, 12, or 15?")))
people = (int(input("How many people split the bill?")))
bill_with_tip = tip/100 * bill + bill
final_amount = "{:.2f}".format(bill_with_tip)#the {:.2f} is used to round off numbersmto 2 decimal places.
print(f"Each person should pay: ${final_amount}")
