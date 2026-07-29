#List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
#Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
#Set is an unordered, unindexed collection that prohibits duplicate members; it is unmodifiable, but allows adding new items.
#Dictionary : is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

fruits = ["pineapple", "orange"]
print('fruits:', fruits)
print('Number of fruits:', len(fruits))
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']
print('web_techs:', web_techs)
lst = ['Brian', 250, True, {'country':'Kenya', 'city':'Nairobi'}] # list containing different data types
print('lst', lst)
last_index = len(lst [-1])
last_lst = lst[last_index]
print(last_lst)

#unpacking lists 
lstE = ["Item1", "Item2", "Item3", "Item4"]
first_item, second_item, *rest = lstE
print(first_item)
print(rest)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

#does_exist()...in
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False


#append()
# syntax
lst = list()
lst.append('item')
print('lst', lst)


#insert()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

#remove()
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']

#pop() - The pop() method removes the specified index, (or the last item if index is not specified):
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

#Del() - The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely
fruits_two = ["Orange", "Tangerine", "Peach", "Guave"]
del fruits_two[0]
print('fruits_two', fruits_two)


#clear() - Empties the list
Item = ["item1", "item2"]
print('Item',Item)
Item.clear()
print('Item',Item)

#Copying a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

#joining a list
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

#joining using extend()
ft1 = [1,2,3]
ft2 = [5,7,9]
ft1.extend(ft2)
print('ft1' ,ft1)

#Counting items on a list 
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

#index of an item
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence

#reverse()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)

#sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]

lst = []
print(lst)

lst = [1,2,3,4,5,6]
print(lst)
print(len(lst))

mixed_data_types = ["Brian", 30, 1.87, "Single", "not married"]
print(mixed_data_types)

it_companies = ("Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon")
print(it_companies)
print(len(it_companies))
first_company,second_company,third_company,fourth_company, fifth_company, sixth_company = it_companies

print(first_company)
print(third_company)
print(sixth_company)

it_companies = ["Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies [0] = 'XAI'
print(it_companies)

it_companies.insert(3, 'Yahoo')
print(it_companies)

it_companies = ["Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
does_exist = "Google" in it_companies
print(does_exist)

it_companies = ["Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort(reverse=True)
print(it_companies)

it_companies = ["Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
first_three = it_companies [-3:]
print(first_three)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
coding = front_end + back_end
print(coding)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()


print(ages)
print("Maximum age;", max(ages))
print("Minimum age;", min(ages))

print("Total Age:", min(ages) + max(ages))
median = (ages[4] + ages[5]) / 2
print(median)
average = (sum(ages))/10
print (average)







































