list1 = [7, 19, 13, 5]
list2 = [2, 3, 13]

list1.extend(list2) # [7, 19, 13, 5, 2, 3, 13]
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)