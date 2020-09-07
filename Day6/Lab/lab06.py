# TODO: write code to answer the following questions:
# 1) which of these embassies is closest to the White House in meters?
# how far is it, and what is the address?
# 2) if I wanted to hold a morning meeting there, which cafe would you suggest?
# 3) if I wanted to hold an evening meeting there, which bar would you suggest?
import importlib # to import file
import sys # add directory to system PATH
import imp
#imported_items = imp.load_source('temp_name', 'PATH/TO/KEY/FILE')
sys.path.insert(0, '/Users/jinki/Documents/API keys')
# Import items from file
imported_items = importlib.import_module('start_google')
#dir(imported_items)
#gmaps = imported_items.gmaps

gmaps = imported_items.client
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
location = gmaps.geocode(whitehouse)
location # location is a list of dictionaries
# Get location
location[0]['geometry']['location']

# Store coordinates
WHlatlong = location[0]['geometry']['location']

# re-write embassy coordinates into dictionary
embassies = [{'lat': 38.917228, 'lng': -77.0522365},
	{'lat': 38.9076502, 'lng': -77.0370427},
	{'lat': 38.916944, 'lng': -77.048739} ]

# Find the distance (in km) between WH and embassies
#def closest_embassy():
em_distances = []
for i in embassies:
	distance = gmaps.distance_matrix(WHlatlong, i)
	em_distances.append(distance['rows'][0]['elements'][0]['distance']['text'])
embassy_index = em_distances.index(min(em_distances))
destination = gmaps.reverse_geocode(embassies[embassy_index])
embassy_address = destination[0]['address_components']
embassy_address

# find cafes and bars near the embassy!
def find_place(types, standard):
	if type(types) not in [str]:
		raise TypeError("Please enter a place as a string")

	else:
		cafes = gmaps.places(query = types, location = embassies[embassy_index])['results']

		if standard == "distance":
			distance = []
			for i in range(0, len(cafes)):
				coord = cafes[i]['geometry']['location']
				this_distance = gmaps.distance_matrix(embassies[embassy_index], coord)
				distance.append(this_distance['rows'][0]['elements'][0]['distance']['text'])
			cafe_index = distance.index(min(distance))
			cafe_address = cafes[cafe_index]['formatted_address']
			return cafe_address

		elif standard == "rating":
			rating = []
			for i in range(0, len(cafes)):
				rating.append(cafes[i]["rating"])
			cafe_index = distance.index(min(rating))
			cafe_address = cafes[cafe_index]['formatted_address']
			return cafe_address

		elif standard == "popularity":
			users = []
			for i in range(0, len(cafes)):
				users.append(cafes[i]["user_ratings_total"])
			cafe_index = distance.index(min(users))
			cafe_address = cafes[cafe_index]['formatted_address']
			return cafe_address

		else:
			print("Type a valid standard: distance, rating, popularity")

find_place("cafe", "distance")
find_place(3, "rating")
