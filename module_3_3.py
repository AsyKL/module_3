def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(2,'qwerty', c = False)
values_list = [5, 'string', 3.5]
values_dict = {'a': 8, 'b': 9, 'c': 0}
print_params(*values_list)
print_params(**values_dict)