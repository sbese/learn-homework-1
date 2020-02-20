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
            print("\nПрограмма: Пока!")
            break
        answer = questions_dict.get(question, "Нет ответа")
        print(f"Программа: {answer}")
     
if __name__ == "__main__":
    questions_dict = {
         "Как дела?": "Хорошо!", 
         "Что делаешь?": "Программирую",
         "Чем увлекаешься?": "Программированием",
         "Какая погода?": "Отличная"
         }
    ask_user()
