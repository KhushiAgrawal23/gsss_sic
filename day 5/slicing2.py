capitals = ['panjim', 'bhubaneswar', 'guwahati', 'aizwal', 'imphal', 'agartala', 'ganktok', 'kohima', 'itanagar', 'shilong']

print(capitals) # by default entire list
print(capitals[1:7]) # by default from beginning to end
print(capitals[2:8:2]) # by default from beginning to end and default increment of 1
#print(capitals[10]) # IndexError
print(capitals[1:17]) # No IndexError in slicing
print(capitals[3:2]) # eMPTY lIST
print(capitals[3:3]) # empty list
print(capitals[3:2:-1])
print(capitals[::3])
print(capitals[-1]) # last element
print(capitals[-11]) # IndexError
print(capitals[-10]) # panjim which is the 1st element in the list with 10 elements.
print(capitals[::-1])
print(capitals[:-15:-1]) # Entire list in reverse with no error
print(capitals[:15:2]) # 
print(capitals[-15:-1:1]) # start from index -15 and go till last but element in forward direction with a jump of 1
 # In slicing, we get to know 3 things. 1st the range, 2nd the amount of jump and 3rd the direction to move.