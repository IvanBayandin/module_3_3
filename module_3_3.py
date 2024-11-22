def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params()
print_params(2,4, 'bass')
print_params(False, 55)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = ['Hello', 5.5, 12]
values_dict = {'a': 24, 'b': False, 'c': 'Ivan'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['city', 9]
print_params(*values_list_2, 42)