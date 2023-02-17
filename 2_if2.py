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

def main():

    print(comparison('ffd','ffd'))
    print(comparison(2,'tt'))
    print(comparison('learn','d'))
    print(comparison('pytho','learn'))
    print(comparison('pytho','learns'))

def comparison(one, two):

    if isinstance(one, str) and isinstance(two, str):
      if one == two:
        return '1'
      elif len(str(one)) > len(str(two)):
        return '2'
      elif two == 'learn':
        return '3'
    else:
      return '0'

if __name__ == "__main__":
    main()
