# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
import itertools

STUFF_DICT = {"Мыло": 0.5,
              "Палатка": 5,
              "Вода": 5,
              "Консервы": 3,
              "Топор": 1.5,
              "Спички": 0.2,
              "Горелка": 4,
              "Одежда": 2,
              "Повербанк": 0.5,
              "Разное": 1.5
              }

# Вместимость маленькая, чтобы было наглядно (иначе получается слишком много комбинаций)
BACKPACK_CAPACITY = 1.7


# Получилось, конечно, сложно, но как есть :)
# Другого не придумал :(
def backpack_kit(stuff: dict[str:int], capacity: float) -> list[list[str]]:
    # Создаем список вещей (из ключей словаря)
    stuff_lst = [item for item in stuff.keys()]
    all_combinations = []

    # Начинаем по нему проходиться
    for i in range(len(stuff_lst)):
        # Делаем временный список первого уровня и убираем элемент, на котором находимся
        tmp_lst = stuff_lst.copy()
        tmp_lst.remove(stuff_lst[i])

        # Начинаем проходиться по копии первого уровня
        for j in range(len(tmp_lst)):
            # Создаем ВСЕ возможные комбинации с разными (в каждом цикле разная длина) -
            # это будет временный список второго уровня (состоящий из списков строк)
            sec_tmp_lst = list(itertools.combinations(tmp_lst, j))

            # Проходим по созданным комбинациям
            for combo in sec_tmp_lst:
                # Считаем суммарный вес комбинации
                counter = 0
                for k in range(len(combo)):
                    counter += stuff[combo[k]]
                # Если он меньше допустимого, добавляем эту комбинацию в список
                if counter <= capacity:
                    if len(combo) > 0:
                        # Преобразуем в списки, чтобы не было пустых занчений в комбинациях
                        combo_lst = list(combo)
                        all_combinations.append(combo_lst)

    # Убираем дубликаты
    valid_combinations = []
    [valid_combinations.append(x) for x in all_combinations if x not in valid_combinations]

    # Сортируем по длине (для наглядности)
    valid_combinations.sort(key=len)

    return valid_combinations


if __name__ == '__main__':
    backpack_combinations = backpack_kit(STUFF_DICT, BACKPACK_CAPACITY)
    for kit in backpack_combinations:
        print(kit)
