def int_check(number: str) -> int:
    try:
        return int(number)
    except ValueError:
        print("Вы ввели не число! Повторите ввод!")
        return int_check(input())


def user_input() -> tuple:
    print("Введите стороны треугольника:")
    a = int_check(input("a = "))
    neg_raiser(a)
    b = int_check(input("b = "))
    neg_raiser(b)
    c = int_check(input("c = "))
    neg_raiser(c)
    return a, b, c


class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self._a = a
        self._b = b
        self._c = c
        if self._a == self._b and self._a == self._c:
            self._property = "равносторонний"
        elif (self._a ** 2 == self._b ** 2 + self._c ** 2
              or self._b ** 2 == self._a ** 2 + self._c ** 2
              or self._c ** 2 == self._b ** 2 + self._a ** 2):
            self._property = "прямоугольный"
        else:
            self._property = "разносторонний"

    def __str__(self) -> str:
        return f"Треугольник со сторонам: {self._a}, {self._b}, {self._c}, он {self._property}."

    def check(self) -> bool:
        if (self._a > self._b + self._c
                or self._b > self._a + self._c
                or self._c > self._b + self._a):
            print("Нет такого треугольника! Повторите ввод!")
            return False
        return True


def make_triang() -> Triangle:
    a, b, c = user_input()
    new_triang = Triangle(a, b, c)
    while not new_triang.check():
        a, b, c = user_input()
        new_triang = Triangle(a, b, c)
    return new_triang


class NegativeSidesError(Exception):
    def __init__(self, text, side):
        self.txt = text
        self.side = side


def neg_raiser(side: int) -> None:
    if side < 0:
        neg_error = NegativeSidesError(f"Сторона меньше нуля: {side}. Повторите ввод!", side)
        raise neg_error


if __name__ == '__main__':
    my_triang = make_triang()
    if my_triang is None:
        my_triang = make_triang()
    else:
        print(my_triang)
