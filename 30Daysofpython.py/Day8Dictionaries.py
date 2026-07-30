#Dictionaries - A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
#To create a dictionary we use curly brackets, {} or the dict() built-in function.
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

person = {
    'first_name':'Brian',
    'last_name':'Wanjohi',
    'age':30,
    'country':'Kenya',
    'is_marred':False,
    'skills':['SAP', 'Data Analysis', 'Business Intelligence', 'Python'],
    'address':{
        'street':'Grace Lane',
        'zipcode':'02210'
    }
    }
print(person)

print(len(person))

#Accessing Dictionary Items
print(person['first_name'])

#check if a key exist or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.
print(person.get('first_name'))

#Adding item to dict - New key
person['height'] = '187cm'
print(person)

#changing
person['first_name'] = 'Gibbs'
print(person.get('first_name'))

#Adding via append() - An addition to an existing key 
person['skills'].append('HTML') 
print(person.get('skills'))

#Checking Keys in a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

#Removing Key and Value Pairs from a Dictionary
#pop(key): removes the item with the specified key name:
#popitem(): removes the last item
#del: removes an item with specified key name

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
print(dct)

#dct = list(dct)
#print(dct)

dct.clear()
print(dct)

#Copying Dct
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

#getting keya & values as a list
keys = dct.keys()
values = dct.values()
print(keys, values)


#Exercise
dogs = {}
dogs ['Colour'] = 'Brown'
dogs ['Breed'] = 'Spritz'
dogs ['Age'] = 5
print(dogs)

Student = {'First_Name ' : 'Brian', 
           'Second_Name' : 'Gibbs', 
           'Gender' : 'Male',
           'Age' : '29'}

keys = Student.keys()
print(keys)
values = Student.values()
print(values)

Student.pop('Age')
print(Student)
del Student
print(Student)
























