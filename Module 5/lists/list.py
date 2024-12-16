# Lists are ordered collection of items which can store zny data type.
# 
lists = ["milk","apple",1,2,3,4]
print(lists[0]) 

# slicing 
list = ["banana","apple","guava",1,2,3]
print(list[0:]) # It will print all the elements starting from 0th index to the last
print(list[0:4]) # If i have print elements from 0th index to 3rd index (4th index will be excluded)
list.append("pineapple") # It will add one element pineaaple in last
print(list) 

# mutuability
l1 = ["ram","shyam","mohan"]
l1[0] ="krishna"
print(l1) # Due to its mutuability we can change elements from list


# Insertion
l = ["brinjal","tomato","potato"]
l.insert(1,"chilly") # It will insert chilly at 1st index
print(l)

# extend : which is used to append element from other list
movies_l = ["KKKG","KGf","Robot"]
movies_l2 = ["Duplicate","pink","jawan"]
movies_l.extend(movies_l2) # It will combine both the lists elements and make one masterlist
print(movies_l)

