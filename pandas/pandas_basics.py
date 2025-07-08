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