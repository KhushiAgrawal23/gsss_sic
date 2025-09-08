def partition_array(my_list):
    pivot = my_list[-1]
    j = 0
    for i in range(len(my_list)-1):
        if pivot > my_list[i]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            j += 1
    my_list[-1], my_list[j] = my_list[j], my_list[-1]

l1 = [34, 223, 22, 31, 1, 100, 50, 40, 22, 72]
print(f'Before Partitioning: {l1}')
partition_array(l1)
print(f'After Partitioning: {l1}')