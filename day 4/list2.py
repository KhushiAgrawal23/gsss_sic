names3 = ['suresh', 'mahesh', 'girish']

names4 = list(names3) # Deep Copy (We make a duplicate copy of the existing list)

print('Names3 = ', names3)
print('Names4 = ',names4)

names3[2] = 'harish'
print('Names4 = ',names4)
print('Names3 = ', names3)