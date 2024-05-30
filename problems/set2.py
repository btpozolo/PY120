# Generic Greeting

class Cat:
    
    @classmethod
    def generic_greeting(cls):
        print('Hello! I\'m a cat!')
        return

Cat.generic_greeting()
kitty = Cat()
type(kitty).generic_greeting()
print(type(kitty))

# Hello, Chloe!

class Cat:
    def __init__(self, name):
        self._name = name

    def rename(self, new_name):
        self.name = new_name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# Comments show expected output
kitty = Cat('Sophie')
print(kitty.name)             # Sophie
kitty.rename('Chloe')
print(kitty.name)             # Chloe

# Identify Yourself

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    
    def identify(self):
        return self

# Comments show expected output
kitty = Cat('Sophie')
print(kitty.identify())
# <__main__.Cat object at 0x10508c8d0>
# The object ID (0x105...) may vary

# Generic Greeting 2

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @classmethod
    def generic_greeting(cls):
        print('Hello! I\'m a cat!')
    
    def personal_greeting(self):
        print(f'Hello! My name is {self.name}!')

kitty = Cat('Sophie')

# Comments show expected output
Cat.generic_greeting()        # Hello! I'm a cat!
kitty.personal_greeting()     # Hello! My name is Sophie!

# Counting Cats
class Cat:
    num_cats = 0

    def __init__(self) -> None:
        Cat.num_cats += 1
        pass
    
    @classmethod
    def total(cls):
        print(cls.num_cats)

Cat.total()         # 0

kitty1 = Cat()
Cat.total()         # 1

kitty2 = Cat()
Cat.total()         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
Cat.total()         # 3

# Colorful cat

class Cat:
    color = 'purple'

    def __init__(self, name) -> None:
        self.name = name
    
    def greet(self):
        print(f'Hello! My name is {self.name} and I\'m a {Cat.color} cat')

sophie = Cat('sophie')
sophie.greet()

# Identify Yourself 2

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def __str__(self) -> str:
        return f'I\'m {self.name}!'

# Comments show expected output
kitty = Cat('Sophie')
print(kitty)        # I'm Sophie!