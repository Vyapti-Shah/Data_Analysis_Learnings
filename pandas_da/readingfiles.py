#Reading in Files
import pandas as pd

#csv files
df = pd.read_csv(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\readingfiles\countries of the world.csv',header=None,names=['Country','Region'])
print(df)
df_ = pd.read_table(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\readingfiles\countries of the world.csv',sep=',')
print(df_)

#text files
df_text = pd.read_csv(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\readingfiles\countries of the world.txt',sep='\t')
print(df_text)
df_txt = pd.read_table(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\readingfiles\countries of the world.txt') #we can use read_table to seperate \t
print(df_txt)

#json files
pd.set_option('display.max.column',40) #displays all the columns 
df_json = pd.read_json(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\readingfiles\json_sample.json')
print(df_json)

#excel files
pd.set_option('display.max.row',235) #displays all the rows
df_excel = pd.read_excel(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\readingfiles\world_population_excel_workbook.xlsx',sheet_name='Sheet1')
print(df_excel)
df_excel.info()
print(df_excel.shape)
print(df_excel.head(5))
print(df_excel.tail(5))
print(df_excel['Rank'])
print(df_excel.loc[224]) #prints the data at 224th location of the index 
print(df_excel.iloc[224]) #prints the data at 224th location of the index 
