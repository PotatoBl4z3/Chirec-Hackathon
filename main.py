import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from gui.py import gui()

df = pd.read_csv("Symptoms.csv")
l2 = df.iloc[0, 1:len(df.columns)]
print(l2)
#l1 = gui()
#for a in range(len(df.index)):
#    l2 = df.loc[a, 1:len(df.columns)]