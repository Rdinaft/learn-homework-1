"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {'Где ты': 'Тут', 'Кто ты': 'Я - это я', 'Зачем': 'Затем', 'Кто я': 'Неважно'}

def ask_user(answers_dict):
   
    print('Задай мне вопрос')
    while True:
        answers_dict = input('').capitalize()
        if answers_dict in questions_and_answers:
            print(questions_and_answers.get(answers_dict))
            break
        else:
            print('again')
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
