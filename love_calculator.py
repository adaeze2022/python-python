print("Welcome to the love calculator!")
name_1 = input("What is your name? ")
name_2 = input("What is their name? ")
combined_name = name_1 + name_2
lower_case_string = combined_name.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
true = t + r + u + e
love = l + o + v + e
love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, Congratulations! you guys are compatible!")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}, I'm sorry! you guys do not belong together.")
