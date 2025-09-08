def my_function(num1, num2 = 100):
    return num1 + num2

def my_function(num1 = 100, num2 = 400):
    return num1 - num2

def my_function1(num1 = 50, num2): # Error
    return num1 + num2

print(f'Sum = {my_function(10, 20)}')
print(f'Sum = {my_function(40, 90)}')
print(f'Sum = {my_function(num1 = 11, num2 = 90)}')
print(f'Sum = {my_function(num2 = 0, num1 = 90)}')
print(f'Sum = {my_function(10)}')
print(f'Sum = {my_function(40, 90)}')