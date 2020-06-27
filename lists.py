#lists

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accessing Elements in a List

print(bicycles[0])

#Can use string functions to elements in a List

print(bicycles[0].title()) #Index starts at 0

#Negative Indexing

print(bicycles[-1])

#Changing, Adding, and Removing Elements

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Adding Elements to a List

motorcycles.append('honda')
print(motorcycles)

#Inserting Elements to a List

motorcycles.insert(2, 'bajaj')
print(motorcycles)

#Deleting Elements to a List

del motorcycles[0]
print(motorcycles)

#Removing an Item Using the pop() Method

popped_element = motorcycles.pop()
print(popped_element)
print(motorcycles)

popped_element = motorcycles.pop(1)
print(popped_element)
print(motorcycles)

#Removing an Item by Value

motorcycles.remove('yamaha')
print(motorcycles)

#Sorting a List Permanently with the sort() Method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse = True) #sorting on reverse alphabetical order
print(cars)

#Sorting a List Temporarily with the sorted() Function

cars = ['bmw', 'audi', 'toyota', 'subaru']

print(sorted(cars))
print(cars)

#Printing a List in Reverse Order

cars.reverse()
print(cars)
cars.reverse()
print(cars) #to get the original order again

#Finding the length of list

print(len(cars))

#Looping Through an Entire List

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#Using the range() Function

for value in range(1, 5):
    print(value)

#Using range() to Make a List of Numbers

numbers = list(range(1,6))
print(numbers)

#use the range() function to tell Python to skip numbers

even_numbers = list(range(2, 11, 2))
print(even_numbers)

print(min(even_numbers))
print(max(even_numbers))
print(sum(even_numbers))

#List Comprehensions

squares = [value**2 for value in range(1,11)]
print(squares)

#Slicing a List

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[-3:])
print(players[-3:-2])
print(players[-3:-1])
print(players[-3:4])
print(players[:-2])

#Looping Through a Slice

for player in players[0:3]:
    print(player)

#Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods
print(my_foods)
print(friends_foods)

my_foods.append('cannoli')
friends_foods.append('ice cream')

friends_foods = my_foods

print(my_foods, friends_foods) #Here we see both new elements added are in both the list now

#hence we use friends_food = my_foods[:]

#Tuples

dimensions = (50, 20)
print(dimensions)
print(dimensions[0])

#dimensions[0] = 40   Error

#Looping Through All Values in a Tuple

for dimension in dimensions:
    print(dimension)
