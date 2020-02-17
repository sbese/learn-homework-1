"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def ask_user():
     while True:
        try:
            question = input("Пользователь: ")
        except KeyboardInterrupt:
            print("Пока!")
            break
        if question in questions_dict.keys():
            print(f"Программа: {questions_dict[question]}")
        else:
            print(f"Программа: Нет ответа")
     
if __name__ == "__main__":
    questions_dict = {
         "Как дела": "Хорошо!", 
         "Что делаешь?": "Программирую",
         "Чем увлекаешься?": "Программированием",
         "Какая погода?": "Отличная"
         }
    ask_user()
