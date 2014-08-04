get_core_metadata
=================

Examine the USGS core repository online database for updates

purpose
--------
the purpose of this project is to create a set of scripts that examine the United States Geological Survey Core Research Center (USGS-CRC) online database and check for changes on a daily basis.

usage
------
the usgs crc database also handles the following parameters:
townshipnumber=
crclibrarynumber=
state=
type=
cuttings=
fieldsorting=%2Btwnnum
fieldsorting=%2Blibnum
fieldsorting=%2Bmindepth
wellname=
section=
operator=
cores=true
field=
rangenumber=
search=
county=
apinumber=
offset=0
formation=

any of these parameters can be added to the 'data' dict in the usgs_crc.py script (in any order) to refine or modify the query.

