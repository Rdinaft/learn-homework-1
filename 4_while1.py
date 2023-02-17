"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    
    print('Здравствуй. Как дела?')
    while True:
        greetings = input('').capitalize()
        if greetings == 'Хорошо' or greetings == 'Нормально':
            break
        else:
            print('Здравствуй. Как дела?')

    
if __name__ == "__main__":
    hello_user()
