get_core_metadata
=================

Examine the USGS core repository online database for updates

purpose
--------
the purpose of this project is to create a set of scripts that examine the United States Geological Survey Core Research Center (USGS-CRC) online database and check for changes on a daily basis.

usage
------
the usgs crc database also handles the following parameters:
townshipnumber (integer)
crclibrarynumber (integer)
state (string)
type (string)
cuttings (boolean)
wellname (string)
section (integer)
operator (string)
cores (boolean)
field (string)
rangenumber (integer)
county (string)
apinumber (integer)
formation (string)

any of these parameters can be added to/modified in the 'data' dict that is in the usgs_crc.py script (in any order) to refine or modify the query.

