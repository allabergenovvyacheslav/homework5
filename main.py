immutable_var= (1, 2, 3, 'Enter', 'Shift')
print(immutable_var)
#immutable_var[3] = 'Delete'
#print(immutable_var)
# TypeError: 'tuple' object does not support item assignment
# Изменить нельзя, потому что кортеж не может обращатся к элементам
mutable_list = [1, 2, 3, "Tab", "Ctrl"]
print(mutable_list)
mutable_list[3] = "Caps Lock"
print(mutable_list)
