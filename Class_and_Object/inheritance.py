class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Inside the animal constructor")

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"

class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def burk(self):
        return f"{self.name} says woof!"

    def discribe(self):
        return f"{self.name} is a {self.breed}"

my_dog = Dog(name= "Buddy", breed= "Bull dog")

print(my_dog.eat())
print(my_dog.burk())

print(my_dog.discribe())