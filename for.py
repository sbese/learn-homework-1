"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

import random


def main():
    school_scores_sum = 0
    school_scores_count = 0
    for scholl_class in school:
        class_scores_sum = sum(scholl_class["scores"])
        class_scores_count = len(scholl_class["scores"])
        print(class_scores_sum/class_scores_count)
        school_scores_sum += class_scores_sum
        school_scores_count += class_scores_count
    print(school_scores_sum/school_scores_count)


if __name__ == "__main__":
    school = [{"school_class": f"{x}a",  "scores": [random.randint(
        2, 5) for y in range(random.randint(5, 15))]} for x in range(1, 12)]
    print(school)
    main()
