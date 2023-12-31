# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
import os


# Затычка для сохранения
def reader() -> tuple[int,int, list]:
    if os.path.exists("saved.txt"):
        line_counter = 0
        operations = []
        with open("saved.txt", "r") as file:
            for line in file:
                line_counter += 1
                if line_counter == 1:
                    money = line.split(",")[0]
                    counter = line.split(",")[1]
                else:
                    operations.append(line. strip('\n'))
        money = num_str_to_int(money)
        counter = num_str_to_int(counter)
    else:
        return 0, 0, []
    return money, counter, operations


# Статический метод для проверки на целое число
def int_check(number: str) -> bool:
    try:
        int(number)
        return True
    except ValueError:
        return False


# Статический метод для перевода строки в целое число
def num_str_to_int(number: str) -> int:
    while not int_check(number):
        number = input("Вы ввели не цифру! Повторите!\n")
    return int(number)


class ATM:
    # Конструктор
    def __init__(self, money_in=0, counter=0, operations=None):
        self._money_in = money_in
        self._op_counter = counter

        if operations is None:
            self._operations = []
        else:
            self._operations = operations

    # Печать
    def __str__(self):
        out_str = f"На счету: {round(self._money_in, 2)} у.е.\n История операций:\n"
        for operation in self._operations:
            out_str += f'{operation}\n'

        return out_str

    # Сохранение операции
    def save_operation(self, operation_name: str, value: int, result: bool):
        self._operations.append(f"Операция: {operation_name}; сумма: {value}; результат: {result}")

    # Геттеры для полей
    def get_money(self) -> int:
        return self._money_in
    def get_counter(self) -> int:
        return self._op_counter
    def get_operations_str(self) -> str:
        op_str = '\n'
        for operation in self._operations:
            op_str += f"{operation}\n"
        return op_str

    # Снятие комиссии для богатых
    def rich_commission(self, percent=10, rich_factor=5_000_000) -> None:
        if self._money_in > rich_factor:
            tax = round((self._money_in * percent) / 100, 2)
            self._money_in -= tax
            print(f"Списан налог на богатство в размере: {tax}")

    # Добавление процента на остаток
    def add_depo(self, percent=3, counter_value=2) -> None:
        if self._op_counter == counter_value:
            depo = round((self._money_in * percent) / 100, 2)
            self._money_in += depo
            self._op_counter = 0
            print(f"Начислен процент на остаток в размере: {depo}")
        else:
            self._op_counter += 1

    # Статический метод для проверки на кратность 50
    def multiple_amount(self, number: int, multiplicator=50) -> bool:
        if number % multiplicator == 0:
            return True
        return False

    # Расчет комиссии при снятии
    def commission_calc(self, withdraw_amount: int, commission=1.5, min_com=30, max_com=600) -> float:
        rated_commission = round((withdraw_amount * commission) / 100, 2)
        if min_com < rated_commission < max_com:
            return rated_commission
        elif rated_commission < min_com:
            return min_com
        return max_com

    # Внесение денег на счет
    def add_money(self, amount: int) -> None:
        self.rich_commission()
        if self.multiple_amount(amount):
            self._money_in += amount
            print(f"Вы пополнили счет на: {amount} у.е.")
            self.add_depo()
            self.save_operation("Пополнение", amount, True)
        else:
            print("Сумма пополнения должна быть кратна 50 у.е. Операция отменена.")
            self.save_operation("Пополнение", amount, False)
        print(self)

    # Снятие денег со счета
    def withdraw_money(self, amount: int) -> None:
        self.rich_commission()
        if self.multiple_amount(amount):
            commission = self.commission_calc(amount)
            if amount + commission > self._money_in:
                print("На счете недостаточно средств. Введите другую сумму.")
                self.save_operation("Снятие", amount, False)
            else:
                self._money_in -= amount + commission
                print(f"Снято: {amount} у.е., комиссия за снятие: {commission}.")
                self.add_depo()
                self.save_operation("Снятие", amount, True)
        else:
            print("Сумма снятия должна быть кратна 50 у.е. Операция отменена.")
            self.save_operation("Снятие", amount, False)

        print(self)


# Главное меню программы в виде статического метода
def main_menu(atm: ATM):
    print("Главное меню::")
    print("1 - Внести сумму")
    print("2 - Снять сумму")
    print("3 - Выход")

    inp_com = input("Введите действие: ")
    inp_com = num_str_to_int(inp_com)

    if inp_com == 1:
        in_amount = input("Введите сумму: ")
        in_amount = num_str_to_int(in_amount)
        atm.add_money(in_amount)
        return main_menu(atm)

    elif inp_com == 2:
        withdraw_amount = input("Введите сумму: ")
        withdraw_amount = num_str_to_int(withdraw_amount)
        atm.withdraw_money(withdraw_amount)
        return main_menu(atm)

    elif inp_com == 3:
        print(atm)
        print("До свидания!")
        with open("saved.txt", "w+") as file:
            file.write(f"{atm.get_money()}, {atm.get_counter()}, {atm.get_operations_str()}")
        exit()

    else:
        print("Нет такой команды!")
        return main_menu(atm)


if __name__ == '__main__':
    saved_money, saved_counter, saved_operations = reader()
    new_ATM = ATM(saved_money, saved_counter, saved_operations)
    main_menu(new_ATM)
