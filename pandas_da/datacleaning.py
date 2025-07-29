#Data Cleaning
import pandas as pd
df_unfiltered = pd.read_excel(r'C:\Users\vyapti shah\OneDrive\Desktop\pandas_da\files\Customer Call List.xlsx')
print(df_unfiltered)

df = df_unfiltered.drop_duplicates()
print(df)

print()

df = df.drop(columns="Not_Useful_Column")
print(df)

print()

#df["Last_Name"] = df["Last_Name"].str.lstrip("...")
#df["Last_Name"] = df["Last_Name"].str.lstrip("/")
#df["Last_Name"] = df["Last_Name"].str.rstrip("_")
df["Last_Name"] = df["Last_Name"].str.strip("123./_")
print(df)

print()

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[4:7] + '-' + x[8:12])
df["Phone_Number"] = df["Phone_Number"].str.replace('N/a','')
df["Phone_Number"] = df["Phone_Number"].str.replace('NaN','')
df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')
print(df)

df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(pat=',',n=2, expand=True)
print(df)

df["Paying Customer"] = df["Paying Customer"].str.replace('Yes','Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No','N')
print(df)

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes','Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No','N')
print(df)

#df = df.replace('N/a','')
#df = df.replace('NaN','')
df=df.fillna('') #fills blank space in place of NaN
print(df)

for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)
print(df)

for x in df.index:
    if df.loc[x, "Phone_Number"] == '': #if the Phone Number column is blank then remove it
        df.drop(x, inplace=True)
print(df)
#Another way to drop null values => df = df.dropna(subset="Phone_Number"), inplace=True)

df = df.reset_index(drop=True) #drops the index column
print(df)

df = df.reset_index() #index column shown here
print(df)