import output_implement
import OpenMapQuest_interact
from collections import namedtuple


inputlist = namedtuple("inputlist", "number_of_locations location_listy output_type")





def produce_output(inputs: 'inputs tuple'):
    """given an inputlist namedtuple, an url will be built and with the JSON object produced,
    will obtain the information necessary and produce the appropriate output. If in invalid location is provided, then NO ROUTE FOUND is printed.
    if any other error occurs (eg. invalid API key, no internet connection, etc) then MAPQUEST ERROR is printed"""
    urly = OpenMapQuest_interact.url_build(inputs.location_listy)
    try:
        json_object = OpenMapQuest_interact.url_read(urly)
    except:
        print("\nMAPQUEST ERROR")
    else:
        try:
            check_exist = json_object['route']['locations']
        except:
            print("\nNO ROUTE FOUND")
        else:
            for x in inputs.output_type:
                if x == 'STEPS':
                    output_implement.STEPS().maneuver_print(json_object)
                elif x == 'TOTALDISTANCE':
                    output_implement.TOTALDISTANCE().print_distance(json_object)
                elif x == 'TOTALTIME':
                    output_implement.TOTALTIME().print_time(json_object)
                elif x == 'LATLONG':
                    output_implement.LATLONG().print_latlong(json_object)
                elif x == "ELEVATION":
                    eurly = OpenMapQuest_interact.elev_url_build(inputs.location_listy)
                    ejson_object = OpenMapQuest_interact.elev_url_read(eurly)
                    output_implement.ELEVATION().final_elevation(ejson_object)
            print("\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.")





def handle_input():
    """prompts the user for number of locations, then the specific locations, the types of outputs desired, and then returns each in a namedtuple """
    number_of_locations =  location_num()
    location_listy = location_list(number_of_locations)
    output_type = output_desired()
    inputs = inputlist(number_of_locations, location_listy, output_type)
    return inputs


def location_num():
    """takes an integer as input, asks user to insert a new number if int < 2. If int > 2, it simply returns the number"""
    while True:
        location_numbers = int(input())
        if location_numbers < 2:
            print("Please enter a value above 2 or more.")
        else:
            return location_numbers

def location_list(location_numbers: int):
    """for the next number of locations specified by the location number, an input
    line will be made to take a location and return a list of those locations."""

    location_listo = []
    for x in range(location_numbers):
        loc_input = input()
        location_listo.append(loc_input)
    return location_listo

def output_desired():
    """ asks input for a positive integer (at least 1) and for the next (number inputed)
    lines, it will take inputs which describe a certain output and return a list of outputs desired"""
    possible_outputs = ['STEPS', 'TOTALDISTANCE', 'TOTALTIME', 'LATLONG', 'ELEVATION']
    while True:
        out_num = int(input())
        if out_num < 1:
            print ("Please input a positive integer at least 1 or above")
        else:
            desired_outputs = []
            while True:
                for x in range(out_num):
                    desired_output = input()
                    if desired_output in possible_outputs:
                        if desired_output in desired_outputs:
                            pass
                        else:
                            desired_outputs.append(desired_output)
                    else:
                        print("please enter one of the following: ", possible_outputs)
                return desired_outputs


#test_list = ['4533 Campus Dr, Irvine, CA', '1111 Figueroa St, Los Angeles, CA', '3799 S Las Vegas Blvd, Las Vegas, NV']
#fail_list = ['Irvine, CA', 'Lisbon, Portugal']

if __name__ == '__main__':
    get_input_info = handle_input()
    produce_output(get_input_info)





