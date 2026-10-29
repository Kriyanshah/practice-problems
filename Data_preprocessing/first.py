import pandas as pd
df = pd.read_csv("C:/Users/kriya/Downloads/Titanic-Dataset.csv")


# dataset dimensions
print("Shape:")
print(df.shape)

# column names and data types
print("\ncolumns:")
print(df.columns)

#  data types
print("\nData types:")
print(df.dtypes)