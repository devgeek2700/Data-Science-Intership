print("Hello")
a = 6
b = 10
y = 'R'
print(type(a))
print(y)
print(a+b)

#condition
if a>3:
    print("big")
else:
    print("small")


#typecasting
e = int(4.67)
print(e)


#string
text = a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(text)

print("\n")

#slicing
str = "Hello World"
str1 = "India!"
print(str[2:7])

#modify string
print(str.upper())
print(str.lower())

#without whitespace
print(str.strip())

print(str+str1)

#String Format ----> takes only number
age = 45
txt = "My name is John, I am {}"
print(txt.format(age))

#boolean
x = 5
y = "Neha"
print(bool(x))
print(bool(y))

#operators

#Exponentiation
m = 8
n = 3
print(m**n)

print("\n")

#List[]  --->  ordered, changeable, and allow duplicate values.

fruits = ["apple", "Mango", "Orange", "apple",[3, 56, "Hello", 'S', 6.345]]
print(fruits)

print(fruits[3])
print(fruits[-3])
l2 = fruits[4][3]
print(l2)

print(fruits[2:5])

#Change Item Value
fruits[2] = "Neha"
print(fruits)

fruits[1:3] = ["blackcurrant", "watermelon"]
print(fruits)

fruits[1:3] = ["watermelon"]
print(fruits)

#Append Items
fruits.append("Pushpa")
print(fruits)

fruits.insert(5,"cherry")
print(fruits)
print(len(fruits))

#Remove items
#Remove
fruits.remove("Pushpa")
print(fruits)

#pop
fruits.pop(1)
print(fruits)

fruits.pop()
print(fruits)

# fruits.clear()
# print(fruits)

print("\n")

#Loop Through a List

#for-in
for x in fruits:
    print(x)

for i in range(len(fruits)):
    print(fruits[2])

i = 0
while(i<len(fruits)):
    print(fruits[i])
    i = i+1

[print(x) for x in fruits]

print("\n")

#List Comprehension
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)
        print(newlist)


print("\n")
#sort
fruits1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits1.sort()
print(fruits1)

fruits1.sort(reverse=True)
print(fruits1)


print("\n")


#Tuples()  --> ordered, unchangeable, and allow duplicate values & diff datatypes.
mytuple = ("apple", "banana", "cherry")
print(mytuple)

print(mytuple[2])
print(mytuple[-2])
print(mytuple[2:4])

#Change :
#1) Convert into a list:

# y = list(mytuple)
# y.append("Neha")
# mytuple = tuple(y)
# print(mytuple)


#2)Add tuple to a tuple
# y = ("orange",)
# mytuple += y
# print(mytuple)

#Unpack Tuples
(x,y,z)= mytuple
print(x)



#Dictionaries{}   ----> keys:value pair   ---> Ordered/Unordered, Changeable, Duplicates Not Allowed
myprofile = {"Name": "Neha", "Branch":"AI&DA", "BOD":2003, "course": "Engg"}
print(myprofile)
print(myprofile["BOD"])
print(myprofile.keys())