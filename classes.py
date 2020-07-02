# Creating and Using a Class

class Dog:
    '''A simpl class to model a dog'''

    def __init__(self , name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is sitting")

    def roll_over(self):
        print(self.name.title() + " is rolling over")

my_dog = Dog("Cash", 21)
my_dog.sit()
my_dog.roll_over()

your_dog = Dog("Bella", 12)
your_dog.sit()
your_dog.roll_over()

print(str(my_dog.age) + " is the age of my dog named " + my_dog.name)

# Working with Classes and Instances

class Car:

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        print(self.name.title() + " , " + self.model + " , " + str(self.year) +
              " having an run of " + str(self.odometer) + " miles")

    def update_odometer(self, mileage):
        '''changing the value of attribute through method'''

        if mileage >= self.odometer:
            self.odometer = mileage

        else:
            print("You cant roll back odometer")

    def increment_odometer(self, mileage):
        '''updating odometer value using method'''

        self.odometer += mileage


my_car = Car("Audi", "Q4", 1986)
my_car.odometer = 55                     #modifying the attribute value directly
my_car.update_odometer(62)
my_car.increment_odometer(18)
my_car.get_descriptive_name()

# Inheritance

class ElectricCar(Car):
    '''child class of Car class'''

    def __init__(self, name, model, year):
        '''we will user super.init to connect with parent class'''
        super().__init__(name, model, year)
        self.charge_time = 2
        self.battery = Battery()

    def describe_battery(self):
        print("Car has a battery charging time of " + str(self.battery) + " hr")

    def increment_odometer(self, mileage):
        # Overriding methods from a parent class
        # To do this, you define a method
        # in the child class with the same name as the method you want to override
        # in the parent class. Python will disregard the parent class method and only
        # pay attention to the method you define in the child class.
        print("Child class ")
        self.odometer += mileage

class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

tesla = ElectricCar('tesla', 'T6', 2002)
tesla.increment_odometer(88)
tesla.update_odometer(12)
tesla.battery.describe_battery() # Calling battery's method describe_battery