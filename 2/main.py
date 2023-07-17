# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def check(a, b, c):
    if (a > b + c
            or b > a + c
            or c > b + a):
        print("Нет такого треугольника! Повторите ввод!")
        return False


def int_check(number):
    try:
        return int(number)
    except ValueError:
        print("Вы ввели не число! Повторите ввод!")
        return int_check(input())


def user_input():
    print("Введите стороны треугольника:")
    a = int_check(input("a = "))
    b = int_check(input("b = "))
    c = int_check(input("c = "))
    return a, b, c


class Triangle:
    def __init__(self, a, b, c):
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

    def __str__(self):
        return f"Треугольник со сторонам: {self._a}, {self._b}, {self._c}, он {self._property}."


def make_triang():
    a, b, c = user_input()
    if not check(a, b, c):
        a, b, c = user_input()
    new_triang = Triangle(a, b, c)
    return new_triang


if __name__ == '__main__':
    my_triang = make_triang()
    if my_triang is None:
        my_triang = make_triang()
    else:
        print(my_triang)
