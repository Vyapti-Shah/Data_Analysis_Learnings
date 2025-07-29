#Converting Data Types
num_int = 7
print(type(num_int))

print()

num_str = '7'
print(type(num_str))

print()

nun_str_conv = int(num_str)
print(type(nun_str_conv))

print()

num_sum = num_int + nun_str_conv
print(num_sum)
print(type(num_sum))

print()

list_type = [1,2,3]
print(type(list_type))
print(type(tuple(list_type)))

print()

list_type = [1,2,3,3,2,1,2,3,2,1]
print(type(set(list_type)))

print()

dict_type = {'name': 'Alex','age': 28, 'hair': 'N/A'}
print(type(dict_type))
print(dict_type.items())
print(dict_type.values())
print(dict_type.keys())
print(type(list(dict_type.keys())))
print(type(list(dict_type.values())))

print()

long_str = "I like to party"
print(set(long_str))