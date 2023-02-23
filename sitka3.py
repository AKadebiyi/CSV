#1. changing the file to include all the data for the year 2018
#2. change the title to - Daily and low high temperatures - 2018
#3. extract low temps from the file and  add to chart
#4. shade in the area between high and low

import csv
from datetime import datetime

infile = open('sitka_weather_2018_simple.csv','r')

csvfile = csv.reader(infile)

header_row = next(csvfile)
print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []  #y-axis
lows = []
dates = []  #x-axis

#somedate = datetime.strptime('2018-07-01','%Y-%m-%d')
#print(somedate)

for row in csvfile:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    thedate = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(thedate)

print(highs)
print(lows)
print(dates)

import matplotlib.pyplot as plt
fig = plt.figure()

plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c="blue",alpha=0.5)

plt.title("Daily and low high temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature(F), fontsize=16")
plt.tick_params(axis="both",which="major",labelsize=16)
plt.fill_between(dates,lows,highs,facecolor="turquoise",alpha=0.1)

fig.autofmt_xdate()

plt.subplot(2,1,1) #meaning 2 rows and 1 column and 1 is which graph is going to be 1
plt.plot(dates,highs,c="red")
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates,lows,c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()