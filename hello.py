import pandas as pd
# s=pd.Series([1,2,345,56])

# s=pd.Series([1,2,3,4,5] ,index=['a','b','c','d','e'])
# print(s)
# # data frame
# df =pd.DataFrame({
#     "name":["bruhan ","hiroshi","satoshi namanto"],"marks":[12,14,43]})
# print(df)
# reading files 
df =pd.read_csv("Walmart Data Analysis and Forcasting.csv")
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
print(df["Store"])
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
print(type(df["Store"]))
# Expected output of this statement
# <class 'pandas.core.series.Series'>