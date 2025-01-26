import pandas as pd
# s=pd.Series([1,2,345,56])

# s=pd.Series([1,2,3,4,5] ,index=['a','b','c','d','e'])
# print(s)
# # data frame
# df =pd.DataFrame({
#     "name":["bruhan ","hiroshi","satoshi namanto"],"marks":[12,14,43]})
# print(df)
# reading files 
# df =pd.read_csv("Walmart Data Analysis and Forcasting.csv")
# print(df)
# if  i want to read the first 5 elements we could use 
# head function
# print(df.head()) 
# # Similarly we could use what we call tail function opposite of head reads the last 5 elements of the file
# print(df.tail())
# if we want to have some information of what kind data inside the file is and in order to calculate min max mean std stander deviation and much more inside the describe function
# print(df.describe())
#  this will tell us the following 
    #      Store       Weekly_Sales  Holiday_Flag  Temperature   Fuel_Price       CPI     Unemployment
# count  6435.000000  6.435000e+03   6435.000000  6435.000000  6435.000000  6435.000000   6435.000000
# mean     23.000000  1.046965e+06      0.069930    60.663782     3.358607   171.578394      7.999151
# std      12.988182  5.643666e+05      0.255049    18.444933     0.459020    39.356712      1.875885
# min       1.000000  2.099862e+05      0.000000    -2.060000     2.472000   126.064000      3.879000
# 25%      12.000000  5.533501e+05      0.000000    47.460000     2.933000   131.735000      6.891000
# 50%      23.000000  9.607460e+05      0.000000    62.670000     3.445000   182.616521      7.874000
# 75%      34.000000  1.420159e+06      0.000000    74.940000     3.735000   212.743293      8.622000
# max      45.000000  3.818686e+06      1.000000   100.140000     4.468000   227.232807     14.313000
# print(df.info())
#   this function tell us the   information about our columns including 
# column type non null columns etc
#  The Expected Results from the output 
#  0   Store         6435 non-null   int64
#  1   Date          6435 non-null   object
#  2   Weekly_Sales  6435 non-null   float64
#  3   Holiday_Flag  6435 non-null   int64
#  4   Temperature   6435 non-null   float64
#  5   Fuel_Price    6435 non-null   float64
#  6   CPI           6435 non-null   float64
#  7   Unemployment  6435 non-null   float64
# df["Store"]
#  inorder to select one item from the csv file we could use ["followd by the name of column"]
# print(df["Store"])
# # 0        1
# 1        1
# 2        1
# 3        1
# 4        1
#         ..
# 6430    45
# 6431    45
# 6432    45
# 6433    45
# 6434    45 
#  In order to calculate the the type of the specific column in our case   store attribute is the one in which we want to find the value 
# print(type(df["Store"]))
# Expected output of this statement
# <class 'pandas.core.series.Series'>
# print(df[["Store","Date"]])
#  ILOC it is a function used to print out the specific row of the file  for example 
# print(df.iloc[23])
#  this will give us the 23rd rows data  from all the column names 
# Store                    1
# Date            16-07-2010
# Weekly_Sales    1448938.92
# Holiday_Flag             0
# Temperature          83.15
# Fuel_Price           2.623
# CPI             211.100385
# Unemployment         7.787
# Name: 23, dtype: object
# df2=pd.read_csv("data.csv")
# print(df2)
# #  now in order to clean those nan fields what we can  do here is that  we can use a function called 
# # dropna means drop not available
# print(df2.dropna())
# #  you can also fill out the nan fields with your desired number so instead of deleting the rows you fill it out with numbers you like 
# print(df2.fillna(2))
# #  if you want to change the name of the column for example
# # suppose you want to change the names of stores columns to dukaan 
# df2.rename(columns={"Store":"dukaan"},inplace=True)
# print(df2)
#  but these changes are temporary if we want to make it permenet we could use something called inplace =True
# this thing make the changes inside\ the file  so every time you wite something with inplace =true it makes it reflected on the actaul file 
# now if we check  the type of data we are storing we could get some thing like string object int64 and float64
# but if you want to change the type iod the column for example in  case of dukaan 
# df2.dropna(inplace=True)
# print(df2)

# df2["Store"] = df2["Store"].astype("int64")
# print(df2.info())
# # now if you want to calculate the length of the dataframe you can use len() or should  i say length function 
# print(len(df2))
# # so there are 6424 number of rows inside the file data.csv 
# #  Now inorder to add the a new field inside the file what we can  do here is that we will add a column named as employees_salery 
# df2["emp_salary"]=[ 0 for i in range(len(df2))]
# print(df2)
# #  A new column emp_salary will be added with the values being all zeros
# # suppose you want to create a new column that has values being the squre of fuel_price you can do that by defining a function named multiply
# def multiply(a):
#     return a*a
# df2["Highest__fuel_price"]=df2["Fuel_Price"].apply(multiply)
# print(df2)
# df2.to_csv("export.csv",index=False)
# merge function in pandas  also concat function
df3=pd.DataFrame({"name":["burhan ameer","harry bhai","hanzla","shinchan"],"marks":[100,100,23,100 ]})
df4=pd.DataFrame({"name":["hiroshi nohara","burhan ameer","doraemon",],"roll":[12,21,43]})
# print(pd.concat([df3,df4]))
#  so what concat function does is it takes the two values and make a table out of it regardless of the fact what values it stores 
# MERGE FUNCTION
# In merge function we can have only the similar values inside the resultant table 
print(pd.merge(df3,df4,on="name"))
#  as you will see from this code segment this will only gives us the values that are in common between two data frames 