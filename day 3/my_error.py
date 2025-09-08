class AgeError(Exception):
    def __init__(self):
        self.error_msg = "age error occured. Welcome to Mad world"

try:
    age = 25
    print(f'Your age is {age}')
    if age > 18:
        raise AgeError
    else:
        print('Enjoy your life Buddy')
except AgeError as e:
    print(e.error_msg)