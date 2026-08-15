import pandas as pd

data = [100, 102, 104]

series = pd.Series(data= data, index=["A", "B", "C"])

print(series)

print(series.loc["A"])      #use keys to locate the value
print(series.iloc[1])       #use index to locate the value