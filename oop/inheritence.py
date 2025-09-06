class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Baby(Person):
    pass

class Adult(Person):
    def drink(self,drink_name):
        print(f'I am drinking {drink_name}')

ian = Baby("Ian", 1)
print(isinstance(ian, Person))