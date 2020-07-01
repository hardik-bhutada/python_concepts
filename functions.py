#Defining a function

def greet_user():
    '''This is a comment called as docstring which describes
what the function does.'''
    print("Hello Sir")

greet_user()

# Passing Information to a Function

def greet_with_name(username):
    print("Hello " + username.title() + " !")

greet_with_name("Hardik")

# Positional Arguments

def describe_pet(animal_type , animal_name):
    print("I have a " + animal_type + " whose name is " + animal_name)

describe_pet("cat" , "meoww")
# describe_pet('dog', 'cash')   We can call a function as many time as needed

# Order Matters in Positional Arguments
# You can get unexpected results if you mix up the order of the arguments

# Keyword Arguments
# A keyword argument is a name-value pair that you pass to a function. You
# directly associate the name and the value within the argument, so when you
# pass the argument to the function, there’s no confusion


def describe_pet_using_keyword_argument(animal_type , animal_name):
    print("Using keyword arguments ----- I have a " + animal_type + " whose name is " + animal_name)

describe_pet_using_keyword_argument(animal_name='meoww' , animal_type='cat')

# Default Values
# When writing a function, you can define a default value for each parameter.

def describe_pet_default_values(animal_name, animal_type = 'dog'):
    print("Using default arguments ----- I have a " + animal_type + " whose name is " + animal_name)

describe_pet_default_values(animal_name='cash')
                        # or
# describe_pet_default_values('cash', 'cat')
# describe_pet_default_values(animal_name='sheep', animal_type='shaun')

# Returning a Simple Value

def get_formatted_name(firstname, lastname):
    fullname = firstname + " " + lastname
    return fullname.title()

musician = get_formatted_name("hardik", "bhutada")
print(musician)

def get_formatted_name(firstname, middlename, lastname):
    fullname = firstname + " " + middlename + " " + lastname
    return fullname.title()

musician = get_formatted_name('hardik', 'gajanan', 'bhutada')
print(musician)

# Making an Argument Optional

def optional_argument(firstname, lastname, middlename=''):
    if middlename:
        fullname = firstname + ' ' + middlename + ' ' + lastname
    else:
        fullname = firstname + ' ' + lastname

    return fullname.title()

musician = optional_argument('hardik', 'bhutada')
print(musician)

musician = optional_argument('hardik', 'bhutada', 'gajanan')
print(musician)

# Returning a Dictionary

def build_person(firstname, lastname):
    '''this function returns a dictionary'''
    person = {'first': firstname, 'last': lastname}
    return person

musician = build_person('Hardik', 'Bhutada')
print(musician)

# Using a Function with a while Loop

def get_formatted_name_withwhileloop(firstname, lastname):
    fullname = firstname + " " + lastname
    return fullname.title()

while True:
    print("Enter name and q to quit")

    firstnameinput = input("Enter first name : ")

    if firstnameinput == 'q':
        break

    lastnameinput = input("Enter last name : ")

    if lastnameinput == 'q':
        break

    name = get_formatted_name_withwhileloop(firstnameinput, lastnameinput)
    print(name)

# Passing and Modifying a List

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        designs = unprinted_designs.pop()
        print("Printing : " + designs)

        completed_models.append(designs)

def print_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model + " is completed")

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
print_completed_models(completed_models)
print(unprinted_designs)

# Preventing a Function from Modifying a List

def print_models(unprinted_designs, completed_models):

    ''' You can send a copy of a list to a function
    The slice notation [:] makes a copy of the list to send to the function '''

    while unprinted_designs:
        designs = unprinted_designs.pop()
        print("Printing : " + designs)

        completed_models.append(designs)

def print_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model + " is completed")

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
print_completed_models(completed_models)
print(unprinted_designs)

# Passing an Arbitrary Number of Arguments

def make_pizza(*toppings):
    '''Note that Python packs the
    arguments into a tuple, even if the function receives only one value'''
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing Positional and Arbitrary Arguments

def make_pizza(size, *toppings):
    print("Making a " + str(size) + " inch pizza with following toppings")
    for topping in toppings:
        print(" - " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary Keyword Arguments

def build_profile(firstname, lastname, **user_info):
    '''In this case, you can write functions that accept as many key-value
    pairs as the calling statement provides'''

    profile = {}

    profile['firstname'] = firstname
    profile['lastname'] = lastname

    for key, value in user_info.items():
        profile[key] = value

    return profile


user_profile = build_profile('hardik', 'bhutada', location = 'pune', country = 'India')
print(user_profile)

# Importing an Entire Module

import learningto_importmodules

learningto_importmodules.make_pizza(16, 'pepperoni')
learningto_importmodules.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing Specific Functions

from learningto_importmodules import make_pizza
make_pizza(16, 'pepperoni')

# Using as to Give a Function an Alias

from learningto_importmodules import make_pizza as mp
mp(16, 'pepperoni')

# Using as to Give a Module an Alias

import learningto_importmodules as p
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module

from learningto_importmodules import *
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')