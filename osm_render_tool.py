#!/usr/bin/env python2

from mapnik import *
import sys
from locationSearch import str2coords
from urllib2 import urlopen, URLError, HTTPError
import time
from PIL import Image

def parseInput():
	## To run search, run python osm_render_tool.py search "Boston Copley Square"
	if 'search' in sys.argv:
		searchStr = sys.argv[sys.argv.index('search') + 1]
		try:
			minLat, maxLat, minLon, maxLon = str2coords(searchStr)
			return minLat, maxLat, minLon, maxLon
		except:
			print "Could not find '" + searchStr + "'. Try rephrasing or using coordinate input: python osm_render_tool.py coords 'minLat, maxLat, minLon, maxLon'"
	## To render a map with user-defined lat/lon edges
	elif 'coords' in sys.argv:
		coords = sys.argv[sys.argv.index('coords') + 1].split(',')
		if len(coords) == 4:
			minLat = float(coords[0])
			maxLat = float(coords[1])
			minLon = float(coords[2])
			maxLon = float(coords[3])
			return minLat, maxLat, minLon, maxLon
		else:
			print "Incorrect number of coordinates. Format is: python osm_render_tool.py coords 'minLon, maxLat, maxLon, minLat'"
	else:
		print "Usage: python osm_render_tool.py search 'query' OR python osm_render_tool.py coords 'minLat, maxLat, minLon, maxLon'"
		return -1

def downloadMaps(minLat, maxLat, minLon, maxLon):
	url = 'http://overpass.osm.rambler.ru/cgi/xapi_meta?*[bbox=' + str(minLon) + ',' + str(minLat) + ',' + str(maxLon) + ',' + str(maxLat) + ']'
	# Download map from server
	try:
		f = urlopen(url)
		print "Downloading " + url

        # Open our local file for writing
		with open(os.path.basename('temp_map.osm'), "wb") as map_file:
			map_file.write(f.read())

	#handle errors
	except HTTPError, e:
		print "HTTP Error:", e.code, url
	except URLError, e:
		print "URL Error:", e.reason, url
	return 0

minLat, maxLat, minLon, maxLon = parseInput()
downloadMaps(minLat,maxLat,minLon,maxLon)

print "Rendering Map from XML"

mapfile = 'style.xml'
map_output = 'map.png'

m = Map(4*1024,4*1024)
load_map(m, mapfile)

bbox = (Envelope(minLon, maxLat, maxLon, minLat))

m.zoom_to_box(bbox)
print "Scale = " , m.scale()
render_to_file(m, map_output)

im = Image.open('map.png')