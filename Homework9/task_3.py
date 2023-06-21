# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

with open('test_file/task_3.txt', encoding='utf-8') as f:
    my_list_purchase = []
    purchase = 0
    for i in f.readlines():
        if i != '\n':
            purchase += int(i)
        else:
            my_list_purchase.append(purchase)
            purchase = 0

    my_list_purchase = sorted(my_list_purchase, reverse=True)[:3]

    three_most_expensive_purchases = sum(my_list_purchase)

assert three_most_expensive_purchases == 202346
