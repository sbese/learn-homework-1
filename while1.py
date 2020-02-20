"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    while True:
      user_input = input("как дела? ")
      if user_input == "Хорошо":
        break

    
if __name__ == "__main__":
    ask_user()
