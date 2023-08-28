import math
import random
import csv

"""
Декоратор для нахождения корней с каждой тройкой чисел из csv-файла
"""
def quad_eq_csv_decorator(func_to_decorate):
    def wrapper():
        with open('nums.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                num_lst = [float(row[i]) for i in range(len(row))]
                if num_lst:
                    sol = func_to_decorate(num_lst)
                    if sol:
                        print(f'a={num_lst[0]}, b={num_lst[1]}, c={num_lst[2]}\nРешение: {sol}\n')
                    else:
                        print('Решения нет!\n')
    return wrapper


"""
Нахождение корней квадратного уравнения
"""
@quad_eq_csv_decorator
def quad_eq_sol(nums: list[float]) -> list:
    a = nums[0]
    b = nums[1]
    c = nums[2]
    discr = b ** 2 - 4 * a * c
    solution = []
    if a != 0:
        if discr > 0:
            solution.append((-b + math.sqrt(discr)) / (2 * a))
            solution.append((-b - math.sqrt(discr)) / (2 * a))
        elif discr == 0:
            solution.append(-b / (2 * a))
        else:
            return solution
    else:
        solution.append(-c/b)
    return solution


"""
Случайное число с плавающей запятой в диапазон от 1 до 100
"""
def rand_num_gen() -> float:
    return round(random.random() * random.randint(10, 1000), 1)


"""
Сохранение 3 чисел в файл
"""
def csv_save(nums=3) -> None:
    with open('nums.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(random.randint(100, 1000)):
            rand_nums = [rand_num_gen() for i in range(nums)]
            writer.writerow(rand_nums)


if __name__ == '__main__':
    csv_save()
    quad_eq_sol()
