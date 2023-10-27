import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import somegui

df = pd.read_csv("Symptoms.csv")
l2 = df.iloc[0, 1:len(df.columns)].tolist()
l1 = somegui.gui()
for a in range(len(df.index)):
    l2 = df.iloc[a, 1:len(df.columns)].tolist()
    if l1 == l2:
        print(df.iloc[a,0])