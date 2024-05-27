class Sport:
    def __init__(self, name) -> None:
        self.name = name
    
basketball = Sport('basketball')
basketball.name
soccer = Sport('soccer')

class Foo:
    pass

foo = Foo()
print(f'I am a {foo.__class__.__name__} object')
print(f'I am a {type(foo).__name__} object')

# Classes and Objects

class Car():
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self.speed = 0
    
    @classmethod
    def mpg(cls, distance, gallons):
        print(f'{distance / gallons} miles per gallon')

    def accelerate(self, number):
        self.speed += number
        print(f'The {self.color} {self.model} accelerate by {number} mph.')

    def brake(self, number):
        self.speed -= number
        print(f'The {self.color} {self.model} brakes by {number} mph.')

    @staticmethod
    def turn_on():
        print(f'The engine is turned on.')
    
    def turn_off(self):
        self.speed = 0
        print(f'The {self.model}\'s engine is turned off.')
    
    def get_speed(self):
        print(f'The current speed is: {self.speed} mph')

    def paint_car(self, new_color):
        self.color = new_color

    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_color):
        self._color = new_color

s10 = Car('chevy', 1995, 'silver')
Car.turn_on()
s10.model
s10.year
s10.color
#s10.color = 'pink'
s10.paint_car('pink')
s10.color

s10.year = 1900

s10.accelerate(20)
s10.get_speed()
s10.brake(10)
s10.turn_off()
s10.get_speed()

# Person

class Person:
    def __init__(self, f_name, l_name):
        self._set_name(f_name, l_name)
    
    @classmethod
    def _validate(cls, name):
        if not name.isalpha():
            raise ValueError('Name must be alphabetic')
    
    def _set_name(self, f_name, l_name):
        Person._validate(f_name)
        Person._validate(l_name)
        self._f_name = f_name
        self._l_name = l_name

    @property
    def name(self):
        f_name = self._f_name.capitalize()
        l_name = self._l_name.capitalize()
        return f'{f_name} {l_name}'
    
    @name.setter
    def name(self, new_name):
        f_name, l_name = new_name
        self._set_name(f_name, l_name)


actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
character = Person('Da5id', 'Meier')
# ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.]


##
## Magic Methods
##

class Car:
    def __init__(self, name, year, color):
        self.name = name
        self.year = year
        self.color = color

    def __str__(self):
        return f'{self.name} {self.year} {self.color.capitalize()}'

    def __repr__(self) -> str:
        return f'Car({self.name}, {self.year}, {self.color})'


class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        color = self.color.title()
        return f'{color} {self.year} {self.model}'

    def __repr__(self):
        color = repr(self.color)
        year = repr(self.year)
        model = repr(self.model)
        return f'Car({model}, {year}, {color})'

# Vector


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)
    
    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x * other.x
        new_y = self.y * other.y
        return new_x + new_y
    
    def __abs__(self):
        magnitude = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        return magnitude

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

v1 = Vector(5, 12)
v2 = Vector(13, -4)
print(v1 + v2)      # Vector(18, 8)

print(v1 - v2) # Vector(-8, 16)
print(v1 * v2) # 17
print(abs(v1)) # 13.0

##
## Election 
##

class Candidate:
    def __init__(self, name):
        self.votes = 0
        self.name = name

    def __add__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        
        self.votes += 1
        return self

    def info(self):
        print(f'{self.name}: {self.votes} votes')

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

class Election:
    def __init__(self, candidates) -> None:
        self.candidates = candidates
    
    def results(self):
        outcome = {candidate.name: candidate.votes
            for candidate in candidates
        }
        for name, votes in outcome.items():
            print(f'{name}: {votes} votes')

        winner = max(outcome, key=outcome.get)
        winning_votes = outcome.get(winner)
        total_votes = sum(outcome.values())
        return f'\n{winner} won: {winning_votes / total_votes:.1%} votes'

election = Election(candidates)
print(election.results())