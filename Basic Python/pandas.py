import pandas as pd

# # series(1 dimensional)
# s=pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])
# print(s)

# # dataframes (2 dimensional)
# df =pd.DataFrame({"name": ["saim","haider","fahad"] , "marks" :[12, 13 , 14]})
# print(df)  

# reading csv file
df = pd.read_csv("C:\\Users\\bilga\\OneDrive\\Desktop\\aa.csv")
print(df)

# some functions 
# df.head()          #print first 5 rows
# df.tail()          #print first five columns
# df.describe()      
# df.info()

# data selection
# print(df["Name"])
# print(df[["Name","Age"]])
# print(df.iloc[1])                 #iloc will print the row



# for NAN
# any function on file not change the orignal file make a new copy but if we use inplace then it will make change in orignal
df2=pd.read_csv("C:\\Users\\bilga\\OneDrive\\Desktop\\aaa.csv")
print(df2)

print(df2.fillna("saim"))      
df2.dropna()     #dropna will remove those rows in which data is missing 

print(df2.rename(columns={"Name":"name"}))

print(len(df2))  #give the total number of rows
  
df2["abc"]=[i for i in range(len(df2))]          #to add new column
print(df2)

df2.to_csv("C:\\Users\\bilga\\OneDrive\\Desktop\\b.csv", index=false)     #to save the file

print(pd.concat([df,df2]))     
pd.merge(df,df2 ,on="Name")      #it will merge according to name which are common 





