#Set - Collection of items (unordered & unindexed - used to store unique items)
#It's possible to find the union, intersection, difference, subset, super set and disjoint set among sets
#Empty set : st = set ()

st = {'Item1', 'Item2', 'Item3', 'Item4'}
len(st)
print(len(st))

#Accessing items in a set - We use loops
print('Does set contain Item1?', 'Item1' in st)

#Adding item to a set - Using Add()
st.add('Item5')
print(st)

#adding multiple items using update()
st.update(['Item6', 'Item7', 'Item8'])
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

#removing items from a set : remove()
fruits.remove('tomato')
print(fruits)

# #pop () -removes random item
fruits.pop()
print(fruits)

#finding the removed item
removed_item = fruits.pop()
print(removed_item)

#clearing set using clear()
st.clear()
print(st)

#deleting a set using del()
# del st
print(st)

# converting list to set
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered

#joining sets - can be done using union() or update() or |
cars = {'lambo', 'nissan', 'chevy', 'ferrari', 'vw'}
bikes = {'kawasaki', 'ducatti', 'honda', 'harley'}
# cars.update(bikes)
# print(cars)

vehicles = cars.union(bikes)
print(vehicles)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
# or using this : print(fruits | vegetables

#finding intersections - returns a set of items which are in both the sets or using & symbol. See the example
st1 = {1, 2, 3, 4, 5}
st2 = {5, 4, 6, 7, 8}
st1.intersection(st2)
print(st1.intersection(st2))

#checking subset & superset
#subset = issubset()
#superset = issuperset
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
print(st2.issubset(st1))
print(st1.issubset(st2))
print(st1.issuperset(st2))

#finding the difference
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1
st2-st1
print(st1 - st2)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# dragon - python

#Finding Symmetric Difference Between Two Sets - returns the symmetric difference between two sets 
#It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
python ^ dragon
print(python.symmetric_difference(dragon))
print(whole_numbers.symmetric_difference(some_numbers))

#Joining Sets - If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
print(st2.isdisjoint(st1))

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item
print(even_numbers.isdisjoint(odd_numbers))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
print(python.isdisjoint(dragon))

#Exercise
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#len of set It_companies
print(len(it_companies))

#Adding twitter to It_companies - Single update so used add()
it_companies.add('Twitter')
print(it_companies)

#Adding Multiple companies - update ([])
it_companies.update(['Yahoo', 'Bing'])
print(it_companies)

it_companies.remove('Twitter')
print(it_companies)

#Exercise 2
st = {1, 3, 5, 7, 9}
st1 = {2, 4, 6, 8, 10}
# st2 = st.union(st1)
# print(st2) - To Return new set

st.update(st1)
print(st)

#intersection
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)
print(python.intersection(dragon))

python.isdisjoint(dragon)
print(python.isdisjoint(dragon))

comb = python.union(dragon)
print(comb)

python.symmetric_difference(dragon)
print(python.symmetric_difference(dragon))
# del (python)
# print(python)
# del (dragon)
# print(dragon)

#Exercise3
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
age = set(age)
print(age)

print(len(age))

text = 'I am a teacher and I love to inspire and teach people'
words = text.split()
words =set(words)
print(len(words))




















