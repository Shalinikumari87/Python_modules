# Tuples are ordered collections of elements.
# tuples are immutable
t = ("apple",2,4.5,True)
print(type(t)) # It is a tuple
print(t[2]) # It will give value of element on 2nd index that is 4.5
# t[0] = "fruit" # Due to its imutuability we can change elements in tuple
print(t) # It wiil throw an error

# 
tup = (1,2,1,2,"jackfruit")
print(tup.count(2)) # It will count the occurence of 2 in elements
print(tup.index(1)) # It will print 1 on 0 index
print(tup*2) # It will repeat the tuples elemts two times
print(tup[0:4]) # we can also do slicing in tuples
print(tup[::-1]) # If we want to reverse tuple

# 
t1 = (1,2,70,40,0)
print(max(t1)) # it will print maximum value in tuple
print(min(t1)) # it will print minimum value in tuple
t2 = (4,5,6,7) # If i have to combine both t1 and t2
t3 = (t1,t2) # nested tuples that means tuple inside tuple
print(t3) 
t0 = (t1 + t2) # It will combine both the tuples
print(t0) 