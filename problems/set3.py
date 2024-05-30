# Inherited Year

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):
    pass

class Car(Vehicle):
    pass

# Comments show expected output
truck1 = Truck(1994)
print(truck1.year)            # 1994

car1 = Car(2006)
print(car1.year)              # 2006

# Start the Engine

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):
    def __init__(self, year):
        super().__init__(year)
        self.start_engine()

    def start_engine(self):
        print('Ready to go!')

# Comments show expected output
truck1 = Truck(1994)          # Ready to go!
print(truck1.year)            # 1994

# Only Pass the Year

class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):
    def __init__(self, year, bed_type):
        super().__init__(year)
        self.bed_type = bed_type

class Car(Vehicle):
    pass

# Comments show expected output
truck1 = Truck(1994, 'Short')
print(truck1.year)            # 1994
print(truck1.bed_type)        # Short

car1 = Car(2006)
print(car1.year)              # 2006
print(car1.bed_type)
# AttributeError: 'Car' object has no attribute 'bed_type'

# Start Engine pt 2

class Vehicle:
    def start_engine(self):
        return 'Ready to go!'

class Truck(Vehicle):
    def start_engine(self, speed):
        return super().start_engine() + f' Drive {speed}, please!'

# Comments show expected output
truck1 = Truck()
print(truck1.start_engine('fast'))
# Ready to go! Drive fast, please!

truck2 = Truck()
print(truck1.start_engine('slow'))
# Ready to go! Drive slow, please!

# Walk the cat

class WalkingMixIn:
    def walk(self):
        print('Let\'s go for a walk!')


class Cat(WalkingMixIn):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

# Comments show expected output
kitty = Cat('Sophie')
kitty.greet()       # Hello! My name is Sophie!
kitty.walk()        # Let's go for a walk!

# Towable

class TowableMixIn:
    def tow(self):
        print('I can tow a trailer!')

class Truck(TowableMixIn):
    pass

class Car:
    pass

# Comments show expected output
truck1 = Truck()
truck1.tow()        # I can tow a trailer!

car1 = Car()
car1.tow()
# AttributeError: 'Car' object has no attribute 'tow'

# Towable #2

class Vehicle:
    def __init__(self, year) -> None:
        self.year = year

class TowingMixin:
    def tow(self):
        return 'I can tow a trailer!'

class Truck(TowingMixin, Vehicle):
    pass

class Car(Vehicle):
    pass

# Comments show expected output
truck1 = Truck(1994)
print(truck1.year)            # 1994
print(truck1.tow())           # I can tow a trailer!

car1 = Car(2006)
print(car1.year)              # 2006

# Method Resolution Path

class Animal:
    def __init__(self, color):
        self.color = color

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat('Black')
print(cat1.color)

# MRO 2

class Animal:
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat()
cat1.color

# MRO 3

class FlyingMixin:
    def fly(self):
        return "I'm flying!"

class Animal:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Cat(Animal):
    pass

class Bird(FlyingMixin, Animal):
    pass

bird1 = Bird('Red')
print(bird1.color)

# MRO: Bird, FlyingMixin, Animal
