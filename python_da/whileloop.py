#While Loops
number = 0
while number < 5:
    print(number)
    number = number + 1

print()

number = 0
while number < 5:
    print(number)
    if number == 3:
        break
    number = number + 1

print()

number = 0
while number < 5:
    print(number)
    if number == 3:
        break
    number = number + 1
else:
    print('No longer < 5')

print()

number = 0
while number < 5:
    number = number + 1
    if number == 3:
        continue 
    print(number)
else:
    print('No longer < 5')