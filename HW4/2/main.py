# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}
from collections.abc import Hashable


def rev_kwargs(**kwargs) -> dict:
    kwarg_dict = kwargs
    rev_kwarg_dict = {}
    for kwarg, value in kwarg_dict.items():
        if isinstance(value, Hashable):
            rev_kwarg_dict[value] = kwarg
        else:
            rev_kwarg_dict[str(value)] = kwarg
    return rev_kwarg_dict


if __name__ == '__main__':
    print(rev_kwargs(res=1, reverse=[1, 2, 3]))
