#For Loops
integers = [1,2,3,4,5]
for number in integers:
    print(number)


for number in integers:
    print('yep!')


integers = [1,2,3,4,5]
for Jelly in integers:
    print(Jelly + Jelly)


ice_cream_dict = {'name': 'Alex Freberg', 'weekly intake': 5, 'favorite ice creams': ['MCC', 'Chocolate']}
for cream in ice_cream_dict.values():
    print(cream)


for key, value in ice_cream_dict.items():
    print(key, '->',value)


#Nested For Loops
flavors = ['Vanilla', 'Chocolate', 'Cookie Dough']
toppings = ['Hot Fudge', 'Oreos', 'Marshmallows']
for one in flavors:
    for two in toppings:
        print(one, 'topped with', two)