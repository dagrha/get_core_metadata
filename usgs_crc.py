import urllib2
import urllib
import time
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

data_file = open(csv_name, 'w')
print>>data_file, response.read()
