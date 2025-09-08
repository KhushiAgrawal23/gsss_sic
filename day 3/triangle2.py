def draw_triangle(number_of_lines):
    for i in range(number_of_lines):
        print(' ' * (number_of_lines-i-1), end='')
        print('*' * (2 * i + 1))
 
draw_triangle(9)