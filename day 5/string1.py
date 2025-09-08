my_str = 'meghalaya'
print(f'My string = {my_str}') # print the string as it is
print(f'My string = {my_str[::]}') # start from index 0 till last possible index of the string
print(f'My string = {my_str[1:8:]}') # start from index 1 and go till index 7 (No IndexError)
print(f'My string = {my_str[1:8:2]}') # start from index 1 and go till index 7 with a jump of 2