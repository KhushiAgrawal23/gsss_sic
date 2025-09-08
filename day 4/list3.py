list1 = [7, 19, 13, 5]
list2 = [2, 3, 13]

print(list1.extend(list2)) # [7, 19, 13, 5, 2, 3, 13]
print(list1)
list1.append(list2) # [7, 19, 13, 5, [2, 3, 13] ]
print(list1)