def partition_array(my_list, low, high):
    pivot = my_list[high]
    j = low
    for i in range(low, high):
        if pivot > my_list[i]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            j += 1
    my_list[high], my_list[j] = my_list[j], my_list[high]
    return j