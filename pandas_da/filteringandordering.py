#Filtering and Ordering
import pandas as pd
df = pd.read_csv(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\readingfiles\world_population.csv')
print(df)
print(df[df['Rank'] <= 10]) #prints ranks less than or equal to 10

print()

specific_countries = ['Bangladesh','Brazil']
print(df[df['Country'].isin(specific_countries)])

print(df[df['Country'].str.contains('United')])

print()

print("Filtering")

df_ = df.set_index('Country')
print(df_)
print(df_.filter(items=['Continents','CCA3'],axis=1)) #filters and gives the continents with CCA3
print(df_.filter(items=['Zimbabwe'],axis=0)) #filters and gives Zimbabwe
print(df_.filter(items=['United'],axis=0)) #filters and gives United

print()

print(df_.loc['United States'])

print()

print(df_.iloc[3])

print()

print("Ordering")
print(df[df['Rank'] < 10].sort_values(by=['Rank','Country'],ascending=True)) #the country did not change much becoz the rank is the higher order of importance here so it will be arragned wrt to the rank
print(df[df['Rank'] < 10].sort_values(by=['Country','Rank'],ascending=True))
print(df[df['Rank'] < 10].sort_values(by=['Continent','Country'],ascending=[False,True]))
