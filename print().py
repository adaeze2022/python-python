#this is a comment
print("Hello, World!")


x = 5
y = "John"
print(x)
print(y)


x = 4        # x is of type int
x = "Sally"  # x is of type str
print(x)

x = "awesome"
print("Python is" + x)

x = "Python "
y = "is "
z = "awesome"
o = x + y + z  
print(o)


x = 10
y = 20
print(x + y)

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)

x = 5
print(type(x))

x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

x = 35e3
print(x)

x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(type(a))
print(type(b))
print(type(c))

print(a)
print(b)
print(c)

import random
print(random.randrange(1, 10))

print("Hello")
print('Hello')

a = """Python is a very interesting and useful
programing language. """
print(a)

a = 'Hello, World!'
print(a[6])

for b in "banana":
    print(b)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "the best things in life are not free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are not free!"
print("expensiive" not in txt)

txt = "The best things in life are not free!"
if "expensive" not in txt:
    print("No, 'expensive' is not present in the sentence.")

b = "Young thug is cheese!"
print(b[2:5])

b= "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(","))

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 34
txt = "My name is Jason, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.98
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.98
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(10 + 5)

