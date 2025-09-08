languages = ['python', 'java', 'c', 'c++', 'react', 'angular']
language_type = ['scrpting', 'oop', 'procedural', 'oop', 'frontend_framework', 'frontend_framework']

print('%-15s %s' % ('LANGUAGE', 'TYPE'))
print('-' * 20)
for i in range(len(languages)):
    print('%-15s %s'%(languages[i] ,language_type[i]))

# print('%08d'%(123456))