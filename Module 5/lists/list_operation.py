# repeated list

l1 = [1,2,3]*5 # It will repeat elements five times
print(l1)

msg = "today is our class \n" # \n is used for creating new line
print(msg*3) # it will print msg 3 times with new line

# Deep copy and shallow copy
# shallow copy: value will change with change in other list
list = [4,5,6,7] 
a=list # a will also refer to same memory location where list is stored
list[1] = 8 # if we cahnges elemnts in list a value will also change due to same memory location
print(a)

# Deep copy : It will change the value in another list
lists = ["guava", "milk",8,9,3]
b = list.copy() # It will cretae a new memory location with same elments that is in list

lists[1] = "butter"
print(lists) # It will change milk to butter and prints
print(b) # It will not change milk to butter because b memory location is different

# Sorted list
a = ["hary","bruce","tony"] # if i have to sort the elements alphabetically
print(sorted(a))
print(a.index("bruce")) # it will show on which index brruce is stored that is 1
print(len(a)) # it will count how many elements are there in lists
print(a.count("bruce")) # it will count the occurence of lists how many times it is in list
print(a.remove("tom")) # it will remove tom from list
print(a.clear()) # it will delete all elememts from lists
print(a.pop()) # it removes one element from last in list




