# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

# Можно с помощью двух циклов
def duplicates_only_cycle(list_with_duplicates: list[int]) -> list[int]:
    out_lst = []

    for i in range(len(list_with_duplicates) - 1):
        for j in range(i + 1, len(list_with_duplicates)):
            if list_with_duplicates[i] == list_with_duplicates[j]:
                out_lst.append(list_with_duplicates[i])
    return list(out_lst)


# Ф можно с помощью генератора списка
def duplicates_only_lst_compr(list_with_duplicates: list[int]) -> list[int]:
    return [list_with_duplicates[i] for i in range(len(list_with_duplicates) - 1) for j in
            range(i + 1, len(list_with_duplicates)) if list_with_duplicates[i] == list_with_duplicates[j]]


if __name__ == '__main__':
    in_list = [1, 2, 3, 1, 2, 4, 5]
    print(duplicates_only_cycle(in_list))
    print(duplicates_only_lst_compr(in_list))
