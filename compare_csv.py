import csv
import time
from datetime import date, timedelta

corenums_yest = []
topdepth_yest = []
corenums_today = []
topdepth_today = []
timestr = time.strftime("%Y%m%d")
yesterday = date.today() - timedelta(1)
csv_yest = yesterday.strftime('%Y%m%d') + '_usgscrc.csv'
csv_today = timestr + '_usgscrc.csv'

with open(csv_yest, 'rb') as csvfile1:
    corereader1 = csv.reader(csvfile1)
    for row in corereader1:
        corenums_yest.append(row[7])
        topdepth_yest.append(row[24])

with open(csv_today, 'rb') as csvfile2:
    corereader2 = csv.reader(csvfile2)
    for row in corereader2:
        corenums_today.append(row[7])
        topdepth_today.append(row[24])
        
index_yest = corenums_yest + '-' + topdepth_yest
index_today = corenums_today + '-' + corenums_today

s = set(index_today)
differences = [x for x in index_yest if x not in s]

print differences
