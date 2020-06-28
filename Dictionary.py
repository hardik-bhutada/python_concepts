#A Simple Dictionary

alien_0 = {'color': 'green' , 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#A dictionary in Python is a collection of key-value pairs.
# A key’s value can be a number, a string, a list, or even another dictionary.

# If a
# player shoots down this alien, you can look up how many points they should
# earn using code like this:

new_points = alien_0['points']
print("You just earned "+ str(new_points) + " points !!")

# Adding New Key-Value Pairs

alien_0['x_position'] = 0
alien_0['y_position'] = 255
print(alien_0)

# We can also start with an empty dictionary alien_0 = {}

# Modifying Values in a Dictionary
print("The color of alien is "+ alien_0['color'])

alien_0['color'] = 'yellow'
print("The modified color of alien is "+ alien_0['color'])
del alien_0

# For a more interesting example, let’s track the position of an alien that
# can move at different speeds.

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print("Original position of alien is "+ str(alien_0['x_position']))
x_increment = 0

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("Modified position of alien is "+ str(alien_0['x_position']))

# Looping Through All Key-Value Pairs

user_0 = {
    'username': 'hardik1010',
    'firstname': 'hardik',
    'lastname': 'bhutada'
}

for key, value in user_0.items():
    print('Key : '+ key)
    print('Value : '+ value)

#for key in user_0:   or    for key in user_0.keys(): can be used for looping

# Looping Through a Dictionary’s Keys in Order

for key in sorted(user_0.keys()):
    print(key + " " + user_0[key])

# Looping Through All Values in a Dictionary

for val in user_0.values():
    print("Values : " + val)

# To see each value chosen without repetition, we can use a set.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for language in set(favorite_languages.values()):
    print(language)

# A list of dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens= [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Another example

aliens = []

for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:5]:
    print(alien)

# When it’s time to change colors, we can use a for loop and
# an if statement to change the color of aliens.

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:5]:
    print(alien)

# A list in a dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a "+ pizza['crust']+ " crust pizza with the following toppings : ")

for topping in pizza['toppings']:
    print("\t" + topping)

# Another Example

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}


for name , language in favorite_languages.items():
    print(name.title() + "'s favorite languages are ")
    for lan in language:
        print("\t" + lan)

# A Dictionary in a Dictionary

users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'position' : 'princeton',
    },
    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'position' : 'paris',
    },
}

for username , userinfo in users.items():
    print("UserName : " + username)
    full_name = userinfo['first'] + " " + userinfo['last']
    print(full_name + " Living at " + userinfo['position'])