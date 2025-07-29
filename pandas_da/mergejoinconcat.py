#Merge, Join and Concatenate 
import pandas as pd
df1 = pd.read_csv(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\files\LOTR.csv')
print(df1)
df2 = pd.read_csv(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\files\LOTR2.csv')
print(df2)

print()

print("Merge")

print(df1.merge(df2,how='inner')) #Performs an inner join on columns (here FellowshipID and FirstName) and keeps rows where both FellowshipID and FirstName are same

print()

print(df1.merge(df2, how = 'inner', on = ['FellowshipID'])) #it takes FirstName_x and FirstName_y 
#on = ['FellowshipID'] = joins only on the FellowshipID column, but here both df1 and df2 have a FirstName column 
#so pandas keeps both, but to avoid a name clash, it renames them to: FirstName_x from df1 and FirstName_y from df2

print()

print(df1.merge(df2, how = 'inner', on = ['FellowshipID', 'FirstName']))

print()

print(df1.merge(df2, how = 'outer')) #Performs an outer join on columns (here FellowshipID and FirstName) and keeps all the rows regardless of them being same or not

print()

print(df1.merge(df2, how = 'left')) #Performs an left join on columns (here FellowshipID and FirstName) and keeps all the data in the left dataframe (here df1)

print()

print(df1.merge(df2, how = 'right')) #Performs an right join on columns (here FellowshipID and FirstName) and keeps all the data in the right dataframe (here df2)

print()

print(df1.merge(df2, how = 'cross')) 

print()

print("Join")

print(df1.join(df2, on = 'FellowshipID', how = 'outer', lsuffix = '_Left',rsuffix = '_Right')) 
#lsuffix = '_Left',rsuffix = '_Right' => Adds suffixes to columns with the same name (FirstName, in this case): FirstName_Left from df1 and FirstName_Right from df2

print()

df3 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), how = 'outer', lsuffix = '_Left',rsuffix = '_Right')
print(df3)

print()

print("Concat")

print(pd.concat([df1,df2]))
print(pd.concat([df1,df2], join = 'inner')) #only same 
print(pd.concat([df1,df2], join = 'outer', axis = 1)) #all

print()

#df1.append(df2) #As of Pandas v1.4.0 the DataFrame.append() method is deprecated and will be removed in future versions.