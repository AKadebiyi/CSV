#1. handle error checking using try and except
#2. change file to use death valley data


import csv
from datetime import datetime

infile = open('sitka_weather_2018_simple.csv','r')
infile1 = open('death_valley_2018_simple.csv','r')

csvfile = csv.reader(infile)
csvfile1 = csv.reader(infile1)

header_row = next(csvfile)
print(type(header_row))

header_row1 = next(csvfile1)
print(type(header_row1))

for index, column_header in enumerate(header_row):
    print(index, column_header)

for index, column_header in enumerate(header_row1):
    print(index, column_header)

highs = []  #y-axis
lows = []
dates = [] 
names = [] #x-axis

highs1 = []  #y-axis
lows1 = []
dates1 = [] 
names1 = [] #x-axis


for row in csvfile:
    try:
        high = int(row[header_row.index('TMAX')])
        low = int(row[header_row.index('TMIN')])
        thedate = datetime.strptime(row[header_row.index('DATE')],'%Y-%m-%d')
        name = row[header_row.index('NAME')]
    except ValueError:
        print(f'Missing data for {thedate}') #this skips the date that has missing data
    else:
        highs.append(high)
        lows.append(low)
        dates.append(thedate)
        names.append(name)

for row in csvfile1:
    try:
        high1 = int(row[header_row1.index('TMAX')])
        low1 = int(row[header_row1.index('TMIN')])
        thedate1 = datetime.strptime(row[header_row1.index('DATE')],'%Y-%m-%d')
        name1 = row[header_row1.index('NAME')]
    except ValueError:
        print(f'Missing data for {thedate1}') #this skips the date that has missing data
    else:
        highs1.append(high1)
        lows1.append(low1)
        dates1.append(thedate1)
        names1.append(name1)

print(highs)
print(lows)
print(dates)

print(highs1)
print(lows1)
print(dates1)


import matplotlib.pyplot as plt
fig = plt.figure()

#plt.plot(dates,highs,c="red",alpha=0.5)
#plt.plot(dates,lows,c="blue",alpha=0.5)
"""
plt.title("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US", fontsize=16)
plt.xlabel("", fontsize=10)
plt.ylabel("Temperature(F)")
plt.tick_params(axis="both",which="major",labelsize=12)
plt.fill_between(dates,lows,highs,facecolor="turquoise",alpha=0.1)
"""


plt.subplot(2,1,1) #meaning 2 rows and 1 column and 1 is which graph is going to be 1
plt.plot(dates,highs,c="red",alpha=0.5)
plt.plot(dates,lows,c="blue",alpha=0.5)
plt.title(names[0])
plt.xlabel("", fontsize=12)
#plt.ylabel("Temperature(F)")
plt.tick_params(axis="both",which="major",labelsize=12)
plt.fill_between(dates,lows,highs,facecolor="blue",alpha=0.1)


plt.subplot(2,1,2)
plt.plot(dates1,highs1,c="red",alpha=0.5)
plt.plot(dates1,lows1,c="blue",alpha=0.5)
plt.title(names1[0])
plt.xlabel("", fontsize=12)
#plt.ylabel("Temperature(F)")
plt.tick_params(axis="both",which="major",labelsize=12)
plt.fill_between(dates1,lows1,highs1,facecolor="blue",alpha=0.1)


plt.suptitle(f"Temperature comparison between {names[0]} and {names1[0]}")

fig.autofmt_xdate()

plt.show()
