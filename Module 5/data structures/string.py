# String is a sequence of character where character is a single unit of text which is helpful to
# represent and manipulate textual data.

# concatnation of string
print("hello" + "world") # It will conceate strings.

# Slicing of string.
string1 = "I am a student" # if i have to print I to am only we count indexes of I on 0th index,
                            # space on 1st index,a on 2nd index and m on 3rd index
                            # but we have to take till 4th index then it will give value to third index.
                            
print(string1[0:4])
print(string1[3:]) #it will print 3rd index to last index

# print all character except last three character.
str = "pwskills"
print(str[:-3]) #it will print only pwski because we have excluded 3 characters from last
                # s on -1, l on -2 and l on -3

print(str[-3:]) #it will print only last three character which is lls

print(str[::-1])# it will reverse thr string and output will be sllikswp
print(len(str)) # it will give count of character in string and output will be 8

# strings are immutable because we cannot change one character from string
s = "apple"
s[0] = 'p'
print(s) #it will throw an error due to strings immutability concept.


