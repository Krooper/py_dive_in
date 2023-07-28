# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
# (Может помочь метод translate из модуля string)


# Создаем словарь со всеми символами и числом повторений каждого
import re


def symbols_counter(in_str: str) -> dict[str:int]:
    symbol_dict = {}
    for symbol in in_str:
        if symbol in symbol_dict.keys():
            symbol_dict[symbol] += 1
        else:
            symbol_dict[symbol] = 1
    return symbol_dict


# Получаем список из наибольших повторений длиною 10 или меньше
def most_frequent_lst(symbols: dict[str:int]) -> list[int]:
    freq_lst = [frequency for frequency in symbols.values()]
    freq_lst.sort()
    if len(freq_lst) >= 10:
        return freq_lst[-10:]
    return freq_lst


# Получаем словарь с 10-ю (или меньше) самыми популярными символами и их кол-ом повторений
def most_popular_symbols(symbols: dict[str:int], freq_lst: list[int]) -> dict[str:int]:
    most_freq_symbols = {}
    for symbol, frequency in symbols.items():
        for freq in freq_lst:
            if symbols[symbol] == freq:
                most_freq_symbols[symbol] = frequency
    return most_freq_symbols


# Парсер строк
# По итогу, не очень разобрался с translate(), поэтому сделал так
def str_parser(str_to_parse: str) -> str:
    return re.sub(r'[^\w]|_', '', str_to_parse).lower()


if __name__ == '__main__':
    # Строка для примера
    my_str = "QQ, wwweeEe , rr:?*()№%:\";_+-=?><|}{:?%!*;'RRrttttttyyyyyyyuuuuuuuu!!!iiiiiiiii   oooooooooo LLLLl Jkdsa"
    symbols_and_freq = symbols_counter(str_parser(my_str))
    print(most_popular_symbols(symbols_and_freq, most_frequent_lst(symbols_and_freq)))
