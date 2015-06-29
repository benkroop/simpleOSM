import urllib2

def str2coords(user_string):
	searchStr = user_string.replace(' ', '+') + "+wikipedia"

	#print searchStr
	## Do a Google search for the terms the user entered, plus "Wikipedia", then open the first result
	url = 'https://www.google.com/search?q=' + searchStr + '&btnI='
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers={'User-Agent':user_agent,} 

	request = urllib2.Request(url,None,headers)
	response = urllib2.urlopen(request)
	html = response.read()

	# Find the coordinates
	geoURL = "http://" + html[html.index('tools.wmflabs.org'):html.index('"><span', html.index('tools.wmflabs.org'))].replace('&amp;', "&")

	response = urllib2.urlopen(geoURL)
	locactionHTML = response.read()
	latStart = locactionHTML.index('<span class="geo"><span class="latitude" title="Latitude">') + 58
	lat = locactionHTML[latStart:locactionHTML.index('</span>', latStart)]
	lonStart = locactionHTML.index('<span class="longitude" title="Longitude">', latStart) + 42
	lon = locactionHTML[lonStart:locactionHTML.index('</span>', lonStart)]

	lat = float(lat)
	lon = float(lon)

	## By default and for cities let's make a 0.05 degree lat spread and 0.08 lon spread
	minLat = lat - 0.025
	maxLat = lat + 0.025
	minLon = lon - 0.04
	maxLon = lon + 0.04
	## If it's a landmark, make a boudning box that's 0.006 degrees vertically and 0.01 degrees horizontally
	if geoURL.find("landmark") != -1:
		minLat = lat - 0.003
		maxLat = lat + 0.003
		minLon = lon - 0.005
		maxLon = lon + 0.005
	if geoURL.find("edu") != -1:
		minLat = lat - 0.003
		maxLat = lat + 0.003
		minLon = lon - 0.005
		maxLon = lon + 0.005
	print minLat, maxLat, minLon, maxLon
	return minLat, maxLat, minLon, maxLon