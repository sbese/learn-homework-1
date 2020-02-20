"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def main(str_1, str_2):
    if not (type(str_1) is str and type(str_2) is str):
        return 0
    if len(str_1) == len(str_2):
        return 1
    elif len(str_1) > len(str_2):
        return 2
    elif len(str_1) != len(str_2) and str_2 == "learn":
        return 3


if __name__ == "__main__":
    print(main("123","abc"))
    print(main("1dg23","abc"))
    print(main("123","adfdbc"))
    print(main("123",1))
    print(main(1,"abc"))
    print(main("a","learn"))
