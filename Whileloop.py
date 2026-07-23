number = 100 
while number > 0:
     print(number)
number = number // 2
command = ""
while command.upper() != "quit":
    command = input(">")
    print("ECHO", command)