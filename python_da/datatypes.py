print(type(-12 + 100)) #integer
print(type(12 + 10.25)) #float
print(type(12 + 3j)) #complex
print(type(1 > 5)) #boolean
print(1 == 1)
print('Single Quote')
print("Double Quote")
multiline = """
The ice cream vanquished
my longing for sweets,
upon this diet I look away,
it no longer exists on this day.
"""
print(multiline)

a = 'Hello World!'
print(a[2:5])
print(a*3)
print(a + a)

#list
print([1,2,3]) 
print(['Cookie Dough','Strawberry','Chocolate'])
print(['Vanilla', 3, ['Scoops','Spoon'],True])

ice_cream = ['Cookie Dough','Strawberry','Chocolate']
ice_cream.append('Salted Caramel')
print(ice_cream)

ice_cream[0] = 'Butter Pecan'
print(ice_cream)

nest_list = ['Vanilla', 3, ['Scoops','Spoon'],True]
print(nest_list[2][1])

#tuple
tuple_scoops = (1,2,3,2,1)
print(tuple_scoops)
print(type(tuple_scoops))
print(tuple_scoops[0])
#tuple_scoops.append(3) #'tuple' object has no attribute 'append'

# sets
daily_pints = {1,2,3}
print(daily_pints)
print(type(daily_pints))

daily_pints_log = {1,2,31,2,3,4,1,2,5,6,3,2}
print(daily_pints_log)

wifes_daily_pints_log = {1,3,5,7,3,24,5,7,3,2,0}
print(daily_pints_log | wifes_daily_pints_log)
print(daily_pints_log & wifes_daily_pints_log)
print(wifes_daily_pints_log - daily_pints_log )
print(wifes_daily_pints_log ^ daily_pints_log )

# dictionaries
# Key/Value Pair
dict_cream = {'name': 'Alex Freberg', 'weekly intake': 5, 'favorite ice creams': ['MCC','Chocolate']}
print(dict_cream)
print(type(dict_cream))
dict_cream.values()
dict_cream.keys()
dict_cream.items()
dict_cream['name']
dict_cream['name'] = 'Christine Freberg'
print(dict_cream)
dict_cream.update({'name': 'Christine Freberg', 'weekly intake': 10, 'weight': 300})
print(dict_cream)
del dict_cream['weight']
print(dict_cream)