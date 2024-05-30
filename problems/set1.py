# Find the class

# Comments show expected output
print(type("Hello"))                # <class 'str'>
print(type(5))                      # <class 'int'>
print(type([1, 2, 3]))              # <class 'list'>

# Create the Class

class Cat:
    def __init__(self, name) -> None:
        self.name = name
    
    def greet(self):
        print(f'Hello! My name is {self.name}')
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

# Create the Object

kitty = Cat('Sophie')
kitty.greet()
kitty.name = 'Luna'
kitty.greet()

# What are you?

# Hello Sophie!

# Default Person

class Person:
    def __init__(self, name='John Doe') -> None:
        self._name = name
    
    @property
    def name(self):
        return self._name

person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
print(person1.name)    # John Doe
print(person2.name)    # Pepe Le Pew

