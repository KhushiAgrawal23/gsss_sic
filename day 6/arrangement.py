import sys
import pdb

pdb.set_trace()

def check_arrangement(braces):
    arranged = True
    open_count = close_count = 0
    for brace in braces:
        if brace == '{':
            open_count += 1
        else:
            close_count += 1
        if close_count > open_count:
            arranged = False
            break
    if arranged and open_count == close_count:
        return open_count
    return -1

input_str = sys.argv[1]
print(f'User given input is {input_str}')
number_of_pairs = check_arrangement(input_str)
if number_of_pairs != -1:
    print(f'Number of pairs of braces is {number_of_pairs}')
else:
    print('Braces improperly arranged')