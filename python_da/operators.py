#Comparison Operators
print(10 == 50)
print(10 != 50)

print('Vanilla' == 'Vanilla')

x = 'Vanilla'
y = 'Chocolate'
print(x != y)

print(10 <= 10)
print(50 >= 10)


#Logical Operators
print((70 > 50) and (50 > 10))
print((10 > 50) or (50 > 10))
print(('Vanilla' > 'Chocolate') and (50 > 10))
print(not(50 > 10))

#Membership Operators
ice_cream = 'I love Chocolate ice cream'
print('love' in 'I love Chocolate ice cream')

scoops = [1,2,3,4,5]
wanted_scoops = 8
print(wanted_scoops in scoops)