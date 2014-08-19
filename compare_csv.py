import csv
import time
from datetime import date, timedelta
import difflib

timestr = time.strftime("%Y%m%d")
yesterday = date.today() - timedelta(1)
csv_yest = yesterday.strftime('%Y%m%d') + '_usgscrc.csv'
csv_today = timestr + '_usgscrc.csv'

file1 = open(csv_yest, 'r')
file2 = open(csv_today, 'r')

diff = difflib.ndiff(file1.readlines(), file2.readlines())

delta = ''.join( x for x in diff if x.startswith('- ') or x.startswith('+ '))
print delta
