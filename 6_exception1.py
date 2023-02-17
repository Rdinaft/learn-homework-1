"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
   
    try:
        print('Здравствуй. Как дела?')

        while True:
            greetings = input('').capitalize()
            if greetings == 'Хорошо' or greetings == 'Нормально':
                break
            else:
                print('Здравствуй. Как дела?')
    except KeyboardInterrupt:
        print('Ну давай!')
    
if __name__ == "__main__":
    hello_user()
