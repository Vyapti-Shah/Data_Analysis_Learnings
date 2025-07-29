#Pandas Visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\files\Ice Cream Ratings.csv')
print(df)
df = df.set_index('Date')
print(df) 

print(plt.style.available) #shows all the different styles we can customize our plots
plt.style.use('classic') #classis is one of the style 

df.plot()
plt.show()

df.plot(kind='line',subplots=True)
plt.show()

df.plot(kind = 'line', title = 'Ice Cream Ratings', xlabel = 'Daily Ratings', ylabel = 'Scores')
plt.show()

df.plot(kind='bar',stacked=True) #vertical stacked barchart
plt.show()
df.plot.barh(stacked = True) #horizontal stacked barchart
plt.show()

df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 500, c = 'green')
plt.show()

df.plot.hist(bins = 10)
plt.show()

df.boxplot()
plt.show()

df.plot.area(figsize = (10,5))
plt.show()

df.plot.pie(y='Flavor Rating',figsize=(10,10))
plt.show()
