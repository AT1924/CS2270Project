import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
## Data is day/month/year

def readData(csv_file):
    df = pd.read_csv(csv_file, sep=';', names=["date", "hour", "level"])
    df = df.iloc[1:]
    df.index = pd.to_datetime(df["date"] + "/" + df["hour"], format="%d/%m/%Y/%H:%M")
    df = df.drop(columns=["date", "hour"])

    #dailyList = df.to_numpy()
    #dailyList = np.array_split(dailyList, 365)

    listOfDFRows = df.transpose().values.flatten()
    listOfDFRows = listOfDFRows.astype(float)
    listOfDFRows = np.array_split(listOfDFRows, 365)

    #print("Dataframe shape: ", firstDay.shape)
    #dt = (firstDay.index[-1] - firstDay.index[0])
    #print("Number of hours between start and end dates: ", dt.total_seconds()/3600 + 1)
    #print(listOfDFRows)
    # list of all days
    return listOfDFRows
