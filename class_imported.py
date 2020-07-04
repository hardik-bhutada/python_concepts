
from importing_class import Car

my_new_car = Car('audi', 'Q4', 2000)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 33
my_new_car.read_odometer()

# Importing multiple classes

from importing_class import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

