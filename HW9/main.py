import math
import random
import csv


"""
Нахождение корней квадратного уравнения
"""
def quad_eq_sol(a: float, b: float, c: float) -> list:
    discr = b ** 2 - 4 * a * c
    solution = []
    if discr > 0:
        solution.append((-b + math.sqrt(discr)) / (2 * a))
        solution.append((-b - math.sqrt(discr)) / (2 * a))
    elif discr == 0:
        solution.append(-b / (2 * a))
    else:
        return solution

    return solution

"""
Случайное число с плавающей запятой в диапазон от 1 до 100
"""
def rand_num_gen() -> float:
    return round(random.random()*random.randint(10, 1000), 2)


"""
Сохранение 3 чисел в файл
"""
def csv_save(nums=3) -> None:
    with open('nums.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(random.randint(100, 1000)):
            rand_nums = (rand_num_gen() for i in range(nums))
            writer.writerow(rand_nums)


if __name__ == '__main__':
    print(quad_eq_sol(1.5, 3.5, 2))
    csv_save()
