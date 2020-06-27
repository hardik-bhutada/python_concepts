#If - Statements

cars = ['Audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age_0 = 26
if age_0 > 18 and age_0 < 40: #returns true if both conditions are true or else returns false
    print("Young")

if age_0 > 0 or age_0 < 18: #returns false if both conditions are false or else returns true
    print("not eligible")

#Checking Whether a Value Is in a List

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("True")

#Checking Whether a Value Is Not in a List

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user + " can do all the assigned work")

#The if-elif-else Chain

age = 12

if age < 12:
    print("Pay Rs. 60")
elif age < 18:
    print("Pay Rs. 100")
else:
    print("Pay Rs. 150")

#Using if Statements with Lists

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for toppings in requested_toppings:
    if toppings == 'green peppers':
        print("Sorry we are out of greem peppers now")
    else:
        print("Adding -- "+ toppings)

# As an example, let’s check whether the list of requested toppings is
# empty before building the pizza. If the list is empty, we’ll prompt the user
# and make sure they want a plain pizza. If the list is not empty, we’ll build
# the pizza just as we did in the previous examples:

requested_toppings = []

if requested_toppings:
    for toppings in requested_toppings:
        print("Adding -- " + toppings)
else:
    print("Do you want a plain pizza ?")

#Using Multiple Lists

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for toppings in requested_toppings:
    if toppings in available_toppings:
        print("Adding -- " + toppings)
    else:
        print("Sorry we are out " + toppings)