import urllib2
import urllib
import time
import datetime
import csv

data = {}
data['format'] = 'csv'
data['extension'] = 'csv'
data['analysis'] = 'yes'
data['search'] = 'Search'
data['offset'] = '0'
data['formation'] = 'NIOBRARA'
url_values = urllib.urlencode(data)
base = 'http://my.usgs.gov/crcwc/search/cores'
full_url = base + '?' + url_values
print full_url
response = urllib2.urlopen(full_url)

timestr = time.strftime("%Y%m%d")
csv_name = timestr + '_usgscrc.csv'
yest = str(int(timestr) - 1)
csv_yest = yest + '_usgscrc.csv'

data_file = open(csv_name, 'w')
print>>data_file, response.read()

with open(csv_yest, 'rb') as csvfile:
    core_list_yest = []
    core_strings_yest = []
    row_string_yest = ''    
    corereader = csv.reader(csvfile, delimiter=' ', quotechar ='|')
    for row in corereader:
        core_list_yest.append(row)
    for item in core_list_yest:
	    row_string_yest = ''.join(item)
	    core_strings_yest.append(row_string_yest)

with open(csv_name, 'rb') as csvfile:
    core_list = []
    core_strings = []
    row_string = ''
    corereader = csv.reader(csvfile, delimiter=' ', quotechar ='|')
    for row in corereader:
        core_list.append(row)
	for item in core_list:
	    row_string = ''.join(item)
	    core_strings.append(row_string)

print set(core_strings).difference(core_strings_yest)
