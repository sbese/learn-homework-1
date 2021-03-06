"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит
  пользователя ввести вопрос, а затем, если вопрос есть в словаре,
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""


def ask_user():
    while True:
        question = input("Пользователь: ")
        answer = questions_dict.get(question, "Нет ответа")
        print(f"Программа: {answer}")


if __name__ == "__main__":
    questions_dict = {
        "Как дела": "Хорошо!",
        "Что делаешь?": "Программирую",
        "Чем увлекаешься?": "Программированием",
        "Какая погода?": "Отличная",
    }
    ask_user()

