import string
import sys

sys.path.append("e:\\python")

import json
import urllib

class ServerAPI:

	def __init__(self):
		self.server_host = "http://test.talking-points.org"
		
	def get_location(self, tpid):
		request_url = self.server_host + "/locations/show/" + str(tpid) + ".json"
		response = urllib.urlopen(request_url).read()
		if response == "error":
			return null
		else:
			return json.read(response)
    
	def get_location_by_bluetooth_mac(self, mac): 
		request_url = self.server_host + "/locations/show_by_bluetooth_mac/" + str(mac) + ".json"
		response = urllib.urlopen(request_url).read()
		if response == "error":
			return None
		else:
			return json.read(response)

	def get_nearby_locations(self, lat, lng):
		# convert commas into dots in order to not screw up the Rails URL
		latstr = str(lat)
		lngstr = str(lng)
		lat = string.replace(latstr, '.', ',')
		lng = string.replace(lngstr, '.', ',')
		request_url = self.server_host + "/locations/get_nearby/" + lat + ";" + lng + ".json"
		response = urllib.urlopen(request_url).read()
		if response == "error":
			return None
		else:
			return json.read(response)
		
	def getCurrentAddress(self, lat, lng):
		# convert commas into dots in order to not screw up the Rails URL
		latstr = str(lat)
		lngstr = str(lng)
		lat = string.replace(latstr, '.', ',')
		lng = string.replace(lngstr, '.', ',')
		request_url = self.server_host + "/locations/get_address/" + lat + ";" + lng
		response = urllib.urlopen(request_url).read()
		if response == "error":
			return None
		else:
			return response
		