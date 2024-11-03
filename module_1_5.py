immutable_var = 1, 2, 3, 'string', 0.5, True
print(immutable_var)
#immutable_var[5] = 4
#мы не можем изменить значение элементов кортежа так как сам кортеж не поддерживает обращение по элементам
mutable_list = [11, False, 'league', 1.3]
print(mutable_list)
mutable_list[2] = 'string'
print(mutable_list)
print(mutable_list[1])
mutable_list.append('Modified')
print(mutable_list)