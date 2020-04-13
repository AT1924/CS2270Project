import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np
import io
## Data is day/month/year

def readData(csv_file):
    df = pd.read_csv(csv_file, sep=';', names=["date", "hour", "level"])
    df = df.iloc[1:8761]

    df["date"] = pd.to_datetime(df["date"] + "/" + df["hour"], format="%d/%m/%Y/%H:%M")

    df["seconds"] = (df["date"] - pd.to_datetime('2015-01-01 00:00:00')).dt.total_seconds()
    df = df.drop(columns=["hour"])
    df = df.drop(columns=["date"])
    df = df.astype('float32').astype('int32')
    #df.index = pd.to_datetime(df["date"] + "/" + df["hour"], format="%d/%m/%Y/%H:%M")

    listOfDFRows = df.to_numpy().tolist()
    for i in range(len(listOfDFRows)):
        listOfDFRows[i].reverse()
    #print("testing", listOfDFRows)




    valuesPerDay = df.transpose().values.flatten()
    valuesPerDay = valuesPerDay.astype(float)
    valuesPerDay = np.array_split(valuesPerDay, 365)




    return listOfDFRows
