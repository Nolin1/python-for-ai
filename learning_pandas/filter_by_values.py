import pandas as pd

# data = [102, 104, 200,240,100]

# series = pd.Series(data = data, index = ["a", "b", "c", "d", "e"])

# print(series[series <= 200])

calories = {
    "day 1" : 1750,
    "day 2" : 2100,
    "day 3" : 1700
}

series = pd.Series(data = calories)
series.loc["day 3"] += 350


print(series[series>2000])