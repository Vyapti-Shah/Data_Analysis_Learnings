#Indexing
import pandas as pd
df = pd.read_csv(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\readingfiles\world_population.csv')
print(df)
df_ = pd.read_csv(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\readingfiles\world_population.csv',index_col=['Country']) #here we are setting the index column (ie first column) as Country
print(df_)

print()

df_.reset_index(inplace=True) #index which was changed to Country is reseted to default ie. numbers
print(df_)
df_.set_index('Country', inplace=True) #index changed to Country
print(df_)

print() 

#loc can be used for string and integer values and iloc works for integer based position values
print(df_.loc['Albania'])
print() 
print(df_.iloc[1])
print() 
df_.reset_index(inplace = True)
print(df_)
df_.set_index(['Continent','Country'], inplace=True) #index changed to Continent and Country
print(df_)
print() 
df_.sort_index() #sorts alphabetically
pd.set_option('display.max.rows', 235)
print(df_)

print() 

print(df_.loc['Africa','Angola'])
print()
print(df_.iloc[1])