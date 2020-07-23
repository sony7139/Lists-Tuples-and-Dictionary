#creating a dictionary
d = {'day1':'Sunday', 'day2':'Monday', 'day3':'Tuesday','day4':'Wednesday', 'day5':'Thursday','day6':'Friday'}

print("Printing the dictionary:",end = "\n")
print(d,end = "\n")

#Adding an element to the dictionary
d['day7'] = 'Saturday'
print("After adding an element to dictioanry:",end = "\n")
print(d,end = "\n")

#deleting the third element from the dictionary
del d['day3']
print("after deleting the third element:",end = "\n")
print(d,end = "\n")

#deleting the entire dictionary
del d
print(d)
