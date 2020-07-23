#input the length of the list
n = int(input("enter the length of list"))

#creating an empty list
list1 = []

#reading the list items from the user
print("entet the list items")
for i in range(n):
    list1.append(int(input("")))

#printing the list
print(list1)


#assigning the list items directly
list2 = [1, 2, 3, 4, 5]

#accessing list items individually
print(list1[0])

#adding new items to the list
list1.append("MyCaptain")
print(list1)

#removing the last item of the list
list1.pop()
print(list1)

#deleting the entire list
del list1
print(list1)
