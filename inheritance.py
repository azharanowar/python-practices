# Parent/Base Class Blueprint
class Animal:
    def __init__(self, name):
        self.name = name

    def __eat(self):
        print(f"{self.name} is eating now!")

    def sleep(self):
        print(f"{self.name} is sleeping now!")
        self.__eat()  


# Child/Derived Class Blueprint
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking now!")
    
class Cat(Animal):
    def bark(self):
        print(f"{self.name} is meowing now!")


animal = Animal("Animal")

dog = Dog("Mitu")
dog.sleep()
dog.bark()
    
