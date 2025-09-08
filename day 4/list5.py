list1 = [7, 19, 13, 5, 2, 3, 13]

list2 = sorted(list1)
#list1.sort()
print(f'List1 = {list1}') # 
print(f'List2 = {list2}')

value = list1.__str__()
print(value)
print(type(value))
print(list1.__len__())
print(list1.count(130))

print(list1.index(13))
list1.remove(13)
print(list1.index(13))