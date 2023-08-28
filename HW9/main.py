import math
import random
import csv
import json
"""
Декоратор для записи параметров и результата в json (получается как бы "декоратор для декоратора")
"""
def json_save(func_to_decorate):
    def json_wrapper():
        data = func_to_decorate()
        json_data = json.dumps(data, indent='\t')
        with open('data.json', 'w') as json_file:
            json_file.write(json_data)
    return json_wrapper


"""
Декоратор для нахождения корней с каждой тройкой чисел из csv-файла
"""
def quad_eq_csv_decorator(func_to_decorate):
    def eq_wrapper():
        sol_dict = {}
        with open('nums.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                num_lst = [float(row[i]) for i in range(len(row))]
                if num_lst:
                    sol = func_to_decorate(num_lst)
                    print(f'a={sol[0]}, b={sol[1]}, c={sol[2]}\nРешение: {sol[3]}\n')
                    sol_dict[f'{sol[0]}, {sol[1]}, {sol[2]}'] = sol[3]
        return sol_dict
    return eq_wrapper


"""
Нахождение корней квадратного уравнения
"""
@json_save
@quad_eq_csv_decorator
def quad_eq_sol(nums: list[float]) -> tuple:
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
            return a, b, c, 'No solution'
    else:
        solution.append(-c/b)
    return a, b, c, solution


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
