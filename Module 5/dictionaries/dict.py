# Dictionary: It is a data structure that stores data as key value pair
            #   keys are unique and immutable

d = {"name":"zara","email":"za@gmail.com","contact": 1234}
print(d)
print(d["name"]) 
d["name"] = "sara" # If i have to change the name
print(d)

# note: Only string and numbers can be used as key of dictionary
d = {"name":"zara","email":"za@gmail.com","contact": 1234}
d["adress"] = "banglore" # If i have to add adress 
print(d)
del d["adress"] # To delete key velue
print(d)
d.clear() # it will give a empty dictionary
print(d)
d1 = d.copy # It will copy the dictinary 
print(d)

