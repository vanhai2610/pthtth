# print ('Hello World')
# x=2
# print(1<x<3)
# print(10<x<5)
#--------------example1----------------
for letter in 'Industrial':
    print ('Current letter :',letter)

#--------------example2----------------
fruits = ['apple', 'mango','strawberry','durian','dragon fruit']
for fruit in fruits:
    print('current fruit : ', fruit)

#---------example3--------
count = 0
while (count < 5):
    print ('The count is:', count)
    count = count + 1

#--------example4-------
str = 'Hello world'
newstr = str.replace('Hello', 'Bye')
print (newstr)
print(str.find('world'))
print(str.split(' '))
print(str.isnumeric())
print(str.upper())
print(fruits[0])
print(len(fruits))