import csv
import matplotlib.pyplot as plt
from datetime import datetime as ddt
import matplotlib.dates as mdates

fname = input('Enter the name of the csv file : ')
lablel = input('Enter the label : ')

fileobj = open(fname+'.csv')
read = csv.reader(fileobj)
header = next(read)

date = []
adjclose = []

for row in read:
    date.append(ddt.strptime(row[0].strip(), '%Y-%m-%d'))
    adjclose.append(float(row[5]))

fig = plt.figure()
ax = plt.subplot2grid((1, 1), (0, 0))

for labels in ax.xaxis.get_ticklabels():
    labels.set_rotation(45)

ax.plot_date(date, adjclose, '-', xdate=True, ydate=False, label=label),
ax.grid(True)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b-%d'))  # modifying date format

plt.subplots_adjust(left=0.2, bottom=0.2, right=0.95, top=0.95, wspace=0.2, hspace=0.25)
plt.title('Microsoft Inc')
plt.xlabel('Date')
plt.ylabel('Adj.close')
plt.legend()

plt.show()
