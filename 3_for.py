"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по количеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def main():

    print(f'Суммарные продажи всех телефонов составляет {start_value_sum} единиц')
    print(f'Среднее количество продаж всех телефонов составляет {start_value_sum / len(phones)} единиц')

def sum_for_one(sum_sold):

    start_value = 0
    for sum_one in sum_sold:
        start_value += sum_one
    return start_value

def mid_sold_for_one(mid_sold):
    
    start_value = 0
    for mid_one in mid_sold:
        start_value += mid_one
    return start_value / len(mid_sold)

start_value_sum = 0
for phone in phones:
    sum_sell = sum_for_one(phone['items_sold'])
    print(f'Суммарные продажи {phone["product"]} составляет {sum_sell} единиц')
    mid_sell = mid_sold_for_one(phone['items_sold'])
    print(f'Среднее количество продаж {phone["product"]} составляет {mid_sell} единиц')
    start_value_sum += sum_sell
    
if __name__ == "__main__":
    main()
