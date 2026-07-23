# count = 0
# for numbers in range (1,10,):
#     if numbers % 2 == 0:
#         count += 1
#         print (numbers)
# print (f"Total even numbers between 1 and 10 is: {count}")
count = 0
for numbers in range (1,20,):
    if numbers % 2 != 0:
        count += 1
        print (numbers)
        print (f"Total odd numbers between 1 and 20 is: {count}")