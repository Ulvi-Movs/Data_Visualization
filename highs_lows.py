# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14

@author: ULVI PC
"""

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "daily_weather_World_2020.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        if row[1] == "Poland":
            try:
                current_date = datetime.strptime(row[3], "%Y-%m-%d")
                high = round((float(row[14]) - 32) * 5/9)
                low = round((float(row[16]) - 32) * 5/9)
            except ValueError:
                print(current_date, "missing data")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, highs, c= 'red', alpha = 0.8)
plt.plot(dates, lows, c= 'blue', alpha = 0.8)
plt.fill_between(dates, highs, lows, facecolor= "blue", alpha = 0.1)
plt.title("Daily high and low tempiratures, Poland, 2020", fontsize = 24)
plt.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.show()
