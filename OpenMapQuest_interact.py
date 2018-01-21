import output_implement
import json
import urllib.parse
import urllib.request





base_url = 'http://open.mapquestapi.com'
API_key = 'Pqe4U4CGca3SEdPMqFrr2hoFvMOiLaXj'


def url_build(loca_list: list ):
    """'creates an url in json format by taking a starting point and an ending point"""
    dfrom = loca_list[0]
    search_parameters = [('key', API_key), ('from', dfrom )]
    for x in loca_list[1:]:
        search_parameters.append(('to', x))
    return base_url + '/directions/v2/route?' + urllib.parse.urlencode(search_parameters)



def url_read(url: str):
    """takes an url and retrieves its contents in the form of json response converted into a python object"""
    response = None

    try:
        response = urllib.request.urlopen(url)
        url_data = response.read()
        url_str = url_data.decode(encoding = 'UTF-8')
        url_python = json.loads(url_str)
        return url_python
    finally:
        if response != None:
            response.close()



def _url_translate(url: str):
    """replaces all the values of %2C in an URL with commas"""
    too = url.replace('%2C', ',')
    return too

def _elev_organize_and_create_url(x = 'latlngpair'):
    """takes a latlng pair which is inside a dictionary and returns a mapquest api url which, if clicked on, has the json which has the elevation information contained"""
    search_parameters = [('key', API_key)]
    latlng_list = []
    latlng_list.append(str(x['lat']))
    latlng_list.append(str(x['lng']))
    latlng_pairs = ','.join(latlng_list)
    super_tuple = ('latLngCollection',latlng_pairs)
    search_parameters.append(super_tuple)
    bigurl =  base_url + '/elevation/v1/profile?' + _url_translate(urllib.parse.urlencode(search_parameters))
    return bigurl

def elev_url_build(loca_list: list):
    """   takes each latlngpair and return a list of urls (i'm doing this because the url does not allow all the coordinates at once)
    """

    basic = url_build(loca_list)
    infos = url_read(basic)

    url_list = []
    for x in output_implement.LATLONG().raw_latlong(infos):
        url_list.append(_elev_organize_and_create_url(x))
    return url_list

def elev_url_read(url_list: list):
    """takes a list of urls for the elevation API and then returns the json for each one in a list"""
    json_list = []

    for x in url_list:
        response = None

        try:
            response = urllib.request.urlopen(x)
            url_data = response.read()
            url_str = url_data.decode(encoding = 'UTF-8')
            url_python = json.loads(url_str)
            json_list.append(url_python)
        finally:
            if response != None:
                response.close()
    return json_list



