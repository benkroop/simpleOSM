# simpleOSM

simpleOSM is a tool that downloads and renders a map from OpenStreetMaps. It can accept either a bounding box of latitudes and longitudes, or a plain-english search query.

**Usage**

*Search*
To render a map of an area without coordinates, like a city, landmark, or college campus, use the "search" function:
	
	python osm_render_tool.py search "Pittsburgh"

![Pittsburgh](/samples/map_pittsburgh.jpg)

	python osm_render_tool.py search "Harvard"

	python osm_render_tool.py search "Times Square"

![Times Square](/samples/map_manhattan.jpg)

The search funtion can handle most well known places and landmarks and can deal with misspellings.

*Coordinate Render*

To render a map constrained by maximum and minimum latitudes and longitudes, use the "coords" function:
	
	python osm_render_tool.py coords "40.440322, 40.446322, -79.948583, -79.938583"

![CMU](/samples/map_CMU.png)

**Technical Requirements**
- mapnik
- urllib2
- PIL