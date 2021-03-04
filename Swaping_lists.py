""" swaping two list """

arr1=[1,2,3]

#declaring  list1

arr2=[9,8,7]

#declaring list2

"""swaping statements"""

temp=arr1

arr1=arr2

arr2=temp

print('array 1 is',range(len(arr1)))

#printing range of list

for i in range(len(arr1)):

	print(arr1[i])	

print('array 2 is',range(len(arr1)))

for i in range(len(arr2)):

	print(arr2[i])
