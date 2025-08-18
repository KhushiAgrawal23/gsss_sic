def my_function(num1, num2=0):
    return num1 + num2
print(f'sum = {my_function(10,20)}')
print(f'sum = {my_function(40, 90)}')
print(f'sum = {my_function(num2 = 40, num1 = 90)}')