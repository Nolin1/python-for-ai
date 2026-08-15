import pandas as pd

data = {
    "name" : ["Nolin", "Zesan", "Ayman"],
    "Age" : [23, 19, 16]
}

data_frame = pd.DataFrame(data= data, index= ["Brother 1", "Brother 2", "Brother 3"])

print(data_frame)

print(data_frame.loc["Brother 2"])