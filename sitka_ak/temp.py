import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2018_simple.csv'

dates, highs, lows = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date) 
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red', alpha=0.5)
ax.plot(dates, lows, c = 'blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='purple', alpha=0.2)

ax.set_title('Daily High Temp in F', fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temp in F', fontsize = 16)
ax.tick_params(axis='both', which="major", labelsize=16)

plt.show()