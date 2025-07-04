import pandas as pd
import numpy as np
'''df=pd.DataFrame({
    "Name":["sujal","parth","ritvik","pragathi"],
    "Marks":["11","20","30","40"],

})
print(df)
print(df.isnull())
print(df.fillna(0))#fill the null values with 0
print(df.dropna(inplace=True))
print(df)

print(df.describe())#describe gives the statistical summary of the data
'''
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'C', 'B'],
    'Values': [10, 20, 30, 40, 50]
})

# Group by 'Category' and get mean of 'Values'
print(df.groupby('Category')['Values'].mean())

data ={
    "Name": ["Sujal", "Parth", "Ritvik", "Pragathi"],
    "Math":[80,85,90],
    "Science":[70,75,80],
    "English":[90,95,100],
    }

df = pd.DataFrame(data)
df["Average"]=df[["Math","Science","English"]].mean(axis=1)
print(df.sort_values(by="Average",ascending=False))