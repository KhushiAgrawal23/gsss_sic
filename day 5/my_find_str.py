def find_str(*args): # ('mysuru', 'uru')
    if args[1] == '':
        return 0
    if len(args) == 2:
        j = 0
        #for i, char in enumerate(args[0]):
        for i in range(len(args[0])):
            #print(args[0][i], '  ', args[1][j])
            #print(i, j)
            if j < len(args[1]):
                if args[0][i] == args[1][j]:
                    j += 1
        if j == len(args[1]):
            return i-j+1
        return -1
    if len(args) == 3:
        pass
    if len(args) == 4:
        pass
    else:
        raise TypeError
        
main_str = 'mysuru'
sub_str = 'uru'
print(find_str(main_str, sub_str))
    

