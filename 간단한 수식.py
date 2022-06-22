import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

print(2+3*4)
number = 2+3 *4
print(number)
number = number + 2
print(number)
number += 2 
print(number)
number *=2
print(number)
number /=2
number %=2
number -= 2
