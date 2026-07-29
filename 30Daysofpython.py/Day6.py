#Tupples - () and not modifiable
empty_tuple = ()
print(empty_tuple)

cars = ('BMW', 'BENZ', 'VOLVO', 'NISSAN')
print(cars)
print(len(cars))

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

print(last_fruit)


fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print(last_fruit)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]
print(all_fruits)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]
print(orange_to_the_rest)

#changing tuple to list
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
print(fruits)

fruits = tuple(fruits)
print(fruits)

#checking an item in tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
does_exist = 'banana' in (fruits)
print(does_exist)

#checking item using in 
fruits = ('banana', 'orange', 'mango', 'lemon')
print('banana' in fruits)


#joining tuples
cars = ('Toyota', 'Honda', 'Escalade')
cars2 = ('Caddilac', 'Bugatti', 'Lambo')
all_cars = cars + cars2
print(all_cars)

#del - deleting tuples
cars2 = ('Caddilac', 'Bugatti', 'Lambo')
# del cars2
print(cars2)

#Exercise 
#1 Empty tuple 
laptops = ()
brothers = ('John', )
sister = ('Kelsie', )
siblings = brothers + sister

print(len(siblings))
parents = ('Anne', 'Peter')
family = siblings + parents
print(family)
print(len(family))

#Exercise 2 - Continuation
print(family[1])
print(family[1])

fruits = ('apple' , 'pineapple' )
vegetables = ('tomatoes' , 'kales' )
animal_products = ('butter', 'ghee' )
food_stuff = fruits + vegetables + animal_products
print(food_stuff)


food_stufflst = list(food_stuff)
print(food_stufflst)

food_stufflst = food_stufflst[0:6]
middle_stuff = food_stufflst[2:4]
print(middle_stuff)
rest = food_stufflst[0:2] + food_stufflst[4:9]
print(rest)

food_stufflst = food_stufflst[0:6]
rest2 = food_stufflst[3:6]
print(rest2)

rest3 = food_stufflst[0:3]
print(rest3)

rest4 = food_stufflst[0::2] 
print(rest4)


food_stufflst.clear()
print(food_stufflst)
'ghee' in food_stufflst
print('ghee' in food_stufflst)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'Estonia' in nordic_countries
'Iceland' in nordic_countries
print('Iceland' in nordic_countries)
print('Estonia' in nordic_countries)





















