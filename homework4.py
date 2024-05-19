# Списки и кортежи
# 1.
immutable_var = (1,4,True, [125, 404, 8], 'tasks')
print(immutable_var)
# 2. Так как кортеж - неизменяемый тип данных, будет возникать
# ошибка при попытке изменить данные внутри кортежа (кортеж не поддерживает обращение по элементам)
immutable_var[0] = 8
print(immutable_var)
# 3.
mutable_list = [5, 150, 9 ,652, 'name']
print(mutable_list)
mutable_list.append('last_name')
print(mutable_list)

