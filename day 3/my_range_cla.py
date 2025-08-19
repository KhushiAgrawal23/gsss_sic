import sys

def my_range(*var_args):
    i = 0
    try:
        while i < len(var_args):
            if type(var_args[i]) != int:
                raise ValueError
            i += 1
    except ValueError as e:
        print(f'invalid input {var_args[i]}')
        return
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
    elif len(var_args) == 3 and var_args[0] <= var_args[1]:
        i = var_args[0]
        while i < var_args[1]:
            yield i
            i += var_args[2]
    elif len(var_args) == 3 and var_args[0] >= var_args[1]:
        if var_args[2] >= 0:
            return
        i = var_args[0]
        while i > var_args[1]:
            yield i
            i += var_args[2] 
    else:
        print('invalid input')

i = 0

try:
    numbers = list(map(int, sys.argv[1:]))
except ValueError:
    for number in sys.argv[1:]:
        for element in number:
            if not (element >= '0' and element <= '9'):
                print(f'Invalid input {number}')
                sys.exit('Program ended')
except TypeError:
    pass
except:
    pass

for i in my_range(*numbers):
    print(i, end='  ')