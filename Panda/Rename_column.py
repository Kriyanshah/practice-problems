import pandas as pd
# sample data 
data = {
    "A": [25,30,35],
    "B": ["John", "doe", "smith"],
    "C": [50000,60000,70000]
}
df = pd.DataFrame(data)
print(df)

# rename columns
df.rename(columns={"A": "Age", "B": "Name", "C": "Salary"}, inplace= True)
print(df.to_string(index=False))