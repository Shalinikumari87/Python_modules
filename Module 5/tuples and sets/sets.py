# Sets are unordered collection and unique collection of elements and it does not allow duplicate
#  elements.Due to unorderd collection indexing will not work in sets
s = {1}
print(type(s))
s1 = {1,2,1,2,"mango","mango","mango"} 
print(s1) # It will remove all duplicate elements and prints only unique elements

# set operations
s1 = {"hacking","reading","coding"}
s2 = {"coding","photography","travelling"}
print(s1|s2) # set union: It combine both the set's elements
print(s1 & s2) # set intersection: It will give common elements in both the sets
print(s1 - s2) # set difference: It will print elements that is present in first set not 2nd set
print(s1 ^ s2) # symetric difference: It prints all the element other than common elements

# frozen sets
# immutable version of sets cannot be added or removed any new element
my_fs = frozenset([1,2,2,2,2,3,3,4,])
print(my_fs)