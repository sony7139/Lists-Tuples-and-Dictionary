#input the length of the list
n = int(input("enter the length of list"))
list1 = []
#reading the list items from the user
print("entet the list items")
for i in range(n):
    list1.append(int(input("")))
print(list1)
print()

#assigning the list items directly
list2 = [1, 2, 3, 4, 5,'hello']

#creating a tuple
tuple1 = (2, 4, 6, 8, 10,'python', 'tuple')

#accessing the elements from a tuple
print("The first element of the tuple is: ")
print(tuple1[0])
if tuple1[0] == 2:
    print("the tuple1 elements are being accessed")
print()
      
#creating a dictionary
d = {'day1':'Sunday', 'day2':'Monday', 'day3':'Tuesday','day4':'Wednesday', 'day5':'Thursday','day6':'Friday'}

print("Printing the dictionary:",end = "\n")
print(d)

#Adding an element to the dictionary
d['day7'] = 'Saturday'
print("After adding an element to dictioanry:",end = "\n")
print(d)
#deleting the first elemnet from the dictionary
del d['day1']
print("after deleting the first element:",end = "\n")
print(d)


