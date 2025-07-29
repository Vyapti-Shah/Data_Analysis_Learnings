#Group by and Aggreggating
import pandas as pd
df = pd.read_csv(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\files\Flavors.csv')
print(df)

group_by_frame = df.groupby('Base Flavor')
print(group_by_frame)
print(group_by_frame.mean(numeric_only=True)) 
# or
print(df.groupby('Base Flavor').mean(numeric_only=True)) #numeric_only=True tells pandas to ignore any non-numeric columns (like strings) and only calculate the mean for numeric columns (like integers or floats).
print(df.groupby('Base Flavor').count())
print(df.groupby('Base Flavor').min())
print(df.groupby('Base Flavor').max())
print(df.groupby('Base Flavor').sum())

print(df.groupby('Base Flavor').agg({'Flavor Rating': ['mean','max','count','sum'], 'Texture Rating':['mean','max','count','sum'] }))
print(df.groupby(['Base Flavor','Liked']).mean(numeric_only=True))
print(df.groupby(['Base Flavor','Liked']).agg({'Flavor Rating': ['mean','max','count','sum']}))
print(df.groupby('Base Flavor').describe())