
#Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
#Введите элементы 2-го списка: 2,5
#Результат: 1,3,4
list1 = input('Введите любые цифры через запятую:').split(',')###пользователь вводит элементы 1-го списка
list2 = input('Введите любые цифры через запятую:').split(',')#вводит элементы 2-го списка
#удалить из первого списка элементы присутствующие во 2-ом
result = [item.strip() for item in list1 if item.strip() not in list2]
print(result)

