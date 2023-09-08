import csv


class NameDescriptor:
    def __init__(self):
        self.__value = ''

    def __get__(self, instance, owner):
        return instance.__value

    def __set__(self, instance, value):
        if value.isalpha() is False:
            raise ValueError(f"Incorrect name!")
        if value.istitle() is False:
            raise ValueError(f"Name must start from a title letter!")
        instance.__value = value


class SurnameDescriptor:
    def __init__(self):
        self.__value = ''

    def __get__(self, instance, owner):
        return instance.__value

    def __set__(self, instance, value):
        if value.isalpha() is False:
            raise ValueError(f"Incorrect surname!")
        if value.istitle() is False:
            raise ValueError(f"Surname must start from a title letter!")
        instance.__value = value


class LastnameDescriptor:
    def __init__(self):
        self.__value = ''

    def __get__(self, instance, owner):
        return instance.__value

    def __set__(self, instance, value):
        if value.isalpha() is False:
            raise ValueError(f"Incorrect lastname!")
        if value.istitle() is False:
            raise ValueError(f"Lastname must start from a title letter!")
        instance.__value = value


class Student:
    __name = NameDescriptor()
    __surname = SurnameDescriptor()
    __lastname = LastnameDescriptor()

    def __init__(self, name, surname, lastname):
        self.__name = name
        self.__surname = surname
        self.__lastname = lastname
        self.__file = f'{self.__surname}{self.__name}{self.__lastname}.csv'
        self.__avg_test_res = {}
        self.__avg_mark = 0
        self.__les_and_res = self.__get_les_and_res_from_csv()

    def __str__(self):
        out_str = f'ФИО: {self.__surname} {self.__name} {self.__lastname}' \
                  f'\nAvg. mark: {self.__avg_mark}\nTest results:\n'
        for lesson, test_res in self.__avg_test_res.items():
            out_str += f'\t{lesson}: {test_res}\n'
        return out_str

    def __get_les_and_res_from_csv(self):
        results = []
        with open(self.__file, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            marks = 0
            for row in reader:
                lesson = row[0]

                mark = row[1]
                marks += int(mark)

                test_res = [int(item) for item in row[2].split('-')]
                self.__avg_test_res[lesson] = round(sum(test_res) / len(test_res), 1)

                results.append({lesson: (mark, test_res)})
            self.__avg_mark = round(marks / len(results), 1)
        return results


if __name__ == '__main__':
    my_st = Student('Андрей', 'Михеев', 'Сергеевич')
    print(my_st)
