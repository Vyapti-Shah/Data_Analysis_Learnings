import pandas as pd
import numpy as np

my_list = [10,25,35]
x = np.array(my_list)
print(x)
print(type(x))
y = pd.Series(my_list)
print(y)
print(type(y))

print()

index_values1 = ['Best','Second Best','Third Best']
my_list1 = [10,25,35]
one = pd.Series(data=my_list1,index=index_values1)
print(one)

print()

index_values2 = ['Best','Second Best','Forth Best']
my_list2 = [10,25,40]
two = pd.Series(data=my_list2,index=index_values2)
print(two)

print()

total = one + two #[(10+10),(25+25),third-NaN,Fourth-NaN]
print(total)
print(type(total))

print()

ice_cream = [['MCC',1],['Butterscotch',2],['Butter Pecan',3]]
ice_cream_dataframe = pd.DataFrame(ice_cream,index=['Flavor 1','Flavor 2','Flavor 3'], columns=('Flavor','Scoops'))
print(ice_cream_dataframe)
print(type(ice_cream_dataframe))

print()

#Another Way:
ice_cream = ['MCC','Butterscotch','Butter Pecan']
scoops = [1,2,3]
dataframe_icecream = {'Flavor': ice_cream, 'Scoops': scoops}
ice_cream_dataframe = pd.DataFrame(dataframe_icecream,index=['Flavor 1','Flavor 2','Flavor 3'] )
print(ice_cream_dataframe) 