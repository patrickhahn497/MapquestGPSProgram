


class STEPS:

    def maneuver_print(self, jsono: "json"):
        """takes a json object, prints DIRECTIONS on a line by itself, and in each subsequent line, prints out step by step instructions to the destination
        as specified in the json"""
        print("\nDIRECTIONS")
        print (jsono['route']['legs'][0]['origNarrative'])
        for x in jsono['route']['legs']:
            for y in x['maneuvers']:
                print (y['narrative'])



class TOTALDISTANCE:


    def print_distance(self, jsono: 'json'):
        """takes a json object, and prints TOTAL DISTANCE: followed by the distance in miles rounded to the nearest mile"""
        roundy_dist  = int(round((jsono['route']['distance']), 0))
        print("\nTOTAL DISTANCE: ", roundy_dist, 'mile(s)')


class TOTALTIME:

    def print_time(self, jsono: 'json'):
        """takes a json object, and prints TOTAL TIME: followed by the time in minutes rounded to the nearest minute"""
        roundo_time  = (int(round((jsono['route']['time'])/60, 0)))
        print ("\nTOTAL TIME:", roundo_time , 'minute(s)')


class LATLONG:


    def _ns(self, number: float):
        """checks whether a number is east or west (south would be negative
        while north would be positive). afterwards, it will return a str with the number followed
        by N,S,E, or W depending on the direction determined"""
        if number< 0:
            return str(abs(number)) + 'S'
        elif number == 0:
            return 0
        else:
            return str(abs(number)) + 'N'

    def _ew(self, number: float):
        """checks whether a number is east west, (west would be negative
        while east would be positive).afterwards, it will return a str with the number followed
        by N,S,E, or W depending on the direction determined"""
        if number< 0:
            return str(abs(number)) + 'W'
        elif number == 0:
            return 0
        else:
            return str(abs(number)) + 'E'

    def raw_latlong(self, jsona: 'json'):
        """takes a json object and returns a list of dictionaries containing lat and lng pairs"""
        latlng_list = []
        for x in jsona['route']['locations']:
            latlng_list.append(x['latLng'])
        return latlng_list


    def print_latlong(self, jsona: 'json'):
        """takes a json object and print LATLONGS alone on a line, followed by the lat long coordinates of each location in the format (LAT) (LONG)"""
        print("\nLATLONGS")
        for x in jsona['route']['locations']:
            round_lat = LATLONG()._ns(round(x['latLng']['lat'], 2))
            round_long = (LATLONG()._ew(round(x['latLng']['lng'], 2)))
            print(round_lat , round_long)




class ELEVATION:

    def final_elevation(self, jsonans: list):
        """takes a list of json and then prints out ELEVATIONS alone on one line followed by an integer number of feet of elevation, one per line, for each of the locations
        specified in the input"""
        print("\nELEVATIONS")
        for x in jsonans:
            print(x['elevationProfile'][0]['height'])

