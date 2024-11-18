# Создайте вручную список содержащий элементы разных типов.
# Получите из него словарь списков, где ключ - тип элемента,
# а значение - список элементов данного типа.
# Для списка: [1, 2, "3", "4", True, 5.5]
# Ответ:  {int: [1, 2, 5], float: [5.5], str: ["3", "4"], bool: [True]}

lst = [1, 2, "3", "4", True, 5.5]
type_elem = {}
for elem in lst:
    if type(elem) in type_elem:
        type_elem[type(elem)].append(elem)
    else:
        type_elem[type(elem)] = [elem]

print(type_elem)