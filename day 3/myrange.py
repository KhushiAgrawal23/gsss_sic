def my_range(*var_args):
    if len(var_args) < 1 or len(var_args) > 3:
        print('TypeError. You gave either 0 or more than 3 Args')
    elif len(var_args) == 1:
        i = 0
        while i < var_args[0]:
            yield i
            i += 1
    elif len(var_args) == 2:
        i = var_args[0]
        while i < var_args[1]:
            yield i
            i += 1
    elif len(var_args) == 3 and var_args[0] < var_args[1]:
        i = var_args[0]
        while i < var_args[1]:
            yield i
            i += var_args[2]
    elif len(var_args) == 3 and var_args[0] > var_args[1]:
        if var_args[2] >= 0:
            return
        i = var_args[0]
        while i > var_args[1]:
            yield i
            i += var_args[2] 
    else:
        print('invalid input')

'''
for i in my_range(sys.argv[1:]):
    print(i, end= ', ')
'''

def my_function(*args):
    print(args)

numbers = []  # we created an empty list
numbers = list()  # we created an empty list
values = [1, 2, 3]
numbers = list(1, 2, 3) # error
numbers = list([1, 2, 3]) # Fine
numbers = list([1, 2, 3], [4, 5]) # Error

numbers = list(1, 2, 3,) # Wrong
numbers = list(values) # Fine

numbers = tuple(1, 20, 3)
my_function(numbers)