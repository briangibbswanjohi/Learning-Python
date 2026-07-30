#if - check if a condition is true and to execute the block code
#else - If condition is true the first block will be executed, if not the else condition will run.
a = 3
if a > 6:
    print('A is a positive number')
else:
    print('A is a negative number')

# if Elif Else
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

#Shorthand
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

#Nested loops
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

#If Condition and Logical Operators - We can avoid writing nested condition by using logical operator and.
a = 0 
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
else:
    print('A is zero')


#If and Or Logical Operators - If one condition is met
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')


# Rubber meets the road:
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive')
else: 
    print('Wait till', 18 - age, 'years to drive')

your_age = int(input("Enter your age: "))
my_age = 30

if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")

elif my_age == your_age:
    print("We are the same age.")

else:
    difference = my_age - your_age
    if difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {difference} years older than you.")

a = int(input('Enter num: '))
b = int(input('Enter num2: '))

if a > b: 
    print(f"{a} is greater than {b}")
elif b > a: 
    print(f"{b} is greater than {a}")
else: 
    print(f'{a} is equal to {b}')



score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")

elif score >= 90:
    print(f"{score} is an A")

elif score >= 80:
    print(f"{score} is a B")

elif score >= 70:
    print(f"{score} is a C")

elif score >= 60:
    print(f"{score} is a D")

elif score >= 50:
    print(f"{score} is an E")

else:
    print(f"{score} is an F")


autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']

Month = input('Enter Month: ')

if Month in autumn:
    print('The season is Autumn')
elif Month in winter: 
    print('The season is Winter')
elif Month in spring: 
    print('The season is Spring')
elif Month in summer: 
    print('The season is Summer')
else: 
    print('Month is invalid')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit:').lower()
if fruit in fruits: 
    print('That fruit already exists in the list')
else: 
    fruits.append(1,fruit)
    print(fruits)

person={
    'first_name': 'Brian',
    'last_name': 'Gibbs',
    'age': 29,
    'country': 'Kenya',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    skills = person['skills']
    middle = len(skills) // 2
    print(skills[middle])

len(skills) // 2

if 'skills' in person:
    print('Python' in person['skills'])


if 'skills' in person:
    skills = person['skills']

    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print("He is a front end developer")

    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("He is a backend developer")

    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("He is a fullstack developer")

    else:
        print("Unknown title")

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")











