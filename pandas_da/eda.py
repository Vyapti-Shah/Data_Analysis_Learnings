#Exploratory Data Analysis in Pandas 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\files\world_population.csv')
print(df)
pd.set_option('display.float_format',lambda x: '%.2f' % x)
print(df)

df.info()
print(df.describe())
print(df.isnull().sum())
print(df.nunique()) #how many unique values are there in each columns

print(df.sort_values(by='World Population Percentage',ascending=False).head(10))

print(df[df['Continent'].str.contains('Oceania')])

print(df.corr(numeric_only=True)) #numeric_only=True for numerical values and .corr() calculates how much related are the values in different columns

sns.heatmap(df.corr(numeric_only=True), annot = True)
plt.rcParams['figure.figsize'] = (20,7)
plt.show()

df1 = df.groupby('Continent').mean(numeric_only=True).sort_values(by="2022 Population",ascending=False)
print(df1)
df1.plot()
plt.show()

df1_ = df1.transpose()
print(df1_)
df1_.plot()
plt.show()

print(df.columns)

df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean().sort_values(by="2022 Population",ascending=False)
print(df2)
df2_ = df2.transpose()
print(df2_)
df2_.plot()
plt.show()

df3 = df.groupby('Continent')[df.columns[5:13]].mean(numeric_only=True).sort_values(by="2022 Population",ascending=False)
print(df3)

df.boxplot(figsize=(20,10))
plt.show()

print(df.select_dtypes(include='float'))