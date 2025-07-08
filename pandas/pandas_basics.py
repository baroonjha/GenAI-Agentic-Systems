import pandas as pd

##creating dataframe

data={
    "Name": ["Alice", "Bob", "Charlie","David"],
    "Age": [25, 30,22, 35],
    "City": ["New York", "London", "Paris","Tokyo"],

}

df=pd.DataFrame(data)
print("DataFrame:\n",df)
filter_df=df[df["Age"]>30]
print("Filtered DataFrame (Age > 30):\n",filter_df)

print("shape of df:",df.shape)
#DataFrame is a data structure which is made using pandas library 
df.head() #display first 5 rows
df.head(10) #display first 10 rows
df.tail() #display last 5 rows

df.info() #display information about the dataframe
df.describe() #display statistical summary of the dataframe ,it only shows numerical columns

##Indexing 

print("speicifc column:\n",df[["Name","Age"]]) #display specific columns

#series can have only single column or single row
#DataFrame can have multiple columns and rows

print("indexing using row index:\n",df.loc[0]) #accessing first row using index

print("type of above:\n",type(df.loc[0])) #type is series as only single row 

# indexing using column index and row index i.e iloc[row_index, column_index]
print("indexing using column index and row index:\n",df.iloc[0, 2]) #accessing first row and first column
print("indexing using column index and row index:\n",df.iloc[0:2, 0:2]) #accessing first row and second column

#assignment 
#  "Name": ["Alice", "Bob", "Charlie","David"],
#     "Age": [25, 30,22, 35],
#     "City": ["New York", "London", "Paris","Tokyo"],

#first col n last col
print("Assignment:\n",df.iloc[:,[0,-1]])


#converting dataframe to array
df.values #converting dataframe to numpy array
print("DataFrame to array:\n", df.values)

df.isnull() #checking for null values in the dataframe
print("Null values in DataFrame:\n", df.isnull()) #return false when not null and return true when null

df['Age'].value_counts() #counting the unique values in the Age column
print("Value counts of Age column:\n", df['Age'].value_counts())

df['Age'].unique() #getting the unique values in the Age column
print("Unique values in Age column:\n", df['Age'].unique())

