class Dog:
    breed = 'Golden Retriever'
    icon = '🐕'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print('Woof Woof 🐶')
    
    def get_breed(self):
        print(f'{self.name} is a {self.breed}.')
        
    def info(self):
        print(f'''
- Name: {self.name}
- Age: {self.age} years
- Breed: {self.breed}''')
    

dog1 = Dog('Bobby',7)
dog2 = Dog('Spotty',5)
dog2.breed = 'Chiwawa'

dog1.info()
