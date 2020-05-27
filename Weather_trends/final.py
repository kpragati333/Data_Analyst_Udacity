# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = pd.read_csv('global_delhi.csv')
y=  pd.read_csv('global_city.csv')
avg_num = 10
x["rollingAverage"] = x["avg_temp"].rolling(window = avg_num).mean()
y["rollingAverage"] = y["avg_temp"].rolling(window = avg_num).mean()


print("Printing city avg with respect to global avg")

plt.plot("year","rollingAverage", data =x, label = "DELHI")
plt.plot("year","rollingAverage", data =y, label = "Global")
plt.legend()
plt.ylabel("Temperature in °C")
plt.xlabel("Year")
plt.title("Temperature time-series city")
plt.show()



