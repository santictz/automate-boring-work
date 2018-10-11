#List can contain individual values and list values
spam = ['cat','bat','rat','elephant']
print(spam[1]) #Index of the list

print('Hello ' + spam[0])

#List can contain other list values
print()
spam2 = [['cat', 'bat'],[10,20,30,40]]
print(spam2[0]) #['cat','bat']
print(spam2[1][1]) #20

#Negative indexes start from the end of the list
print()
print(spam[-1])
print(spam2[1][-2])
print('The ' + spam[-1] + ' is afraid of the ' + spam[-2])

#Sublists with slices: create new list values
print()
print(spam[0:4]) #It will not include the last index
print(spam[1:3])
print(spam[:2]) #Can use shortcuts to start from 0 or use the lenght of the list
print(spam[1:])

#Lenght of the list
print()
print(len(spam))

#Change values inside list with indexes
print()
spam[1] = 'aardvaak'
print(spam[1])

#Concatenation and replication
print()
print([1,2,3] + ['X','Y','Z'])
print(['x','y'] * 3)

#Remove values
print()
spam3 = ['Santi','Ago','Cor','Tez']
del[spam3[2]]
print(spam3)