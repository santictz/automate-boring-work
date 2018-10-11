#List.Index
words = ['hello', 'hi', 'howdy', 'heyas','hi']
print(words.index('hello')) #0
print(words.index('heyas')) #3
print(words.index('hallo')) #Error
print(words.index('hi')) #1, only the first ocurrence

#List.Append
animals = ['cat','dog','bat']
animals.append('moose') #Add moose at the end of the list

#List.Insert
animals.insert(2,'chicken') #Add chicken at index 2

#List.Remove
animals.remove('cat') #Delete the value in the list

#List.Sort
numbers = [2,5,3.14,1,-7]
numbers.sort()
numbers.sort(reverse=True) #Reverse=True sort the values in reverse order
names = ['Alice','ants','Bob','badgers','Carol','cats']
names.sort() #['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats'] Uppercases are first
names.sort(key=str.lower) #This threats all strings as lower cases