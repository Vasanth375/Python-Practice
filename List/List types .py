#List data types
spam=[1,2,3,4,5]#declaring a list
print(spam[1:3])#printing list of slice
#slice means printing or getting subset of original list

#examples
#printing from [first to index 3=4-1]
print(spam[:4])

#printing from index 1 to end of the list
print(spam[1:])

#Adding element from index 1 to all means removing all items from index 
#add only these two values
spam[1:]=["string",9]

print(spam)

#deleting only particular item from list,
del spam[1:2]
print(spam)
