names3 = ['suresh', 'mahesh', 'girish']

names4 = names3 # Shallow Copy (We copy only the address of the list)

print('Names3 = ', names3)
print('Names4 = ',names4)

names3[2] = 'harish'
print('Names4 = ',names4)