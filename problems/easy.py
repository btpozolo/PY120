# Banner Class

class Banner:
    def __init__(self, message):
        self.message = message
        self.length = len(message) + 2

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return '|' + (' ' * self.length) + '|'

    def _horizontal_rule(self):
        return '+' + ('-' * self.length) + '+'

    def _message_line(self):
        return f"| {self.message} |"
    
    # Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+

# Rectangle

class Rectangle:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height
        self._area = width * height
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @property
    def area(self):
        return self._area


rect = Rectangle(4, 5)

print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True

# Square

class Square(Rectangle):
    def __init__(self, width) -> None:
        super().__init__(width, width)

square = Square(5)
print(square.area == 25)      # True

# Cats

class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color
    
    @property
    def info(self):
        return f'My {type(self).__name__.lower()} {self.name} is {self.age} years old and has {self._color} fur.'

cocoa = Cat('Cocoa', 3, 'black')
cheddar = Cat('Cheddar', 4, 'yellow and white')

print(cocoa.info)
print(cheddar.info)

#  

''' Output:
My cat Cocoa is 3 years old and has black fur.
My cat Cheddar is 4 years old and has yellow and white fur.
'''

# Animals

class Animal:
    def __init__(self, name, age, legs, species, status):
        self.name = name
        self.age = age
        self.legs = legs
        self.species = species
        self.status = status

    def introduce(self):
        return (f"Hello, my name is {self.name} and I am "
                f"{self.age} years old and {self.status}.")

class Cat(Animal):
    def __init__(self, name, age, status):
        super().__init__(name, age, 4, 'cat', status)
    
    def introduce(self):
        return super().introduce() + ' Meow meow!'

class Dog(Animal):
    def __init__(self, name, age, status, owner):
        super().__init__(name, age, 4, 'dog', status)
        self._owner = owner
    
    @property
    def owner(self):
        return self._owner
    
    def introduce(self):
        return super().introduce() + ' Woof! Woof!'
    
    def greet_owner(self):
        return f'Hi {self.owner}! Woof! Woof!'

dog = Dog("Bobo", 9, "hungry", "Daddy")
expected = ("Hello, my name is Bobo and I am 9 years old "
            "and hungry. Woof! Woof!")
print(dog.introduce() == expected)                  # True
print(dog.greet_owner() == "Hi Daddy! Woof! Woof!") # True


cat = Cat("Pepe", 4, "happy")
expected = ("Hello, my name is Pepe and I am 4 years old "
            "and happy. Meow meow!")
print(cat.introduce() == expected)      # True

# Pet Shelter

class Pet:
    def __init__(self, type, name) -> None:
        self.type = type
        self.name = name
    
    def __str__(self) -> str:
        return self.name

class Owner:
    def __init__(self, name) -> None:
        self.name = name
        self.pets = []
    
    def adopt(self, pet):
        self.pets.append(pet)

    def number_of_pets(self):
        return len(self.pets)
    
    def __str__(self) -> str:
        return self.name

class Shelter:
    adoptions = dict()

    def __init__(self) -> None:
        pass

    def adopt(self, owner, pet):
        self.adoptions.setdefault(owner, []).append(pet)
        owner.adopt(pet)
        pass

    def print_adoptions(self):
        for owner, pets in self.adoptions.items():
            print(f'{owner} has adopted the following pets:')
            for pet in pets:
                print(f'a {pet.type} named {pet.name}')
            print()
        

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")

# P Hanson has adopted the following pets:
# a cat named Cocoa
# a cat named Cheddar
# a bearded dragon named Darwin

# B Holmes has adopted the following pets:
# a dog named Molly
# a parakeet named Sweetie Pie
# a dog named Kennedy
# a fish named Chester

# P Hanson has 3 adopted pets.
# B Holmes has 4 adopted pets.


# Refactoring Vehicles

class Vehicle:
    def __init__(self, make, model, wheels) -> None:
        self.make = make
        self.model = model
        self.wheels = wheels
    
    def get_wheels(self):
        return self.wheels
    
    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 4)

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 2)

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model, 6)
        self.payload = payload

# Moving

class WalkMixin:
    def walk(self):
        return f'{self.name} {self.gait()} forward'

class Person(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"
    
mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"

# Nobility

class Noble(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self.title = title
    
    def walk(self):
        return f'{self.title} {self.name} struts forward'

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"

# Complete the Program - Houses

class House:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __lt__(self, other):
        if isinstance(other, House):
            return self.price < other.price
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, House):
            return self.price > other.price
        return NotImplemented

home1 = House(100000)
home2 = House(150000)
if home1 < home2:
    print("Home 1 is cheaper")
if home2 > home1:
    print("Home 2 is more expensive")

# Home 1 is cheaper
# Home 2 is more expensive

# Wallet 

class Wallet:
    def __init__(self, amount) -> None:
        self._amount = amount
    
    @property
    def amount(self):
        return self._amount

    def __add__(self, other):
        if isinstance(other, Wallet):
            return Wallet(self.amount + other.amount)
        return NotImplemented

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
type(merged_wallet)
print(merged_wallet.amount == 80)       # True

# Wallet 2

class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Wallet(self.amount + other.amount)

    def __str__(self) -> str:
        return f'Wallet with ${self.amount}'

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet)          # Wallet with $80.

# Reverse Engineering

class Transform:
    def __init__(self, data) -> None:
        self.data = data

    def uppercase(self):
        return self.data.upper()
    
    @classmethod
    def lowercase(cls, data):
        return data.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz