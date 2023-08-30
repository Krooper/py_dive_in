"""
Задание №5
Создайте три (или более) отдельных классов животных. Например, рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
"""

class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.fly = "flying"

    def __str__(self):
        return f'I am {self.fly}'


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.swim = "swimming"

    def __str__(self):
        return f'I am {self.swim}'

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.run = "running"

    def __str__(self):
        return f'I am {self.run}'


if __name__ == '__main__':
    new_bird = Bird("Kesha")
    print(new_bird)

    new_fish = Fish("Dory")
    print(new_fish)

    new_mammal = Mammal("Manny")
    print(new_mammal)
    