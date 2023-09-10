from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __str__(self):
        return f'My name is {self.name}.'


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.fly = "flying"

    def __str__(self):
        return f'My name is {self.name}. I am {self.fly}'


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.swim = "swimming"

    def __str__(self):
        return f'My name is {self.name}. I am {self.swim}'


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.run = "running"

    def __str__(self):
        return f'My name is {self.name}. I am {self.run}'


class Factory:
    @staticmethod
    def create_animal(animal, name) -> Animal:
        if animal == "bird":
            factory_bird = Bird(name)
            return factory_bird
        elif animal == "fish":
            factory_fish = Fish(name)
            return factory_fish
        elif animal == "mammal":
            factory_mammal = Mammal(name)
            return factory_mammal
        else:
            raise WrongAnimalError(f"No such animal: {animal}!", animal)


class WrongAnimalError(Exception):
    def __init__(self, text, animal):
        self.txt = text
        self.animal = animal


if __name__ == '__main__':
    new_bird = Bird("Kesha")
    print(new_bird)
    new_fish = Fish("Dory")
    print(new_fish)
    new_mammal = Mammal("Manny")
    print(new_mammal)

    print(Factory.create_animal('bird', "Factory_Kesha"))
    print(Factory.create_animal('fish', "Factory_Dory"))
    print(Factory.create_animal('mammal', "Factory_Manny"))
    print(Factory.create_animal('insect', "Factory_Ant"))
