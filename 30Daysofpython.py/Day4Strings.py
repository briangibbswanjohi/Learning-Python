#multiline strings
multiline_string = '''I am an SAP Consultant and I enjoy learning at large.
I often do feel with the right motivation and a defined goal it can be very rewarding.
30 days of python has been a walk in the park so far'''
print(multiline_string)

#string concatenation
first_name = 'Brian'
second_name = 'Wanjohi'
space = ' '
fullname = first_name + space + second_name
print(fullname)
print(len(fullname))    

#Escape sequence in strings
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

#formatted string
first_name = "Brian"
second_name = "Wanjohi"
language = "Python"
formated_string = "I am %s %s. I am learning %s" %(first_name, second_name, language)
print(formated_string)

radius = 7
pi = 3.14
area_of_a_circle = pi * radius ** 2 
formated_string = "The area of a circle with a radius %d is pi %.2f." %(radius, area_of_a_circle)
print(formated_string)

#string formating in python 3 
first_name = "Brian"
second_name = "Wanjohi"
language = "Python"
formated_string = "I am {} {}. Learning {}" .format (first_name, second_name, language)
print(formated_string)

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

a = 4
b = 3


print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

#Accessing characters in string by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

#Slicing Python Strings
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon

# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

#Reversing a string
greeting = "Hello World)"
print (greeting [:: -1])

Estate = "Gracelane"
print(Estate [:: -1])

#Skipping Characters While Slicing
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

#capitalize
challenge = 'Thirty days of python'
print(challenge.capitalize)

#count()
challenge = 'Thirty days of python'
print(challenge.count('y'))


#endswith()
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

#expandtabs()
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   
print(challenge.expandtabs(10)) 

#find()
challenge = 'thirty days of python'
print(challenge.find('y')) #rfind does the reverse 

#Break! 





